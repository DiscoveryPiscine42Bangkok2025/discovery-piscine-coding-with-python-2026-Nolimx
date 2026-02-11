#!/usr/bin/env python3
import sys

params = sys.argv[1:]

if len(params) == 0:
    print("none")
else:
    displayed = False

    for p in params:

        if not p.endswith("ism"):
            print(p + "ism")
            displayed = True

    if not displayed:
        print("none")
