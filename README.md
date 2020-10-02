![codespell](https://github.com/ucalyptus/scikit-on-gRPC/workflows/codespell/badge.svg)
![autoblack_push](https://github.com/ucalyptus/scikit-on-gRPC/workflows/autoblack_push/badge.svg)
# scikit-on-gRPC
Using Protocol Buffers and gRPC client-server communication to deploy a scikit-learn joblib exported model.

### A brief overview about Protocol Buffers
Let us assume that we have a data which we want to be in a particular structure and we want to store it somewhere so that it can be shared. Protocol is the process to do exactly this. It helps us serialize structure data so that it can be used afterwards. The method involves an **interface description language** that describes the structure of some data and a program that generates source code from that description for generating or parsing a stream of bytes that represents the structured data.

You need to specify the structure of the data along with the services that you’re serializing by defining the message types in .proto file. Think of this message as a logical record of information in which you specify a message with values. That code then goes to the compiler which compiles it with protocol. A predetermined schema is used to encode and decode the message.


![](https://www.c-sharpcorner.com/article/protocol-buffer-a-beginners-walk-through-moving-beyond-xml-and-json/Images/To-use-Protocol-Buffers-it-is-necessary-to-generate-code-for-each-message-that-needs.png)



A Small Example :-
```
//polyline.proto
syntax = "proto2";

message Point {
  required int32 x = 1;
  required int32 y = 2;
  optional string label = 3;
}

message Line {
  required Point start = 1;
  required Point end = 2;
  optional string label = 3;
}

message Polyline {
  repeated Point point = 1;
  optional string label = 2;
}
```

### Learn about Protocol Buffers [here](https://developers.google.com/protocol-buffers/docs/pythontutorial)


## Usage

- `conda create -n grpcenv python=3.6`
- `conda activate grpcenv`
- `cd scikit-on-gRPC/`
- `pip install -r requirements.txt`
- Open in one terminal 
- `python credit_card_prediction_server.py`
- In another terminal open 
- `python credit_card_prediction_client.py`
