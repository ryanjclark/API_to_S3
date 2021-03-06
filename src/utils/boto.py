import boto3
import logging
from botocore.exceptions import ClientError

def upload_to_s3(output, bucket, folder):
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(
                Filename=output,
                Bucket=bucket,
                Key="{}/{}".format(folder, output))
    except ClientError as e:
        logging.error(e)
        return False
    return True

