# Dockerfile
FROM python:3.6

COPY requirements.txt /

RUN pip install -r requirements.txt

# copy files from local machine to docker image
COPY . /

EXPOSE 8000

RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
CMD ["sh", "-c", "tail -f /dev/null"]
