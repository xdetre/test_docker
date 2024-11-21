FROM python:latest AS aplication

RUN pip install Flask

COPY server.py /app/
COPY resources.py /app/

CMD ["python", "app/server.py"]