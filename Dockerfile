FROM python:3.6

RUN pip --no-cache-dir install PyGithub GitPython

ADD ./backup.py /root/backup.py

ENTRYPOINT python -u /root/backup.py
