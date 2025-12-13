# ml-api-test
A simple project to test fastmlapi package

## Running in Docker

1. Create a docker image
```shell
docker build -t ml-api-test-img .
```

2. Run the container with port 8001 redirected (choose the 8001 port so it's unique in the system)
```shell
docker run -d --name ml-api-test -p 8001:8000 ml-api-test-img
```
