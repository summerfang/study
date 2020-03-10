import re

def is_http_or_https_URL(sURL):
    if not isinstance(sURL, str):
        return None

    if re.match('^http(s?)://', sURL.strip()):
        return True
    else:
        return False

print(is_http_or_https_URL('https://www.sina.com.cn'))
print(is_http_or_https_URL('https://www.sina.com.cn'))
