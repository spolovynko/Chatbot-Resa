FROM python:3.8.5-slim-buster
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y libgl1-mesa-glx libgomp1
RUN apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6
RUN apt-get clean && \ 
    rm -rf /var/lib/apt/lists/*
COPY . /ChatBot
WORKDIR /ChatBot
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm

