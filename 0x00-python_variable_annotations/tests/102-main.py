#!/usr/bin/env python3
import sys

sys.path.append('../')

zoom_array =  __import__('102-type_checking').zoom_array

print(zoom_array.__annotations__)
