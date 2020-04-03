# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import lights_pb2 as lights__pb2


class LightServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.powerOn = channel.unary_unary(
        '/LightService/powerOn',
        request_serializer=lights__pb2.PowerRequest.SerializeToString,
        response_deserializer=lights__pb2.PowerResponse.FromString,
        )
    self.changeColour = channel.unary_unary(
        '/LightService/changeColour',
        request_serializer=lights__pb2.ColourRequest.SerializeToString,
        response_deserializer=lights__pb2.ColourResponse.FromString,
        )


class LightServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def powerOn(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def changeColour(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_LightServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'powerOn': grpc.unary_unary_rpc_method_handler(
          servicer.powerOn,
          request_deserializer=lights__pb2.PowerRequest.FromString,
          response_serializer=lights__pb2.PowerResponse.SerializeToString,
      ),
      'changeColour': grpc.unary_unary_rpc_method_handler(
          servicer.changeColour,
          request_deserializer=lights__pb2.ColourRequest.FromString,
          response_serializer=lights__pb2.ColourResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'LightService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))