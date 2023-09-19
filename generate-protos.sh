# python -m grpc_tools.protoc        : runs the protobuf compiler, which will generate Python code from the protobuf code.
# -I protos                          : tells the compiler where to find files that your protobuf code imports. 
#                                    : You don’t actually use the import feature, but the -I flag is required nonetheless.
# --python_out=. --grpc_python_out=. : tells the compiler where to output the Python files. As you’ll see shortly, 
#                                    : it will generate two files, and you could put each in a separate directory with these options 
#                                    : if you wanted to.
# protos/recommendations.proto       : is the path to the protobuf file, which will be used to generate the Python code.

echo "Generating Protos"

# Generate grpc files at for client
python -m grpc_tools.protoc -I protos --python_out=./client/pb --grpc_python_out=./client/pb protos/recommendations.proto

# Generate grpc files at for server
python -m grpc_tools.protoc -I protos --python_out=./server/pb --grpc_python_out=./server/pb protos/recommendations.proto

echo "Finished"