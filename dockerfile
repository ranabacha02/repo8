
COPY . .

RUN pip install -r requirements.txt

RUN python manage.py makemigrations

EXPOSE 8000/tcp

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
