FROM python:latest
LABEL org.opencontainers.image.authors="juanherruzo@gmail.com"


RUN python3 -m ensurepip --upgrade
RUN python3  -m pip install --upgrade pip
#pip install pipreqs
 #
 #pipreqs /path/to/project

WORKDIR /bot
COPY ./requirements.txt .
COPY ./alembic ./alembic
COPY ./alembic.ini .
COPY ./BaseBot ./BaseBot
COPY ./start_bot.py .
COPY ./main.py .


RUN pip3 install -r requirements.txt



CMD ["python", "main.py"]