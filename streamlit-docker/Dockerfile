FROM python:3.6

EXPOSE ${SD_PORT}

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD streamlit run --server.port ${SD_PORT} processing/app.py