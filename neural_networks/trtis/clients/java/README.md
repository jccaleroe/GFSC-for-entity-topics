``` 
https://github.com/protocolbuffers/protobuf/releases/latest
./configure
make
make check
sudo make install
sudo ldconfig # refresh shared library cache.

protoc -I=. --java_out=. model_config.proto
protoc -I=. --java_out=. request_status.proto
protoc -I=. --java_out=. server_status.proto
protoc -I=. --java_out=. grpc_service.proto

https://mvnrepository.com/artifact/io.grpc/protoc-gen-grpc-java
protoc --plugin=protoc-gen-grpc-java=protoc-gen-grpc-java-1.23.0-linux-x86_64.exe   --grpc-java_out=. grpc_service.proto
```