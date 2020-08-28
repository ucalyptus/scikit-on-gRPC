![codespell](https://github.com/ucalyptus/scikit-on-gRPC/workflows/codespell/badge.svg)
![autoblack_push](https://github.com/ucalyptus/scikit-on-gRPC/workflows/autoblack_push/badge.svg)
# scikit-on-gRPC
Using Protocol Buffers and gRPC client-server communication to deploy a scikit-learn joblib exported model.

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
