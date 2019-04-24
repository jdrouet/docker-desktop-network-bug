# Network bug in Docker Desktop

## How to reproduce

Run the following command

```bash
docker run --rm -v $(pwd):/code -w /code python:latest python main.py
```

Wait until it stops.
Then try to access the internet from any container and you won't be able to

```bash
docker run --rm python:latest curl https://www.docker.com
```
