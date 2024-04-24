FROM python:3.12

RUN mkdir /ecom_today

WORKDIR /ecom_today

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


