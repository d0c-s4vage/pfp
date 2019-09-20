#!/usr/bin/env python
# encoding: utf-8


import unittest
import os
import sys
import utils


class TestCompat(utils.PfpTestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_adler32(self):
        dom = self._test_parse_build(
            "test\x00",
            """
                string test;
                Printf("%X", Checksum(CHECKSUM_ADLER32, 0, 1, -1, -1));
            """,
            stdout="750075",
            # Required for CHECKSUM_ADLER32 to be found
            predefines=True,
        )
