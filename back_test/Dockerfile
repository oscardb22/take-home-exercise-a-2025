FROM python:3.11.12-slim-bookworm

LABEL maintainer="Oscar Dominguez <oscardb22@gmail.com>"

ENV TZ="America/Bogota"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /back_app

RUN ls /usr/share/zoneinfo\
    && cp /usr/share/zoneinfo/America/Bogota /etc/localtime \
    && echo "America/Bogota" >  /etc/timezone \
    && date
RUN apt-get update && apt-get install -y --no-install-recommends \
    g++ \
    gcc \
    libffi-dev \
    libpq-dev \
    python3-dev \
    tzdata \
    libc-dev \
    unzip \
    libreoffice \
    default-jre \
    libmagic1 \
    libglib2.0-0 \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    telnet \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

COPY back_test/ .

RUN pip install -U pip wheel
RUN pip install --no-cache-dir -r requeriments.txt
RUN python manage.py makemigrations authentication
RUN python manage.py makemigrations parking
RUN python manage.py migrate
RUN python manage.py collectstatic

RUN chmod -R 777 ./*

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0:8000"]