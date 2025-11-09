#!/bin/python3

import math
import os
import random
import re
import sys

def check_weird(n):
    if n % 2 != 0:  # Check if n is odd
        print("Weird")
    else:  # n is even
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")

if __name__ == '__main__':
    n = int(input().strip())
    check_weird(n)
