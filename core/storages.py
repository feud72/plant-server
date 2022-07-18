from storages.backends.s3boto3 import S3Boto3Storage

from django.conf import settings

__all__ = (
    # "S3StaticStorage",
    "S3DefaultStorage",
)


# 정적 파일용
# class S3StaticStorage(S3Boto3Storage):
#     default_acl = "public-read"
#     location = "static"

#     def __init__(self, *args, **kwargs):
#         kwargs["custom_domain"] = settings.AWS_CLOUDFRONT_DOMAIN
#         super(S3StaticStorage, self).__init__(*args, **kwargs)


# 미디어 파일용
class S3DefaultStorage(S3Boto3Storage):
    default_acl = "private"
    location = "media"

    def __init__(self, *args, **kwargs):
        kwargs["custom_domain"] = settings.AWS_CLOUDFRONT_DOMAIN
        super(S3DefaultStorage, self).__init__(*args, **kwargs)
