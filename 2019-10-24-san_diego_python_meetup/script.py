#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import os
import pfp
 

template = """
BigEndian();
 
typedef struct {
    uint32 length;
    char type[4];
    char data[length];
    uint32 crc;
} PngChunk;
 
struct {
    uchar signature[8];
 
    while (!FEof()) {
        PngChunk chunks;
    }
} PNG;
"""
 
dom = pfp.parse(data_file="python.png", template=template)
print(dom._pfp__show())
