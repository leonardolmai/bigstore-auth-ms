FROM python:3.10
LABEL authors="Leonardo Lima"
WORKDIR /app
RUN pip install --upgrade pip
COPY . /app
RUN pip install -r requirements/requirements.txt
EXPOSE 8001
CMD ["python3", "main.py"]
