from flask import Flask, request, make_response, jsonify
from email.message import EmailMessage
import ssl
import smtplib
from flask_cors import CORS
import repository.customers as CustomersRepo
import repository.courses as CoursesRepo
import database.mysql as mysql_database
from handlers.customers import customers_handler
from handlers.courses import courses_handler
from workflows import acceses
from datetime import datetime
import os


server_config = {
    "JWT_SECRET": os.getenv("JWT_SECRET"),
    "COURSES_SPECIAL_ACCESSES": [],
    "COURSES_DIRECTORY": os.getenv("COURSES_DIRECTORY"),
    "DATA_VERSION": int(os.getenv("DATA_VERSION", 1)),
    "MAIL_SERVER": os.getenv("MAIL_SERVER"),
    "MAIL_PORT": int(os.getenv("MAIL_PORT")),
    "MAIL_USERNAME": os.getenv("MAIL_USERNAME"),
    "MAIL_PASSWORD": os.getenv("MAIL_PASSWORD"),
    "SECURE_EMAIL_SENDER": os.getenv("MAIL_USERNAME"),
    "MAIL_USE_TLS": True,
    "MAIL_USE_SSL": False,
    "MAIL_DEBUG": True,
    "PASSWORD_RECOVERY_REQUESTS": {}, # {email: {token: str, timestamp: datetime}}
    "CORDELIA_WEBAPP": os.getenv("CORDELIA_WEBAPP")
}

print(server_config)
assert server_config["JWT_SECRET"] is not None, "JWT_SECRET is not set"
assert server_config["COURSES_DIRECTORY"] is not None, "COURSES_DIRECTORY is not set"


def createApp():
    """ SETTING UP REPOSITORIES """
    
    app = Flask(__name__)
    CORS(app)
    app.config.update(**server_config)

    app.register_blueprint(customers_handler, url_prefix="/customers")
    app.register_blueprint(courses_handler, url_prefix="/courses")

    # Setting up / handlers

    @app.route("/health", methods=["GET"])
    def health():
        return make_response(jsonify({"status": "ok"}), 200)

    @app.route("/data-version", methods=["GET"])
    def getDataVersion():
        response = make_response(jsonify({"data_version": app.config["DATA_VERSION"]}), 200)
        response.headers.add_header("Content-Type", "application/json")
        response.headers.add_header("X-Data-Version", app.config["DATA_VERSION"])
        
        return response
    
    @app.route("/password-recovery", methods=["POST"])
    def passwordRecovery():
        email = request.json.get("email")
        if email is None:
            return make_response(jsonify({"error": "email is required"}), 400)
        
        # if password recovery was requested less then 24h ago.
        last_request = app.config["PASSWORD_RECOVERY_REQUESTS"].get(email, None)
        if last_request is not None:
            if datetime.now() - last_request["timestamp"] < datetime.timedelta(hours=24):
                print(f"Too many password recovery requests for {email}")
                return make_response(jsonify({"error": "password recovery was requested less then 24h ago"}), 400)
        

        customer = CustomersRepo.getByEmail(email)
        if customer is None:
            print(f"Password recovery requested for non-existing email: {email}")
            return make_response("", 200) # behave equally if the email is registered or not
        
        
        
        token = acceses.generatePasswordRecoveryToken(customer.id, email, app.config["JWT_SECRET"])
        app.config["PASSWORD_RECOVERY_REQUESTS"][email] = {
            "token": token,
            "timestamp": datetime.now().timestamp()
        }
        
        
        # send email
        mail_body = f"Your password recovery link is: {app.config['CORDELIA_WEBAPP']}/password-recovery?token={token}"
        email_message = EmailMessage()
        email_message["Subject"] = "Password recovery"
        email_message["From"] = app.config["MAIL_USERNAME"]
        email_message["To"] = email
        email_message.set_content(mail_body)
        
        ssl_context = ssl.create_default_context()
        
        with smtplib.SMTP_SSL(app.config["MAIL_SERVER"], app.config["MAIL_PORT"], context=ssl_context) as server:
            server.login(app.config["MAIL_USERNAME"], app.config["MAIL_PASSWORD"])
            server.sendmail(app.config["MAIL_USERNAME"], email, email_message.as_string())
        
        
        return make_response("", 200)
 
    # customers repository
    customers_repo: CustomersRepo.CustomersRepo = mysql_database.createCustomersRepo()
    CustomersRepo.setRepository(customers_repo) 
    
    # courses repository
    courses_repo: CoursesRepo.CoursesRepo = mysql_database.createCoursesRepo()
    CoursesRepo.setRepository(courses_repo)
    
    """ SETTING UP COURSES DATA """
    special_access_map = CoursesRepo.getSpecialAccessMap()
    app.config["COURSES_SPECIAL_ACCESSES"] = acceses.getAccessFromFile(special_access_map)
    return app

if __name__ == "__main__":
    app = createApp()
    app.run(debug=True, host="localhost", port=4050)