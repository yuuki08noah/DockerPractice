FROM python:3.10
WORKDIR /docker
COPY main.py /docker/main.py
COPY requirements.txt /docker/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]