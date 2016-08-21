# -*- coding: utf-8 -*-

def to_unicode(value):
    if isinstance(value, str):
        return value.decode('utf-8')
    else:
        return value


def to_str(value):
    if isinstance(value, unicode):
        return value.encode('utf-8')
    else:
        return value
