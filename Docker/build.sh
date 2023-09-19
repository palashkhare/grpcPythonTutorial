cd $(git rev-parse --show-toplevel)

VERSION=$(cat ./VERSION)
#./generate-protos.sh

docker build -t python-grpc-client:$VERSION -f Docker/dockerfile.client .
docker build -t python-grpc-server:$VERSION -f Docker/dockerfile.server .
