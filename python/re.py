import re

# Nautural number
result = re.match('^(-\d+|(0+))$', '0100')
if result is not None:
    print(result.group())
