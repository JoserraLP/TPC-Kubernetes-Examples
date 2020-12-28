FROM python:3.7
COPY app.py /app.py
RUN pip install --no-cache-dir flask
EXPOSE 5000
ENTRYPOINT env FLASK_APP=app.py flask run --host=0.0.0.0