FROM python:3.8-alpine3.12

WORKDIR /usr/src/

COPY . /usr/src/

RUN pip install -r requirements.txt

CMD ["flask", "run", "--host", "0.0.0.0"]
