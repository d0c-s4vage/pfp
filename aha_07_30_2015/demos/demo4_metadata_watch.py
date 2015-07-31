#!/usr/bin/env python
# encoding: utf-8

import binascii
import pfp
import six

# METADATA WATCH

data = "\x03\x00\x04\x00\x07"

template = r"""
	void Sum(ushort &watched, int other1, int other2) {
		Printf("updating %d to (%d + %d)\n", watched, other1, other2);
		watched = other1 + other2;
	}

	uchar a;
	short b;
	ushort c<watch=a;b, update=Sum>;
"""

dom = pfp.parse(
	data		= six.BytesIO(data),
	template	= template,
)

print(dom._pfp__show())

import pdb; pdb.set_trace()
dom.a = 10;
print(dom._pfp__show())

import pdb; pdb.set_trace()
dom.b = 20;
print(dom._pfp__show())

print(binascii.hexlify(dom._pfp__build()))
