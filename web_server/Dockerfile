FROM python:3.10

WORKDIR /web_server
COPY requeriments.txt /web_server/requeriments.txt

RUN pip3 install --no-cache-dir --upgrade -r /web_server/requeriments.txt

COPY . web_server/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]