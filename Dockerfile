FROM python:latest
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY ./app/app.py /app.py
WORKDIR /
CMD ["flask", "run"]
