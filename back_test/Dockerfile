FROM python:3.11.12-slim-bookworm

# Metadatos del contenedor
LABEL maintainer="Oscar Dominguez <oscardb22@gmail.com>"
# CONFIGURAR LA ZONA HORARIA
ENV TZ="America/Bogota"
# Desactiva la salida en búfer de Python para evitar problemas de logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Establece el directorio de trabajo en el contenedor
WORKDIR /back_test

# Instala dependencias del sistema necesarias
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
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Copia el resto de los archivos del proyecto al directorio de trabajo del contenedor
COPY . .

# Instala pipenv
RUN pip install -U pip wheel
RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py makemigrations authentication
RUN python manage.py makemigrations parking
RUN python manage.py migrate

EXPOSE 8000

# Configuration found at "gunicorn.conf.py"
CMD [ "gunicorn", "back_test.asgi:application"]
