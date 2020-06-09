import hashlib
import os
from datetime import datetime


def hash_str(str, digits=8):
    hash_str = hashlib.sha1(str.encode())
    return hash_str.hexdigest()[:digits]


def upload_location(instance, filename):
    name_file, ext_file = os.path.splitext(filename)
    filename = "{0}{1}".format(hash_str(name_file, 16), ext_file)
    date_gen = "{:%y%m%d%H%M%S%z}".format(datetime.now())
    file_path = '{prefix}/{id}/{date}-{filename}'.format(
        id=str(instance.pk), date=date_gen,
        filename=filename, prefix=instance.__class__.__name__.lower())
    return file_path
