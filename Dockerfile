FROM python:3.9.10-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /ygo_marketplace
COPY requirements.txt /ygo_marketplace/
RUN pip install -r requirements.txt
COPY . /ygo_marketplace/

# EXPOSE 8000