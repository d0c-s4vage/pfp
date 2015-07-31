#!/usr/bin/env python
# encoding: utf-8

import binascii
import pfp
import six
import struct
import zlib

# METADATA PACKED

packed_data = zlib.compress("\x01\x02\x03")
data = struct.pack("<b", len(packed_data)) + packed_data

template = r"""
	typedef struct {
		uchar a;
		uchar b;
		uchar c;
	} PACKED_TYPE;

	struct {
		uchar length<watch=data, update=WatchLength>;
		uchar data[length]<packer=GZipper, packtype=PACKED_TYPE>;
	} main;
"""

dom = pfp.parse(
	data		= six.BytesIO(data),
	template	= template,
)

print(dom._pfp__show())

dom.main.data._.a = 10;
dom.main.data._.b = 11;
dom.main.data._.b = 12;

print(dom._pfp__show())

print(binascii.hexlify(dom._pfp__build()))
print(repr(dom._pfp__build()))
