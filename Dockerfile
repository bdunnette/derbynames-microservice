# syntax=docker/dockerfile:1

FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# EXPOSE 5000
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
EXPOSE 8000
ENTRYPOINT ["gunicorn","-b","0.0.0.0","-w","4","app:app"]
