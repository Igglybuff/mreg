FROM python:3.7

RUN git clone "https://github.com/Igglybuff/mreg" /app

WORKDIR /app
RUN pip3 install -r requirements.txt
RUN pip install .

ENTRYPOINT ["/app/entrypoint.sh"]
