FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY app.py /app/

COPY models /app/models

COPY templates /app/templates

COPY data /app/data 

EXPOSE 5000

CMD ["flask", "run","--host", "127.0.0.1", "--port", "5000"]