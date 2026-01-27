FROM python:3.9.10-slim-buster
RUN pip install flask
COPY ./static /home/microweb_app/static/
COPY ./templates /home/microweb_app/templates/
COPY ./flask_app.py /home/microweb_app/
EXPOSE 5050
CMD python /home/microweb_app/flask_app.py