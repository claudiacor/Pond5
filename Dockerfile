FROM python:3
COPY . /app
WORKDIR /app
# install dependencies
RUN pip install -r requirements.txt
#CMD tells Docker to execute the command when the image loads.
CMD ["python", "app.py"]
