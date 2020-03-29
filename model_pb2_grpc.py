# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import model_pb2 as model__pb2


class PredictStub(object):
  """Define the service :
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.predict_credit_status = channel.unary_unary(
        '/Predict/predict_credit_status',
        request_serializer=model__pb2.Features.SerializeToString,
        response_deserializer=model__pb2.Prediction.FromString,
        )


class PredictServicer(object):
  """Define the service :
  """

  def predict_credit_status(self, request, context):
    # missing associated documentation comment in .proto file
#me    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PredictServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'predict_credit_status': grpc.unary_unary_rpc_method_handler(
          servicer.predict_credit_status,
          request_deserializer=model__pb2.Features.FromString,
          response_serializer=model__pb2.Prediction.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Predict', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
