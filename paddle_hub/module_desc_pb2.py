# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: module_desc.proto

import sys
_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='module_desc.proto',
    package='paddle_hub',
    syntax='proto3',
    serialized_pb=_b(
        '\n\x11module_desc.proto\x12\npaddle_hub\"\xcc\x02\n\x0c\x46lexibleData\x12\"\n\x04type\x18\x01 \x01(\x0e\x32\x14.paddle_hub.DataType\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\t\n\x01i\x18\x03 \x01(\x05\x12\t\n\x01\x66\x18\x04 \x01(\x02\x12\t\n\x01\x62\x18\x05 \x01(\x08\x12\t\n\x01s\x18\x06 \x01(\t\x12*\n\x01m\x18\x07 \x03(\x0b\x32\x1f.paddle_hub.FlexibleData.MEntry\x12*\n\x01l\x18\x08 \x03(\x0b\x32\x1f.paddle_hub.FlexibleData.LEntry\x1a\x42\n\x06MEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.paddle_hub.FlexibleData:\x02\x38\x01\x1a\x42\n\x06LEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.paddle_hub.FlexibleData:\x02\x38\x01\"+\n\x08\x46\x65\x65\x64\x44\x65sc\x12\x10\n\x08var_name\x18\x01 \x01(\t\x12\r\n\x05\x61lias\x18\x02 \x01(\t\",\n\tFetchDesc\x12\x10\n\x08var_name\x18\x01 \x01(\t\x12\r\n\x05\x61lias\x18\x02 \x01(\t\"_\n\tModuleVar\x12)\n\nfetch_desc\x18\x01 \x03(\x0b\x32\x15.paddle_hub.FetchDesc\x12\'\n\tfeed_desc\x18\x02 \x03(\x0b\x32\x14.paddle_hub.FeedDesc\"7\n\x08\x41uthInfo\x12\x16\n\x0epaddle_version\x18\x01 \x01(\t\x12\x13\n\x0bhub_version\x18\x02 \x01(\t\"\x83\x03\n\tParamAttr\x12\x36\n\x0bregularizer\x18\x01 \x01(\x0b\x32!.paddle_hub.ParamAttr.Regularizer\x12\x42\n\x12gradient_clip_attr\x18\x02 \x01(\x0b\x32&.paddle_hub.ParamAttr.GradientClipAttr\x12/\n\roptimize_attr\x18\x03 \x01(\x0b\x32\x18.paddle_hub.FlexibleData\x12\x11\n\ttrainable\x18\x04 \x01(\x08\x12\x18\n\x10\x64o_model_average\x18\x05 \x01(\x08\x1a\x39\n\x0bRegularizer\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x1c\n\x14regularization_coeff\x18\x02 \x01(\x02\x1a\x61\n\x10GradientClipAttr\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0b\n\x03min\x18\x02 \x01(\x02\x12\x0b\n\x03max\x18\x03 \x01(\x02\x12\x11\n\tclip_norm\x18\x04 \x01(\x02\x12\x12\n\ngroup_name\x18\x05 \x01(\t\"\xf8\x02\n\nModuleDesc\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x36\n\x08sign2var\x18\x02 \x03(\x0b\x32$.paddle_hub.ModuleDesc.Sign2varEntry\x12\x14\n\x0creturn_numpy\x18\x03 \x01(\x08\x12\x16\n\x0e\x63ontain_assets\x18\x04 \x01(\x08\x12\'\n\tauth_info\x18\x05 \x01(\x0b\x32\x14.paddle_hub.AuthInfo\x12;\n\x0bparam_attrs\x18\x06 \x03(\x0b\x32&.paddle_hub.ModuleDesc.ParamAttrsEntry\x1a\x46\n\rSign2varEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.paddle_hub.ModuleVar:\x02\x38\x01\x1aH\n\x0fParamAttrsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.paddle_hub.ParamAttr:\x02\x38\x01*J\n\x08\x44\x61taType\x12\x07\n\x03INT\x10\x00\x12\t\n\x05\x46LOAT\x10\x01\x12\n\n\x06STRING\x10\x02\x12\x0b\n\x07\x42OOLEAN\x10\x03\x12\x08\n\x04LIST\x10\x04\x12\x07\n\x03MAP\x10\x05\x42\x02H\x03\x62\x06proto3'
    ))
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_DATATYPE = _descriptor.EnumDescriptor(
    name='DataType',
    full_name='paddle_hub.DataType',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='INT', index=0, number=0, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='FLOAT', index=1, number=1, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='STRING', index=2, number=2, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='BOOLEAN', index=3, number=3, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='LIST', index=4, number=4, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='MAP', index=5, number=5, options=None, type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=1382,
    serialized_end=1456,
)
_sym_db.RegisterEnumDescriptor(_DATATYPE)

DataType = enum_type_wrapper.EnumTypeWrapper(_DATATYPE)
INT = 0
FLOAT = 1
STRING = 2
BOOLEAN = 3
LIST = 4
MAP = 5

_FLEXIBLEDATA_MENTRY = _descriptor.Descriptor(
    name='MEntry',
    full_name='paddle_hub.FlexibleData.MEntry',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='key',
            full_name='paddle_hub.FlexibleData.MEntry.key',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='value',
            full_name='paddle_hub.FlexibleData.MEntry.value',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(),
                                      _b('8\001')),
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=232,
    serialized_end=298,
)

_FLEXIBLEDATA_LENTRY = _descriptor.Descriptor(
    name='LEntry',
    full_name='paddle_hub.FlexibleData.LEntry',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='key',
            full_name='paddle_hub.FlexibleData.LEntry.key',
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='value',
            full_name='paddle_hub.FlexibleData.LEntry.value',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(),
                                      _b('8\001')),
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=300,
    serialized_end=366,
)

_FLEXIBLEDATA = _descriptor.Descriptor(
    name='FlexibleData',
    full_name='paddle_hub.FlexibleData',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='type',
            full_name='paddle_hub.FlexibleData.type',
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='name',
            full_name='paddle_hub.FlexibleData.name',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='i',
            full_name='paddle_hub.FlexibleData.i',
            index=2,
            number=3,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='f',
            full_name='paddle_hub.FlexibleData.f',
            index=3,
            number=4,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='b',
            full_name='paddle_hub.FlexibleData.b',
            index=4,
            number=5,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='s',
            full_name='paddle_hub.FlexibleData.s',
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='m',
            full_name='paddle_hub.FlexibleData.m',
            index=6,
            number=7,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='l',
            full_name='paddle_hub.FlexibleData.l',
            index=7,
            number=8,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
    ],
    extensions=[],
    nested_types=[
        _FLEXIBLEDATA_MENTRY,
        _FLEXIBLEDATA_LENTRY,
    ],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=34,
    serialized_end=366,
)

_FEEDDESC = _descriptor.Descriptor(
    name='FeedDesc',
    full_name='paddle_hub.FeedDesc',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='var_name',
            full_name='paddle_hub.FeedDesc.var_name',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='alias',
            full_name='paddle_hub.FeedDesc.alias',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=368,
    serialized_end=411,
)

_FETCHDESC = _descriptor.Descriptor(
    name='FetchDesc',
    full_name='paddle_hub.FetchDesc',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='var_name',
            full_name='paddle_hub.FetchDesc.var_name',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='alias',
            full_name='paddle_hub.FetchDesc.alias',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=413,
    serialized_end=457,
)

_MODULEVAR = _descriptor.Descriptor(
    name='ModuleVar',
    full_name='paddle_hub.ModuleVar',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='fetch_desc',
            full_name='paddle_hub.ModuleVar.fetch_desc',
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='feed_desc',
            full_name='paddle_hub.ModuleVar.feed_desc',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=459,
    serialized_end=554,
)

_AUTHINFO = _descriptor.Descriptor(
    name='AuthInfo',
    full_name='paddle_hub.AuthInfo',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='paddle_version',
            full_name='paddle_hub.AuthInfo.paddle_version',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='hub_version',
            full_name='paddle_hub.AuthInfo.hub_version',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=556,
    serialized_end=611,
)

_PARAMATTR_REGULARIZER = _descriptor.Descriptor(
    name='Regularizer',
    full_name='paddle_hub.ParamAttr.Regularizer',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='type',
            full_name='paddle_hub.ParamAttr.Regularizer.type',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='regularization_coeff',
            full_name='paddle_hub.ParamAttr.Regularizer.regularization_coeff',
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=845,
    serialized_end=902,
)

_PARAMATTR_GRADIENTCLIPATTR = _descriptor.Descriptor(
    name='GradientClipAttr',
    full_name='paddle_hub.ParamAttr.GradientClipAttr',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='type',
            full_name='paddle_hub.ParamAttr.GradientClipAttr.type',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='min',
            full_name='paddle_hub.ParamAttr.GradientClipAttr.min',
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='max',
            full_name='paddle_hub.ParamAttr.GradientClipAttr.max',
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='clip_norm',
            full_name='paddle_hub.ParamAttr.GradientClipAttr.clip_norm',
            index=3,
            number=4,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='group_name',
            full_name='paddle_hub.ParamAttr.GradientClipAttr.group_name',
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=904,
    serialized_end=1001,
)

_PARAMATTR = _descriptor.Descriptor(
    name='ParamAttr',
    full_name='paddle_hub.ParamAttr',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='regularizer',
            full_name='paddle_hub.ParamAttr.regularizer',
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='gradient_clip_attr',
            full_name='paddle_hub.ParamAttr.gradient_clip_attr',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='optimize_attr',
            full_name='paddle_hub.ParamAttr.optimize_attr',
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='trainable',
            full_name='paddle_hub.ParamAttr.trainable',
            index=3,
            number=4,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='do_model_average',
            full_name='paddle_hub.ParamAttr.do_model_average',
            index=4,
            number=5,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
    ],
    extensions=[],
    nested_types=[
        _PARAMATTR_REGULARIZER,
        _PARAMATTR_GRADIENTCLIPATTR,
    ],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=614,
    serialized_end=1001,
)

_MODULEDESC_SIGN2VARENTRY = _descriptor.Descriptor(
    name='Sign2varEntry',
    full_name='paddle_hub.ModuleDesc.Sign2varEntry',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='key',
            full_name='paddle_hub.ModuleDesc.Sign2varEntry.key',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='value',
            full_name='paddle_hub.ModuleDesc.Sign2varEntry.value',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(),
                                      _b('8\001')),
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=1236,
    serialized_end=1306,
)

_MODULEDESC_PARAMATTRSENTRY = _descriptor.Descriptor(
    name='ParamAttrsEntry',
    full_name='paddle_hub.ModuleDesc.ParamAttrsEntry',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='key',
            full_name='paddle_hub.ModuleDesc.ParamAttrsEntry.key',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='value',
            full_name='paddle_hub.ModuleDesc.ParamAttrsEntry.value',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(),
                                      _b('8\001')),
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=1308,
    serialized_end=1380,
)

_MODULEDESC = _descriptor.Descriptor(
    name='ModuleDesc',
    full_name='paddle_hub.ModuleDesc',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='name',
            full_name='paddle_hub.ModuleDesc.name',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='sign2var',
            full_name='paddle_hub.ModuleDesc.sign2var',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='return_numpy',
            full_name='paddle_hub.ModuleDesc.return_numpy',
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='contain_assets',
            full_name='paddle_hub.ModuleDesc.contain_assets',
            index=3,
            number=4,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='auth_info',
            full_name='paddle_hub.ModuleDesc.auth_info',
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='param_attrs',
            full_name='paddle_hub.ModuleDesc.param_attrs',
            index=5,
            number=6,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
    ],
    extensions=[],
    nested_types=[
        _MODULEDESC_SIGN2VARENTRY,
        _MODULEDESC_PARAMATTRSENTRY,
    ],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=1004,
    serialized_end=1380,
)

_FLEXIBLEDATA_MENTRY.fields_by_name['value'].message_type = _FLEXIBLEDATA
_FLEXIBLEDATA_MENTRY.containing_type = _FLEXIBLEDATA
_FLEXIBLEDATA_LENTRY.fields_by_name['value'].message_type = _FLEXIBLEDATA
_FLEXIBLEDATA_LENTRY.containing_type = _FLEXIBLEDATA
_FLEXIBLEDATA.fields_by_name['type'].enum_type = _DATATYPE
_FLEXIBLEDATA.fields_by_name['m'].message_type = _FLEXIBLEDATA_MENTRY
_FLEXIBLEDATA.fields_by_name['l'].message_type = _FLEXIBLEDATA_LENTRY
_MODULEVAR.fields_by_name['fetch_desc'].message_type = _FETCHDESC
_MODULEVAR.fields_by_name['feed_desc'].message_type = _FEEDDESC
_PARAMATTR_REGULARIZER.containing_type = _PARAMATTR
_PARAMATTR_GRADIENTCLIPATTR.containing_type = _PARAMATTR
_PARAMATTR.fields_by_name['regularizer'].message_type = _PARAMATTR_REGULARIZER
_PARAMATTR.fields_by_name[
    'gradient_clip_attr'].message_type = _PARAMATTR_GRADIENTCLIPATTR
_PARAMATTR.fields_by_name['optimize_attr'].message_type = _FLEXIBLEDATA
_MODULEDESC_SIGN2VARENTRY.fields_by_name['value'].message_type = _MODULEVAR
_MODULEDESC_SIGN2VARENTRY.containing_type = _MODULEDESC
_MODULEDESC_PARAMATTRSENTRY.fields_by_name['value'].message_type = _PARAMATTR
_MODULEDESC_PARAMATTRSENTRY.containing_type = _MODULEDESC
_MODULEDESC.fields_by_name['sign2var'].message_type = _MODULEDESC_SIGN2VARENTRY
_MODULEDESC.fields_by_name['auth_info'].message_type = _AUTHINFO
_MODULEDESC.fields_by_name[
    'param_attrs'].message_type = _MODULEDESC_PARAMATTRSENTRY
DESCRIPTOR.message_types_by_name['FlexibleData'] = _FLEXIBLEDATA
DESCRIPTOR.message_types_by_name['FeedDesc'] = _FEEDDESC
DESCRIPTOR.message_types_by_name['FetchDesc'] = _FETCHDESC
DESCRIPTOR.message_types_by_name['ModuleVar'] = _MODULEVAR
DESCRIPTOR.message_types_by_name['AuthInfo'] = _AUTHINFO
DESCRIPTOR.message_types_by_name['ParamAttr'] = _PARAMATTR
DESCRIPTOR.message_types_by_name['ModuleDesc'] = _MODULEDESC
DESCRIPTOR.enum_types_by_name['DataType'] = _DATATYPE

FlexibleData = _reflection.GeneratedProtocolMessageType(
    'FlexibleData',
    (_message.Message, ),
    dict(
        MEntry=_reflection.GeneratedProtocolMessageType(
            'MEntry',
            (_message.Message, ),
            dict(
                DESCRIPTOR=_FLEXIBLEDATA_MENTRY,
                __module__='module_desc_pb2'
                # @@protoc_insertion_point(class_scope:paddle_hub.FlexibleData.MEntry)
            )),
        LEntry=_reflection.GeneratedProtocolMessageType(
            'LEntry',
            (_message.Message, ),
            dict(
                DESCRIPTOR=_FLEXIBLEDATA_LENTRY,
                __module__='module_desc_pb2'
                # @@protoc_insertion_point(class_scope:paddle_hub.FlexibleData.LEntry)
            )),
        DESCRIPTOR=_FLEXIBLEDATA,
        __module__='module_desc_pb2'
        # @@protoc_insertion_point(class_scope:paddle_hub.FlexibleData)
    ))
_sym_db.RegisterMessage(FlexibleData)
_sym_db.RegisterMessage(FlexibleData.MEntry)
_sym_db.RegisterMessage(FlexibleData.LEntry)

FeedDesc = _reflection.GeneratedProtocolMessageType(
    'FeedDesc',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_FEEDDESC,
        __module__='module_desc_pb2'
        # @@protoc_insertion_point(class_scope:paddle_hub.FeedDesc)
    ))
_sym_db.RegisterMessage(FeedDesc)

FetchDesc = _reflection.GeneratedProtocolMessageType(
    'FetchDesc',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_FETCHDESC,
        __module__='module_desc_pb2'
        # @@protoc_insertion_point(class_scope:paddle_hub.FetchDesc)
    ))
_sym_db.RegisterMessage(FetchDesc)

ModuleVar = _reflection.GeneratedProtocolMessageType(
    'ModuleVar',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_MODULEVAR,
        __module__='module_desc_pb2'
        # @@protoc_insertion_point(class_scope:paddle_hub.ModuleVar)
    ))
_sym_db.RegisterMessage(ModuleVar)

AuthInfo = _reflection.GeneratedProtocolMessageType(
    'AuthInfo',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_AUTHINFO,
        __module__='module_desc_pb2'
        # @@protoc_insertion_point(class_scope:paddle_hub.AuthInfo)
    ))
_sym_db.RegisterMessage(AuthInfo)

ParamAttr = _reflection.GeneratedProtocolMessageType(
    'ParamAttr',
    (_message.Message, ),
    dict(
        Regularizer=_reflection.GeneratedProtocolMessageType(
            'Regularizer',
            (_message.Message, ),
            dict(
                DESCRIPTOR=_PARAMATTR_REGULARIZER,
                __module__='module_desc_pb2'
                # @@protoc_insertion_point(class_scope:paddle_hub.ParamAttr.Regularizer)
            )),
        GradientClipAttr=_reflection.GeneratedProtocolMessageType(
            'GradientClipAttr',
            (_message.Message, ),
            dict(
                DESCRIPTOR=_PARAMATTR_GRADIENTCLIPATTR,
                __module__='module_desc_pb2'
                # @@protoc_insertion_point(class_scope:paddle_hub.ParamAttr.GradientClipAttr)
            )),
        DESCRIPTOR=_PARAMATTR,
        __module__='module_desc_pb2'
        # @@protoc_insertion_point(class_scope:paddle_hub.ParamAttr)
    ))
_sym_db.RegisterMessage(ParamAttr)
_sym_db.RegisterMessage(ParamAttr.Regularizer)
_sym_db.RegisterMessage(ParamAttr.GradientClipAttr)

ModuleDesc = _reflection.GeneratedProtocolMessageType(
    'ModuleDesc',
    (_message.Message, ),
    dict(
        Sign2varEntry=_reflection.GeneratedProtocolMessageType(
            'Sign2varEntry',
            (_message.Message, ),
            dict(
                DESCRIPTOR=_MODULEDESC_SIGN2VARENTRY,
                __module__='module_desc_pb2'
                # @@protoc_insertion_point(class_scope:paddle_hub.ModuleDesc.Sign2varEntry)
            )),
        ParamAttrsEntry=_reflection.GeneratedProtocolMessageType(
            'ParamAttrsEntry',
            (_message.Message, ),
            dict(
                DESCRIPTOR=_MODULEDESC_PARAMATTRSENTRY,
                __module__='module_desc_pb2'
                # @@protoc_insertion_point(class_scope:paddle_hub.ModuleDesc.ParamAttrsEntry)
            )),
        DESCRIPTOR=_MODULEDESC,
        __module__='module_desc_pb2'
        # @@protoc_insertion_point(class_scope:paddle_hub.ModuleDesc)
    ))
_sym_db.RegisterMessage(ModuleDesc)
_sym_db.RegisterMessage(ModuleDesc.Sign2varEntry)
_sym_db.RegisterMessage(ModuleDesc.ParamAttrsEntry)

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(),
                                                _b('H\003'))
_FLEXIBLEDATA_MENTRY.has_options = True
_FLEXIBLEDATA_MENTRY._options = _descriptor._ParseOptions(
    descriptor_pb2.MessageOptions(), _b('8\001'))
_FLEXIBLEDATA_LENTRY.has_options = True
_FLEXIBLEDATA_LENTRY._options = _descriptor._ParseOptions(
    descriptor_pb2.MessageOptions(), _b('8\001'))
_MODULEDESC_SIGN2VARENTRY.has_options = True
_MODULEDESC_SIGN2VARENTRY._options = _descriptor._ParseOptions(
    descriptor_pb2.MessageOptions(), _b('8\001'))
_MODULEDESC_PARAMATTRSENTRY.has_options = True
_MODULEDESC_PARAMATTRSENTRY._options = _descriptor._ParseOptions(
    descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
