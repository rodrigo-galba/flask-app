FROM python:3.7-slim

COPY requirements.txt /app/
WORKDIR /app

RUN pip install --upgrade pip \
    &&  pip install --trusted-host pypi.python.org --requirement requirements.txt

COPY src/* /app/

CMD ["python", "app.py"]