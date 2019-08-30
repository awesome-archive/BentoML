# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: repository.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import bentoml.proto.status_pb2 as status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='repository.proto',
  package='bentoml',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10repository.proto\x12\x07\x62\x65ntoml\x1a\x0cstatus.proto\"\x9c\x01\n\x08\x42\x65ntoUri\x12+\n\x04type\x18\x01 \x01(\x0e\x32\x1d.bentoml.BentoUri.StorageType\x12\x0b\n\x03uri\x18\x02 \x01(\t\"V\n\x0bStorageType\x12\t\n\x05UNSET\x10\x00\x12\t\n\x05LOCAL\x10\x01\x12\x06\n\x02S3\x10\x02\x12\x07\n\x03GCS\x10\x03\x12\x16\n\x12\x41ZURE_BLOB_STORAGE\x10\x04\x12\x08\n\x04HDFS\x10\x05\"\xd3\x03\n\rBentoMetadata\x12\x1e\n\x03uri\x18\x01 \x01(\x0b\x32\x11.bentoml.BentoUri\x12\x12\n\ncreated_at\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\x12\x33\n\x03\x65nv\x18\x05 \x01(\x0b\x32&.bentoml.BentoMetadata.BentoServiceEnv\x12\x37\n\tartifacts\x18\x06 \x03(\x0b\x32$.bentoml.BentoMetadata.BentoArtifact\x12\x34\n\x04\x61pis\x18\x07 \x03(\x0b\x32&.bentoml.BentoMetadata.BentoServiceApi\x1aP\n\x0f\x42\x65ntoServiceEnv\x12\x10\n\x08setup_sh\x18\x01 \x01(\t\x12\x11\n\tconda_env\x18\x02 \x01(\t\x12\x18\n\x10pip_dependencies\x18\x03 \x01(\t\x1a\x34\n\rBentoArtifact\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rartifact_type\x18\x02 \x01(\t\x1a\x43\n\x0f\x42\x65ntoServiceApi\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0chandler_type\x18\x02 \x01(\t\x12\x0c\n\x04\x64ocs\x18\x03 \x01(\t\"1\n\x0f\x41\x64\x64\x42\x65ntoRequest\x12\x1e\n\x03uri\x18\x01 \x01(\x0b\x32\x11.bentoml.BentoUri\"Z\n\x10\x41\x64\x64\x42\x65ntoResponse\x12\x1f\n\x06status\x18\x01 \x01(\x0b\x32\x0f.bentoml.Status\x12%\n\x05\x62\x65nto\x18\x02 \x01(\x0b\x32\x16.bentoml.BentoMetadata\"]\n\x13UploadBentoResponse\x12\x1f\n\x06status\x18\x01 \x01(\x0b\x32\x0f.bentoml.Status\x12%\n\x05\x62\x65nto\x18\x02 \x01(\x0b\x32\x16.bentoml.BentoMetadata\"J\n\x1d\x44\x61ngerouslyDeleteBentoRequest\x12\x12\n\nbento_name\x18\x01 \x01(\t\x12\x15\n\rbento_version\x18\x02 \x01(\t\"h\n\x1e\x44\x61ngerouslyDeleteBentoResponse\x12\x1f\n\x06status\x18\x01 \x01(\x0b\x32\x0f.bentoml.Status\x12%\n\x05\x62\x65nto\x18\x02 \x01(\x0b\x32\x16.bentoml.BentoMetadata\"<\n\x0fGetBentoRequest\x12\x12\n\nbento_name\x18\x01 \x01(\t\x12\x15\n\rbento_version\x18\x02 \x01(\t\"Z\n\x10GetBentoResponse\x12\x1f\n\x06status\x18\x01 \x01(\x0b\x32\x0f.bentoml.Status\x12%\n\x05\x62\x65nto\x18\x02 \x01(\x0b\x32\x16.bentoml.BentoMetadata\"E\n\x10ListBentoRequest\x12\x12\n\nbento_name\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12\r\n\x05limit\x18\x03 \x01(\x05\"\\\n\x11ListBentoResponse\x12\x1f\n\x06status\x18\x01 \x01(\x0b\x32\x0f.bentoml.Status\x12&\n\x06\x62\x65ntos\x18\x02 \x03(\x0b\x32\x16.bentoml.BentoMetadatab\x06proto3')
  ,
  dependencies=[status__pb2.DESCRIPTOR,])



_BENTOURI_STORAGETYPE = _descriptor.EnumDescriptor(
  name='StorageType',
  full_name='bentoml.BentoUri.StorageType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCAL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S3', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GCS', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AZURE_BLOB_STORAGE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HDFS', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=114,
  serialized_end=200,
)
_sym_db.RegisterEnumDescriptor(_BENTOURI_STORAGETYPE)


_BENTOURI = _descriptor.Descriptor(
  name='BentoUri',
  full_name='bentoml.BentoUri',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='bentoml.BentoUri.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uri', full_name='bentoml.BentoUri.uri', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BENTOURI_STORAGETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=200,
)


_BENTOMETADATA_BENTOSERVICEENV = _descriptor.Descriptor(
  name='BentoServiceEnv',
  full_name='bentoml.BentoMetadata.BentoServiceEnv',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='setup_sh', full_name='bentoml.BentoMetadata.BentoServiceEnv.setup_sh', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conda_env', full_name='bentoml.BentoMetadata.BentoServiceEnv.conda_env', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pip_dependencies', full_name='bentoml.BentoMetadata.BentoServiceEnv.pip_dependencies', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=467,
  serialized_end=547,
)

_BENTOMETADATA_BENTOARTIFACT = _descriptor.Descriptor(
  name='BentoArtifact',
  full_name='bentoml.BentoMetadata.BentoArtifact',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='bentoml.BentoMetadata.BentoArtifact.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='artifact_type', full_name='bentoml.BentoMetadata.BentoArtifact.artifact_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=549,
  serialized_end=601,
)

_BENTOMETADATA_BENTOSERVICEAPI = _descriptor.Descriptor(
  name='BentoServiceApi',
  full_name='bentoml.BentoMetadata.BentoServiceApi',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='bentoml.BentoMetadata.BentoServiceApi.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='handler_type', full_name='bentoml.BentoMetadata.BentoServiceApi.handler_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='docs', full_name='bentoml.BentoMetadata.BentoServiceApi.docs', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=603,
  serialized_end=670,
)

_BENTOMETADATA = _descriptor.Descriptor(
  name='BentoMetadata',
  full_name='bentoml.BentoMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uri', full_name='bentoml.BentoMetadata.uri', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='bentoml.BentoMetadata.created_at', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='bentoml.BentoMetadata.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='bentoml.BentoMetadata.version', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='env', full_name='bentoml.BentoMetadata.env', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='artifacts', full_name='bentoml.BentoMetadata.artifacts', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='apis', full_name='bentoml.BentoMetadata.apis', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BENTOMETADATA_BENTOSERVICEENV, _BENTOMETADATA_BENTOARTIFACT, _BENTOMETADATA_BENTOSERVICEAPI, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=203,
  serialized_end=670,
)


_ADDBENTOREQUEST = _descriptor.Descriptor(
  name='AddBentoRequest',
  full_name='bentoml.AddBentoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uri', full_name='bentoml.AddBentoRequest.uri', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=672,
  serialized_end=721,
)


_ADDBENTORESPONSE = _descriptor.Descriptor(
  name='AddBentoResponse',
  full_name='bentoml.AddBentoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='bentoml.AddBentoResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bento', full_name='bentoml.AddBentoResponse.bento', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=723,
  serialized_end=813,
)


_UPLOADBENTORESPONSE = _descriptor.Descriptor(
  name='UploadBentoResponse',
  full_name='bentoml.UploadBentoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='bentoml.UploadBentoResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bento', full_name='bentoml.UploadBentoResponse.bento', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=815,
  serialized_end=908,
)


_DANGEROUSLYDELETEBENTOREQUEST = _descriptor.Descriptor(
  name='DangerouslyDeleteBentoRequest',
  full_name='bentoml.DangerouslyDeleteBentoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bento_name', full_name='bentoml.DangerouslyDeleteBentoRequest.bento_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bento_version', full_name='bentoml.DangerouslyDeleteBentoRequest.bento_version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=910,
  serialized_end=984,
)


_DANGEROUSLYDELETEBENTORESPONSE = _descriptor.Descriptor(
  name='DangerouslyDeleteBentoResponse',
  full_name='bentoml.DangerouslyDeleteBentoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='bentoml.DangerouslyDeleteBentoResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bento', full_name='bentoml.DangerouslyDeleteBentoResponse.bento', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=986,
  serialized_end=1090,
)


_GETBENTOREQUEST = _descriptor.Descriptor(
  name='GetBentoRequest',
  full_name='bentoml.GetBentoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bento_name', full_name='bentoml.GetBentoRequest.bento_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bento_version', full_name='bentoml.GetBentoRequest.bento_version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=1092,
  serialized_end=1152,
)


_GETBENTORESPONSE = _descriptor.Descriptor(
  name='GetBentoResponse',
  full_name='bentoml.GetBentoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='bentoml.GetBentoResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bento', full_name='bentoml.GetBentoResponse.bento', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1154,
  serialized_end=1244,
)


_LISTBENTOREQUEST = _descriptor.Descriptor(
  name='ListBentoRequest',
  full_name='bentoml.ListBentoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bento_name', full_name='bentoml.ListBentoRequest.bento_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='bentoml.ListBentoRequest.offset', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='bentoml.ListBentoRequest.limit', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1246,
  serialized_end=1315,
)


_LISTBENTORESPONSE = _descriptor.Descriptor(
  name='ListBentoResponse',
  full_name='bentoml.ListBentoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='bentoml.ListBentoResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bentos', full_name='bentoml.ListBentoResponse.bentos', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1317,
  serialized_end=1409,
)

_BENTOURI.fields_by_name['type'].enum_type = _BENTOURI_STORAGETYPE
_BENTOURI_STORAGETYPE.containing_type = _BENTOURI
_BENTOMETADATA_BENTOSERVICEENV.containing_type = _BENTOMETADATA
_BENTOMETADATA_BENTOARTIFACT.containing_type = _BENTOMETADATA
_BENTOMETADATA_BENTOSERVICEAPI.containing_type = _BENTOMETADATA
_BENTOMETADATA.fields_by_name['uri'].message_type = _BENTOURI
_BENTOMETADATA.fields_by_name['env'].message_type = _BENTOMETADATA_BENTOSERVICEENV
_BENTOMETADATA.fields_by_name['artifacts'].message_type = _BENTOMETADATA_BENTOARTIFACT
_BENTOMETADATA.fields_by_name['apis'].message_type = _BENTOMETADATA_BENTOSERVICEAPI
_ADDBENTOREQUEST.fields_by_name['uri'].message_type = _BENTOURI
_ADDBENTORESPONSE.fields_by_name['status'].message_type = status__pb2._STATUS
_ADDBENTORESPONSE.fields_by_name['bento'].message_type = _BENTOMETADATA
_UPLOADBENTORESPONSE.fields_by_name['status'].message_type = status__pb2._STATUS
_UPLOADBENTORESPONSE.fields_by_name['bento'].message_type = _BENTOMETADATA
_DANGEROUSLYDELETEBENTORESPONSE.fields_by_name['status'].message_type = status__pb2._STATUS
_DANGEROUSLYDELETEBENTORESPONSE.fields_by_name['bento'].message_type = _BENTOMETADATA
_GETBENTORESPONSE.fields_by_name['status'].message_type = status__pb2._STATUS
_GETBENTORESPONSE.fields_by_name['bento'].message_type = _BENTOMETADATA
_LISTBENTORESPONSE.fields_by_name['status'].message_type = status__pb2._STATUS
_LISTBENTORESPONSE.fields_by_name['bentos'].message_type = _BENTOMETADATA
DESCRIPTOR.message_types_by_name['BentoUri'] = _BENTOURI
DESCRIPTOR.message_types_by_name['BentoMetadata'] = _BENTOMETADATA
DESCRIPTOR.message_types_by_name['AddBentoRequest'] = _ADDBENTOREQUEST
DESCRIPTOR.message_types_by_name['AddBentoResponse'] = _ADDBENTORESPONSE
DESCRIPTOR.message_types_by_name['UploadBentoResponse'] = _UPLOADBENTORESPONSE
DESCRIPTOR.message_types_by_name['DangerouslyDeleteBentoRequest'] = _DANGEROUSLYDELETEBENTOREQUEST
DESCRIPTOR.message_types_by_name['DangerouslyDeleteBentoResponse'] = _DANGEROUSLYDELETEBENTORESPONSE
DESCRIPTOR.message_types_by_name['GetBentoRequest'] = _GETBENTOREQUEST
DESCRIPTOR.message_types_by_name['GetBentoResponse'] = _GETBENTORESPONSE
DESCRIPTOR.message_types_by_name['ListBentoRequest'] = _LISTBENTOREQUEST
DESCRIPTOR.message_types_by_name['ListBentoResponse'] = _LISTBENTORESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BentoUri = _reflection.GeneratedProtocolMessageType('BentoUri', (_message.Message,), {
  'DESCRIPTOR' : _BENTOURI,
  '__module__' : 'repository_pb2'
  # @@protoc_insertion_point(class_scope:bentoml.BentoUri)
  })
_sym_db.RegisterMessage(BentoUri)

BentoMetadata = _reflection.GeneratedProtocolMessageType('BentoMetadata', (_message.Message,), {

  'BentoServiceEnv' : _reflection.GeneratedProtocolMessageType('BentoServiceEnv', (_message.Message,), {
    'DESCRIPTOR' : _BENTOMETADATA_BENTOSERVICEENV,
    '__module__' : 'repository_pb2'
    # @@protoc_insertion_point(class_scope:bentoml.BentoMetadata.BentoServiceEnv)
    })
  ,

  'BentoArtifact' : _reflection.GeneratedProtocolMessageType('BentoArtifact', (_message.Message,), {
    'DESCRIPTOR' : _BENTOMETADATA_BENTOARTIFACT,
    '__module__' : 'repository_pb2'
    # @@protoc_insertion_point(class_scope:bentoml.BentoMetadata.BentoArtifact)
    })
  ,

  'BentoServiceApi' : _reflection.GeneratedProtocolMessageType('BentoServiceApi', (_message.Message,), {
    'DESCRIPTOR' : _BENTOMETADATA_BENTOSERVICEAPI,
    '__module__' : 'repository_pb2'
    # @@protoc_insertion_point(class_scope:bentoml.BentoMetadata.BentoServiceApi)
    })
  ,
  'DESCRIPTOR' : _BENTOMETADATA,
  '__module__' : 'repository_pb2'
  # @@protoc_insertion_point(class_scope:bentoml.BentoMetadata)
  })
_sym_db.RegisterMessage(BentoMetadata)
_sym_db.RegisterMessage(BentoMetadata.BentoServiceEnv)
_sym_db.RegisterMessage(BentoMetadata.BentoArtifact)
_sym_db.RegisterMessage(BentoMetadata.BentoServiceApi)

AddBentoRequest = _reflection.GeneratedProtocolMessageType('AddBentoRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDBENTOREQUEST,
  '__module__' : 'repository_pb2'
  # @@protoc_insertion_point(class_scope:bentoml.AddBentoRequest)
  })
_sym_db.RegisterMessage(AddBentoRequest)

AddBentoResponse = _reflection.GeneratedProtocolMessageType('AddBentoResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDBENTORESPONSE,
  '__module__' : 'repository_pb2'
  # @@protoc_insertion_point(class_scope:bentoml.AddBentoResponse)
  })
_sym_db.RegisterMessage(AddBentoResponse)

UploadBentoResponse = _reflection.GeneratedProtocolMessageType('UploadBentoResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADBENTORESPONSE,
  '__module__' : 'repository_pb2'
  # @@protoc_insertion_point(class_scope:bentoml.UploadBentoResponse)
  })
_sym_db.RegisterMessage(UploadBentoResponse)

DangerouslyDeleteBentoRequest = _reflection.GeneratedProtocolMessageType('DangerouslyDeleteBentoRequest', (_message.Message,), {
  'DESCRIPTOR' : _DANGEROUSLYDELETEBENTOREQUEST,
  '__module__' : 'repository_pb2'
  # @@protoc_insertion_point(class_scope:bentoml.DangerouslyDeleteBentoRequest)
  })
_sym_db.RegisterMessage(DangerouslyDeleteBentoRequest)

DangerouslyDeleteBentoResponse = _reflection.GeneratedProtocolMessageType('DangerouslyDeleteBentoResponse', (_message.Message,), {
  'DESCRIPTOR' : _DANGEROUSLYDELETEBENTORESPONSE,
  '__module__' : 'repository_pb2'
  # @@protoc_insertion_point(class_scope:bentoml.DangerouslyDeleteBentoResponse)
  })
_sym_db.RegisterMessage(DangerouslyDeleteBentoResponse)

GetBentoRequest = _reflection.GeneratedProtocolMessageType('GetBentoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBENTOREQUEST,
  '__module__' : 'repository_pb2'
  # @@protoc_insertion_point(class_scope:bentoml.GetBentoRequest)
  })
_sym_db.RegisterMessage(GetBentoRequest)

GetBentoResponse = _reflection.GeneratedProtocolMessageType('GetBentoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETBENTORESPONSE,
  '__module__' : 'repository_pb2'
  # @@protoc_insertion_point(class_scope:bentoml.GetBentoResponse)
  })
_sym_db.RegisterMessage(GetBentoResponse)

ListBentoRequest = _reflection.GeneratedProtocolMessageType('ListBentoRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTBENTOREQUEST,
  '__module__' : 'repository_pb2'
  # @@protoc_insertion_point(class_scope:bentoml.ListBentoRequest)
  })
_sym_db.RegisterMessage(ListBentoRequest)

ListBentoResponse = _reflection.GeneratedProtocolMessageType('ListBentoResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTBENTORESPONSE,
  '__module__' : 'repository_pb2'
  # @@protoc_insertion_point(class_scope:bentoml.ListBentoResponse)
  })
_sym_db.RegisterMessage(ListBentoResponse)


# @@protoc_insertion_point(module_scope)
