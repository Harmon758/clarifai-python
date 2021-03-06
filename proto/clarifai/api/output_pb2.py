# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/clarifai/api/output.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.clarifai.api import common_pb2 as proto_dot_clarifai_dot_api_dot_common__pb2
from proto.clarifai.api import data_pb2 as proto_dot_clarifai_dot_api_dot_data__pb2
from proto.clarifai.api import input_pb2 as proto_dot_clarifai_dot_api_dot_input__pb2
from proto.clarifai.api import model_pb2 as proto_dot_clarifai_dot_api_dot_model__pb2
from proto.clarifai.api.status import status_pb2 as proto_dot_clarifai_dot_api_dot_status_dot_status__pb2
from proto.clarifai.api.utils import extensions_pb2 as proto_dot_clarifai_dot_api_dot_utils_dot_extensions__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/clarifai/api/output.proto',
  package='clarifai.api',
  syntax='proto3',
  serialized_pb=_b('\n\x1fproto/clarifai/api/output.proto\x12\x0c\x63larifai.api\x1a\x1fproto/clarifai/api/common.proto\x1a\x1dproto/clarifai/api/data.proto\x1a\x1eproto/clarifai/api/input.proto\x1a\x1eproto/clarifai/api/model.proto\x1a&proto/clarifai/api/status/status.proto\x1a)proto/clarifai/api/utils/extensions.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xdb\x01\n\x06Output\x12\n\n\x02id\x18\x01 \x01(\t\x12+\n\x06status\x18\x02 \x01(\x0b\x32\x1b.clarifai.api.status.Status\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\"\n\x05model\x18\x04 \x01(\x0b\x32\x13.clarifai.api.Model\x12\"\n\x05input\x18\x05 \x01(\x0b\x32\x13.clarifai.api.Input\x12 \n\x04\x64\x61ta\x18\x06 \x01(\x0b\x32\x12.clarifai.api.Data\"o\n\x13MultiOutputResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.clarifai.api.status.Status\x12+\n\x07outputs\x18\x02 \x03(\x0b\x32\x14.clarifai.api.OutputB\x04\x80\xb5\x18\x01\x42$Z\x03\x61pi\xa2\x02\x04\x43\x41IP\xc2\x02\x01_\xca\x02\x11\x43larifai\\Internalb\x06proto3')
  ,
  dependencies=[proto_dot_clarifai_dot_api_dot_common__pb2.DESCRIPTOR,proto_dot_clarifai_dot_api_dot_data__pb2.DESCRIPTOR,proto_dot_clarifai_dot_api_dot_input__pb2.DESCRIPTOR,proto_dot_clarifai_dot_api_dot_model__pb2.DESCRIPTOR,proto_dot_clarifai_dot_api_dot_status_dot_status__pb2.DESCRIPTOR,proto_dot_clarifai_dot_api_dot_utils_dot_extensions__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_OUTPUT = _descriptor.Descriptor(
  name='Output',
  full_name='clarifai.api.Output',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='clarifai.api.Output.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='clarifai.api.Output.status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='clarifai.api.Output.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model', full_name='clarifai.api.Output.model', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input', full_name='clarifai.api.Output.input', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='clarifai.api.Output.data', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=294,
  serialized_end=513,
)


_MULTIOUTPUTRESPONSE = _descriptor.Descriptor(
  name='MultiOutputResponse',
  full_name='clarifai.api.MultiOutputResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='clarifai.api.MultiOutputResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='clarifai.api.MultiOutputResponse.outputs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200\265\030\001')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=515,
  serialized_end=626,
)

_OUTPUT.fields_by_name['status'].message_type = proto_dot_clarifai_dot_api_dot_status_dot_status__pb2._STATUS
_OUTPUT.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_OUTPUT.fields_by_name['model'].message_type = proto_dot_clarifai_dot_api_dot_model__pb2._MODEL
_OUTPUT.fields_by_name['input'].message_type = proto_dot_clarifai_dot_api_dot_input__pb2._INPUT
_OUTPUT.fields_by_name['data'].message_type = proto_dot_clarifai_dot_api_dot_data__pb2._DATA
_MULTIOUTPUTRESPONSE.fields_by_name['status'].message_type = proto_dot_clarifai_dot_api_dot_status_dot_status__pb2._STATUS
_MULTIOUTPUTRESPONSE.fields_by_name['outputs'].message_type = _OUTPUT
DESCRIPTOR.message_types_by_name['Output'] = _OUTPUT
DESCRIPTOR.message_types_by_name['MultiOutputResponse'] = _MULTIOUTPUTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Output = _reflection.GeneratedProtocolMessageType('Output', (_message.Message,), dict(
  DESCRIPTOR = _OUTPUT,
  __module__ = 'proto.clarifai.api.output_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.Output)
  ))
_sym_db.RegisterMessage(Output)

MultiOutputResponse = _reflection.GeneratedProtocolMessageType('MultiOutputResponse', (_message.Message,), dict(
  DESCRIPTOR = _MULTIOUTPUTRESPONSE,
  __module__ = 'proto.clarifai.api.output_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.MultiOutputResponse)
  ))
_sym_db.RegisterMessage(MultiOutputResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\003api\242\002\004CAIP\302\002\001_\312\002\021Clarifai\\Internal'))
_MULTIOUTPUTRESPONSE.fields_by_name['outputs'].has_options = True
_MULTIOUTPUTRESPONSE.fields_by_name['outputs']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200\265\030\001'))
# @@protoc_insertion_point(module_scope)
