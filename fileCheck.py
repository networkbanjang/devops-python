import os

def findLastdir(backupdir):
    files = os.listdir(backupdir)
    directories = [f for f in files if os.path.isdir(os.path.join(backupdir, f))]
    if directories:
        # 디렉토리를 수정 시간을 기준으로 정렬
        directories.sort(key=lambda x: os.path.getmtime(os.path.join(backupdir, x)), reverse=True)

        # 가장 최신 디렉토리 가져오기
        lastdir = directories[0]
        print("가장 최신 디렉토리:", lastdir)
        return lastdir
    else:
        print("디렉토리가 없거나 파일만 있습니다.")

def filecheck(backupdir,backupfile):
    lastdir=findLastdir(backupdir)
    checkfile = backupdir+lastdir+"/"+backupfile
    print(checkfile)
    if os.path.isfile(checkfile):
        return checkfile
    return False

