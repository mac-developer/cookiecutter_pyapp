FROM python:3.5.2

RUN echo Europe/Madrid > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app
RUN wget -q https://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-2.1.7.tar.gz && \
    tar xzf mysql-connector-python-2.1.7.tar.gz && \
    cd mysql-connector-python-2.1.7 && \
    python setup.py install && \
    cd .. && rm -rf mysql-connector-python-2.1.7 && \
    pip install --no-cache-dir .

# ENTRYPOINT ["run", "-c", "{{ cookiecutter.project_slug }}/etc/config.ini", "-l", "{{ cookiecutter.project_slug }}/logs/{{ cookiecutter.project_slug }}.log"]
ENTRYPOINT ["run"]
CMD []

EXPOSE 8080
