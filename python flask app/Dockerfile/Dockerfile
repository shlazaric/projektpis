FROM python:3.11.3-alpine
WORKDIR /python-flask-app-work-dir
ADD . /python-flask-app-work-dir 
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python","main.py"]

# docker build --tag python-flask-app:1.0 .
# docker run  -p 5000:8080 python-flask-app:1.0