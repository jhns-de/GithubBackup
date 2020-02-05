# GithubBackup

![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/jhns/githubbackup)
![Docker Image CI](https://github.com/jhns-de/GithubBackup/workflows/Docker%20Image%20CI/badge.svg?branch=master)
![Docker Image CI](https://github.com/jhns-de/GithubBackup/workflows/Docker%20Image%20CI/badge.svg?branch=dev)

Docker Container to Download all Github Repos automatically.

```
docker run -v /your/backup/location:/backup \
  -e "github_token=YOUR_GITHUB_TOKEN" \
  jhns/githubbackup:latest
```
