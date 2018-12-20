FROM python:3.7

COPY . /app

WORKDIR /app
RUN pip3 install -r requirements.txt
RUN pip install .

ENTRYPOINT ["/app/entrypoint.sh"]
