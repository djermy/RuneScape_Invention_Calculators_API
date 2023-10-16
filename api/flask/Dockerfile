# use the python 3.11-alpine container image
FROM python:3.11-alpine

# create a non-root user and group
RUN addgroup -g 1000 uwsgiuser && \
    adduser -D -u 1000 -G uwsgiuser uwsgiuser

# set the working directory to app/
WORKDIR /app

# copy the current directory contents into the container at /app
ADD . /app

# install needed components
RUN apk add --no-cache gcc g++ musl-dev linux-headers build-base pcre-dev

# install the dependencies
RUN pip install -r requirements.txt

# change owenership of the application directory to the non-root user
RUN chown -R uwsgiuser:uwsgiuser /app

# switch to the non-root user
USER uwsgiuser

# run the command to start uwsgi
CMD ["uwsgi", "app.ini"]