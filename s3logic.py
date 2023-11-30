import boto3
import logging

def s3_connection(aws_access,aws_secret):

    try:
        s3 = boto3.client(
            service_name="s3",
            region_name="ap-northeast-2", # 자신이 설정한 bucket region
            aws_access_key_id=aws_access,
            aws_secret_access_key=aws_secret,
        )
    except Exception as e:
        logging.error(e)
        print(e)
    else:
        print("s3 bucket connected!")
        return s3

def s3_upload(s3,filePath,bucketName,fileName):
    try:
        s3.upload_file(
            filePath,
            bucketName,
            fileName,
            ExtraArgs={"ACL": "private"},
        )
    except Exception as e:
        logging.error(e)
        print(e)
        return False
    return True
