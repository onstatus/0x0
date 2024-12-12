FROM python:latest
#RUN apt update -y && apt install python3 python3-pip sqlite3 libmagic-dev -y
#COPY . /data
RUN git clone https://github.com/mia-0/0x0.git app && cd app && pip3 install --no-cache-dir -r requirements.txt
WORKDIR /app
RUN cp instance/config.example.py instance/config.py && sed -i "s#/path/to#/app/mnt#;s#FHOST_USE_X_ACCEL_REDIRECT = True#FHOST_USE_X_ACCEL_REDIRECT = False#;s#USE_X_SENDFILE = False#USE_X_SENDFILE =True#" instance/config.py && touch app.db && FLASK_APP=fhost flask db upgrade
EXPOSE 5000
CMD ["flask","--app","fhost.py","run","-h","0.0.0.0"]
