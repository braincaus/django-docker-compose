FROM alpine:latest
LABEL manteiner = "braincaus@gmail.com"
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache && \
    mkdir /application
WORKDIR /application
COPY requirements.txt /application/
RUN pip3 install -r requirements.txt
COPY . /application/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000