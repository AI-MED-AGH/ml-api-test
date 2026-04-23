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

All the instructions needed to build are packed in the `build_release.sh` file, so simply run it:

```shell
./build_release.sh
```


The builded package will be available in a `dist/mlapi_server` folder
