FROM python:3.8.3-alpine

RUN pip install --upgrade pip
RUN apk update
RUN apk add bash
RUN apk add postgresql-dev gcc python3-dev musl-dev

RUN adduser -D user
USER user
WORKDIR /home/user/api

ENV PATH="/home/user/.local/bin:${PATH}"

COPY api/requirements.txt api/requirements.txt

RUN pip install --user -r api/requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
