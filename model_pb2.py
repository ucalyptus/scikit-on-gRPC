# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: model.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='model.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0bmodel.proto\"M\n\x08\x46\x65\x61tures\x12\x0f\n\x07reports\x18\x01 \x01(\x02\x12\x13\n\x0b\x65xpenditure\x18\x02 \x01(\x02\x12\x0b\n\x03\x61ge\x18\x03 \x01(\x02\x12\x0e\n\x06income\x18\x04 \x01(\x02\"\x1a\n\nPrediction\x12\x0c\n\x04\x63\x61rd\x18\x01 \x01(\x02\x32<\n\x07Predict\x12\x31\n\x15predict_credit_status\x12\t.Features\x1a\x0b.Prediction\"\x00\x62\x06proto3'
)




_FEATURES = _descriptor.Descriptor(
  name='Features',
  full_name='Features',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reports', full_name='Features.reports', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expenditure', full_name='Features.expenditure', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='age', full_name='Features.age', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='income', full_name='Features.income', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=92,
)


_PREDICTION = _descriptor.Descriptor(
  name='Prediction',
  full_name='Prediction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='card', full_name='Prediction.card', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=120,
)

DESCRIPTOR.message_types_by_name['Features'] = _FEATURES
DESCRIPTOR.message_types_by_name['Prediction'] = _PREDICTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Features = _reflection.GeneratedProtocolMessageType('Features', (_message.Message,), {
  'DESCRIPTOR' : _FEATURES,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:Features)
  })
_sym_db.RegisterMessage(Features)

Prediction = _reflection.GeneratedProtocolMessageType('Prediction', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTION,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:Prediction)
  })
_sym_db.RegisterMessage(Prediction)



_PREDICT = _descriptor.ServiceDescriptor(
  name='Predict',
  full_name='Predict',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=122,
  serialized_end=182,
  methods=[
  _descriptor.MethodDescriptor(
    name='predict_credit_status',
    full_name='Predict.predict_credit_status',
    index=0,
    containing_service=None,
    input_type=_FEATURES,
    output_type=_PREDICTION,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PREDICT)

DESCRIPTOR.services_by_name['Predict'] = _PREDICT

# @@protoc_insertion_point(module_scope)