# use the python 3.11-alpine container image
FROM python:3.11-alpine

# set the working directory to app/
WORKDIR /app

# copy the current directory contents into the container at /app
ADD . /app

# install needed components
RUN apk add --no-cache gcc g++ musl-dev linux-headers

# install the dependencies
RUN pip install -r requirements.txt

# run the command to start uwsgi
CMD ["uwsgi", "app.ini"]