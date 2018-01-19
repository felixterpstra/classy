class S3Sync():
    def __init__(self, s3_key, s3_secret):
        self.s3_key = s3_key
        self.s3_secret = s3_secret

    def keys(self):
        return '{} - {}'.format(self.s3_key, self.s3_secret)
