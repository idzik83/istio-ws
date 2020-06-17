FROM python:3.7-stretch
WORKDIR app
COPY requirements.txt .
COPY config config
RUN pip install -r requirements.txt
COPY server server
EXPOSE 8080
CMD ["gunicorn", "-c", "config/gunicorn_config.py", "server.api:web_app"]