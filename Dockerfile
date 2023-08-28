FROM python:3.11

WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt

LABEL authors="de.nuriakhmetov"

CMD ["python3", "./main.py"]
