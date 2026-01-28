/bin/python3 /home/devasc/DevOps_R0994211_25-26/Python_Virtual_Environment/flask_login/flask_app_login.py
## bash om venv te starten ^^

## code om container aan te maken + container te runnen
docker build -t docker_login_image .
docker run --name docker_login -p 5555:5555 docker_login_image