#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2018/12/14 16:28
@filename:Is_stressful

"""

import re
def is_stressful(stringd):
    print(re.findall('hElp', stringd, flags=re.IGNORECASE))

is_stressful("I neeed HELP")