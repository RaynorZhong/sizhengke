import random
import time
from hashlib import sha1
from django.core.exceptions import ValidationError
from django.conf import settings
from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible
from qcloud_cos import CosConfig, CosS3Client

secret_id = settings.COS_SECRET_ID
secret_key = settings.COS_SECRET_KEY
region = settings.COS_REGION
bucket = settings.COS_BUCKET
config = CosConfig(Region=region, Secret_id=secret_id, Secret_key=secret_key)
client = CosS3Client(config)
host = 'https://' + bucket + '.cos.' + region + '.myqcloud.com/'


@deconstructible
class CosStorage(Storage):
    def save(self, name, content, max_length=None):
        suffix = name.split('.')[-1]
        key = self.generate_key(suffix)
        try:
            response = client.put_object(
                Bucket=bucket,
                Body=content.read(),
                Key=key,
                EnableMD5=False,
                ContentDisposition='attachment'
            )
        except Exception as e:
            raise
        return host + key

    def generate_key(self, suffix):
        file_name = str(int(time.time() * 10000000)) + ''.join([str(random.randint(1, 9)) for i in range(3)])
        s = sha1()
        s.update(file_name.encode('utf-8'))
        file_name = str(s.hexdigest())
        key = file_name + '.' + suffix
        return key

    def url(self, name):
        return name