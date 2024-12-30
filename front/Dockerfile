FROM python:3.10
WORKDIR /front
COPY main.py /front/main.py
COPY requirements.txt /front/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8002
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]