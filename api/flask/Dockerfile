FROM python:3.11-alpine

WORKDIR /app

RUN apk add --no-cache gcc g++ musl-dev linux-headers

RUN python -m venv venv
RUN source venv/bin/activate

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run"]