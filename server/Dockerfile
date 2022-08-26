FROM python:3.10.4-alpine3.16
RUN pip install --upgrade pip
RUN pip install gunicorn[gevent]
RUN pip install requests Flask Flask-Cors openpyxl mysql-connector-python==8.0.29 pyjwt
RUN pip install bcrypt

WORKDIR /app
COPY . /app
RUN mkdir /app/entitys_data
EXPOSE 4050

CMD gunicorn --worker-class gevent --workers 4 --bind 0.0.0.0:4050 wsgi:app --max-requests 10000 --timeout 150 --keep-alive 5 --log-level debug