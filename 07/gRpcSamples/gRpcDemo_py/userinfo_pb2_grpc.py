# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import userinfo_pb2 as userinfo__pb2


class UserInfoServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetList = channel.unary_unary(
        '/UserInfo.UserInfoService/GetList',
        request_serializer=userinfo__pb2.GetUserListRequest.SerializeToString,
        response_deserializer=userinfo__pb2.GetUserListReply.FromString,
        )
    self.GetById = channel.unary_unary(
        '/UserInfo.UserInfoService/GetById',
        request_serializer=userinfo__pb2.GetUserByIdRequest.SerializeToString,
        response_deserializer=userinfo__pb2.GetUserByIdRelpy.FromString,
        )
    self.Save = channel.unary_unary(
        '/UserInfo.UserInfoService/Save',
        request_serializer=userinfo__pb2.SaveUserRequest.SerializeToString,
        response_deserializer=userinfo__pb2.SaveUserReply.FromString,
        )


class UserInfoServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetById(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Save(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UserInfoServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetList': grpc.unary_unary_rpc_method_handler(
          servicer.GetList,
          request_deserializer=userinfo__pb2.GetUserListRequest.FromString,
          response_serializer=userinfo__pb2.GetUserListReply.SerializeToString,
      ),
      'GetById': grpc.unary_unary_rpc_method_handler(
          servicer.GetById,
          request_deserializer=userinfo__pb2.GetUserByIdRequest.FromString,
          response_serializer=userinfo__pb2.GetUserByIdRelpy.SerializeToString,
      ),
      'Save': grpc.unary_unary_rpc_method_handler(
          servicer.Save,
          request_deserializer=userinfo__pb2.SaveUserRequest.FromString,
          response_serializer=userinfo__pb2.SaveUserReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'UserInfo.UserInfoService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
