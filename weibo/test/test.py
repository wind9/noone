from datetime import datetime
import logging
import logging.handlers
import re

pattern = r'(\d)\1'
test_str = '1111344688'

a = re.findall(pattern, test_str)
print(a)
print(a.groups())

