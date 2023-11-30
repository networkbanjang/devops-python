from dotenv import load_dotenv
from datetime import datetime
import os
import s3logic
from fileCheck import filecheck

load_dotenv()


def main():
    aws_access = os.getenv("AWS_ACCESS")
    aws_secret = os.getenv("AWS_SECRET")
    today = datetime.now().strftime('%Y%m%d')
    backupdir = os.getenv("BACKUP_PATH")
    backupfile = os.getenv("BACKUPFILE")

    s3 = s3logic.s3_connection(aws_access,aws_secret)
    filePath = filecheck(backupdir,backupfile)
    if filePath:
        print("업로드 시작")
        bucketName = os.getenv("BUCKETNAME")
        fileName = today+backupfile
        if s3logic.s3_upload(s3,filePath,bucketName,fileName):
            print(today+"업로드 완료")
    else:
        print("파일이 존재하지 않습니다.")

if __name__ == "__main__":
    main()
