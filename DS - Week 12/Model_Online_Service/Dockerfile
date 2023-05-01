FROM jupyter/scipy-notebook

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt 

COPY train.csv ./train.csv
COPY test.json ./test.json

COPY train.py ./train.py
COPY api.py ./api.py


RUN python3 train.py
