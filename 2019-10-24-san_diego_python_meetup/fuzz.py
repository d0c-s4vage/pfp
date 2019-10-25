#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pfp
import pfp.fuzz
import subprocess
import time


class IntegersOnly(pfp.fuzz.StratGroup):
    name = "ints_only"

    class IntStrat(pfp.fuzz.FieldStrat):
        klass = pfp.fields.IntBase
        choices = [0, 1, 2, 3]

    def filter_fields(self, fields):
        return filter(lambda x: isinstance(x, pfp.fields.IntBase), fields)


def open_image(png_data):
    tmp_file = "/tmp/test.png"
    with open(tmp_file, "wb") as f:
        f.write(png_data)

    proc = subprocess.Popen(["eog", tmp_file])
    time.sleep(0.5)
    proc.terminate()


dom = pfp.parse(template_file="png_watchers.bt", data_file="python.png")
for mutation in pfp.fuzz.mutate(dom, "ints_only", num=100, at_once=3):
    mutated = mutation._pfp__build()
    open_image(mutated)
