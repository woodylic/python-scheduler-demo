FROM python:3-alpine

WORKDIR /usr/src

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/* .

CMD [ "python", "./scheduler.py" ]
