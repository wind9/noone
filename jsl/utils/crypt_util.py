import hashlib


def md5(text):
    h = hashlib.md5()
    h.update(text)
    return h.hexdigest()
