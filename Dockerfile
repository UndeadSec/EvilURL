FROM python:3.6-alpine

WORKDIR /home/
COPY . /home/

ENTRYPOINT [ "python3" ]
CMD [ "evilurl.py" ]