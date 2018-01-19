import boto3, botocore
import os
from integrations import S3Sync

s3connection = S3Sync(os.environ['AWS_S3_ACCESS_KEY'], os.environ['AWS_SECRET_KEY'])

s3 = boto3.resource(
    's3',
    aws_access_key_id=os.environ['AWS_S3_ACCESS_KEY'],
    aws_secret_access_key=os.environ['AWS_SECRET_KEY']
)

# Call S3 to list current buckets
#response = s3.list_buckets()

my_bucket = s3.Bucket('stitched-training')
for object in my_bucket.objects.all():
    print(object)
