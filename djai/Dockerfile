FROM python:3.8.3

RUN pip install --upgrade pip

RUN useradd -m user
USER user

WORKDIR /home/user/api

ENV PATH="/home/user/.local/bin:${PATH}"

COPY api/requirements.txt api/requirements.txt

RUN pip install -r api/requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
