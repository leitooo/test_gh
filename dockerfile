FROM python:3.10

RUN mkdir /app 
WORKDIR /app

COPY app.py .
COPY requirements.txt . 

RUN pip install --no-cache-dir -r requirements.txt

VOLUME [ "/data" ]

CMD [ "python", "app.py" ]
