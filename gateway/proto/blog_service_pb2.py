# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proto/blog_service.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'proto/blog_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18proto/blog_service.proto\"E\n\x11\x43reateBlogRequest\x12\x10\n\x08writerId\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\"F\n\x12\x43reateBlogResponse\x12\x11\n\tisSuccess\x18\x01 \x01(\x08\x12\x10\n\x08\x65rrorMsg\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\"#\n\x14GetBlogDetailRequest\x12\x0b\n\x03url\x18\x01 \x01(\t\"\xa1\x01\n\x15GetBlogDetailResponse\x12\x11\n\tisSuccess\x18\x01 \x01(\x08\x12\x10\n\x08\x65rrorMsg\x18\x02 \x01(\t\x12\x11\n\tblogTitle\x18\x03 \x01(\t\x12\x13\n\x0b\x62logContent\x18\x04 \x01(\t\x12\x15\n\rblogCreatedAt\x18\x05 \x01(\t\x12\x10\n\x08writerId\x18\x06 \x01(\x05\x12\x12\n\nwriterName\x18\x07 \x01(\t\"4\n\x12GetBlogListRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x10\n\x08pageSize\x18\x02 \x01(\x05\"<\n\x0b\x42logSummary\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x11\n\tcreatedAt\x18\x03 \x01(\t\"\xaf\x01\n\x13GetBlogListResponse\x12\x11\n\tisSuccess\x18\x01 \x01(\x08\x12\x10\n\x08\x65rrorMsg\x18\x02 \x01(\t\x12\x1b\n\x05\x62logs\x18\x03 \x03(\x0b\x32\x0c.BlogSummary\x12\x12\n\ntotalCount\x18\x04 \x01(\x05\x12\x0c\n\x04page\x18\x05 \x01(\x05\x12\x10\n\x08prevPage\x18\x06 \x01(\x05\x12\x10\n\x08nextPage\x18\x07 \x01(\x05\x12\x10\n\x08pageSize\x18\x08 \x01(\x05\x32\xbe\x01\n\x0b\x42logService\x12\x35\n\nCreateBlog\x12\x12.CreateBlogRequest\x1a\x13.CreateBlogResponse\x12>\n\rGetBlogDetail\x12\x15.GetBlogDetailRequest\x1a\x16.GetBlogDetailResponse\x12\x38\n\x0bGetBlogList\x12\x13.GetBlogListRequest\x1a\x14.GetBlogListResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, 'proto.blog_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CREATEBLOGREQUEST']._serialized_start = 28
  _globals['_CREATEBLOGREQUEST']._serialized_end = 97
  _globals['_CREATEBLOGRESPONSE']._serialized_start = 99
  _globals['_CREATEBLOGRESPONSE']._serialized_end = 169
  _globals['_GETBLOGDETAILREQUEST']._serialized_start = 171
  _globals['_GETBLOGDETAILREQUEST']._serialized_end = 206
  _globals['_GETBLOGDETAILRESPONSE']._serialized_start = 209
  _globals['_GETBLOGDETAILRESPONSE']._serialized_end = 370
  _globals['_GETBLOGLISTREQUEST']._serialized_start = 372
  _globals['_GETBLOGLISTREQUEST']._serialized_end = 424
  _globals['_BLOGSUMMARY']._serialized_start = 426
  _globals['_BLOGSUMMARY']._serialized_end = 486
  _globals['_GETBLOGLISTRESPONSE']._serialized_start = 489
  _globals['_GETBLOGLISTRESPONSE']._serialized_end = 664
  _globals['_BLOGSERVICE']._serialized_start = 667
  _globals['_BLOGSERVICE']._serialized_end = 857
# @@protoc_insertion_point(module_scope)
