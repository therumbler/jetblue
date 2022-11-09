FROM python:3.10
WORKDIR /app
EXPOSE 8000
RUN python -m pip install pip --upgrade
RUN python -m pip install pipenv
RUN pipenv --python 3.10
ADD Pipfile .
ADD Pipfile.lock .

RUN pipenv sync
COPY . .
# RUN cat Pipfile
# RUN ls -la /app

ENTRYPOINT [ "./docker-entrypoint.sh" ]

