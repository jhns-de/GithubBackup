# GithubBackup

Docker Container to Download all Github Repos automatically.

```
docker run -v /your/backup/location:/backup \
  -e "github_token=YOUR_GITHUB_TOKEN" \
  jhns/githubbackup:latest
```
