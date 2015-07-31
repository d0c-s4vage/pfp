#!/usr/bin/env python
# encoding: utf-8

# DEBUGGER

import binascii
import pfp
import six

data = "\x00\x00\x01\x00\x02"

template = """
	Int3();
	uchar a;
	short b;
	ushort c;
"""

dom = pfp.parse(
	data		= six.BytesIO(data),
	template	= template,
)

print(dom._pfp__show())

print(binascii.hexlify(dom._pfp__build()))
