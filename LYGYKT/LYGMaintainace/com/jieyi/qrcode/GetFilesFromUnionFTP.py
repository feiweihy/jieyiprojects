'''
从银联商户的FTP上获取对账文件
'''

import ftplib,datetime

host = ''#url
username = ''#username
password = ''#password

ftp = ftplib.FTP(host)  # 实例化FTP对象
ftp.login(username, password)  # 登录

# 获取当前路径
pwd_path = ftp.pwd()
print("FTP当前路径:", pwd_path)

# 更改到工作路径
ftp.cwd("/build")
pwd_path = ftp.pwd()
print("FTP当前路径:", pwd_path)

def getYesterday():
    today=datetime.date.today()
    oneday=datetime.timedelta(days=1)
    yesterday=today-oneday
    yesterdaystr = datetime.datetime.strftime(yesterday,"%Y-%m-%d")
    yesterdaystrret = yesterdaystr.replace("-","")
    return yesterdaystrret

# print(getYesterday())

files = ftp.nlst()
print(files)
filesNew = [x for x in files if '.txt' in x and getYesterday() in x]
print(filesNew)

def ftp_download(localpath,file):
     '''以二进制形式下载文件'''
     file_remote = file
     file_local = localpath+file
     bufsize = 1024  # 设置缓冲器大小
     fp = open(file_local, 'wb')
     ftp.retrbinary('RETR %s' % file_remote, fp.write, bufsize)
     fp.close()

for file in filesNew:
    print(file)
    ftp_download("E:\\111\\lygzhzf\\recv\\",file)

