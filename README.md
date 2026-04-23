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

## Building for release

To create a release build, the best approach is to use docker, to have a clean environment.

The `build.Dockerfile` should be used for that:

```shell
docker build -t mlapi-build -f build.Dockerfile .
docker create --name extract-container mlapi-build
rm dist/mlapi_server -rf
mkdir dist -p
docker cp extract-container:/app/dist/mlapi_server ./dist/mlapi_server
```

Optionally, cleanup the temporary container:

```shell
docker rm extract-container
```