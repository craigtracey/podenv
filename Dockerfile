FROM python:2.7

RUN mkdir -p /opt
RUN pip install flask
COPY app.py /opt/

WORKDIR /opt
CMD [ "flask", "run", "--host", "0.0.0.0" ]
