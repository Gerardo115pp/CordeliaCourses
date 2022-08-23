from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
import repository.customers as CustomersRepo
import repository.courses as CoursesRepo
import database.mysql as mysql_database
from handlers.customers import customers_handler
from handlers.courses import courses_handler
from workflows import acceses
import os


server_config = {
    "JWT_SECRET": os.getenv("JWT_SECRET"),
    "COURSES_SPECIAL_ACCESSES": [],
    "COURSES_DIRECTORY": os.getenv("COURSES_DIRECTORY"),
    "DATA_VERSION": int(os.getenv("DATA_VERSION", 1))
}

assert server_config["JWT_SECRET"] is not None, "JWT_SECRET is not set"
assert server_config["COURSES_DIRECTORY"] is not None, "COURSES_DIRECTORY is not set"


def createApp():
    """ SETTING UP REPOSITORIES """
    
    app = Flask(__name__)
    CORS(app)
    app.config.update(**server_config)
    app.register_blueprint(customers_handler, url_prefix="/customers")
    app.register_blueprint(courses_handler, url_prefix="/courses")

    @app.route("/health", methods=["GET"])
    def health():
        return make_response(jsonify({"status": "ok"}), 200)

    @app.route("/data-version", methods=["GET"])
    def getDataVersion():
        response = make_response(jsonify({"data_version": app.config["DATA_VERSION"]}), 200)
        response.headers.add_header("Content-Type", "application/json")
        response.headers.add_header("X-Data-Version", app.config["DATA_VERSION"])
        
        return response
        
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