docker rm extract-container

docker build -t mlapi-build -f build.Dockerfile .
docker create --name extract-container mlapi-build

rm dist/mlapi_server -rf
mkdir dist -p

docker cp extract-container:/app/dist/mlapi_server ./dist/mlapi_server
