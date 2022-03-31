FROM python:3.9
RUN pip3 install flask click
RUN apt-get update && apt-get install curl -y
WORKDIR /usr/src/app
COPY *.py ./
COPY ./templates ./templates
CMD ["python3", "MainScore.py"]