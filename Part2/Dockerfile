FROM python:3.11

COPY ./requirements.txt /temp/requirements.txt
COPY ./wildberries /wildberries
WORKDIR /wildberries

RUN pip install --upgrade pip
RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password wb-user

USER wb-user

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
