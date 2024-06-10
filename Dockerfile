FROM python:3.12.4

RUN apt-get update && apt-get --yes install git

RUN pip install PyGithub GitPython

WORKDIR /root

ADD ./backup.py /root/backup.py

ENTRYPOINT python -u /root/backup.py
