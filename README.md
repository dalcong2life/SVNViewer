SVN Diff Viewer
========


- Python 2.7.9
- Flask 0.11.1

# 개요
본 프로젝트는 subversion으로 관리되는 소스의 diff 내역을 효율적으로 보기위한 viewer를 제공한다.

# Install

먼저, python과 subversion 간 커넥터 역할을 하는 pysvn 패키지를 설치해야한다.
설치된 subversion 서버 버전과 운영 서버 환경에 맞는 버전을 다운받아서 설치한다.

> py27-pysvn-svn193-1.9.0-1849-Win32.exe	1.9.0	python.org 2.7	SVN 1.9.3	Win32
http://tigris.org/files/documents/1233/49489/py27-pysvn-svn193-1.9.0-1849-Win32.exe

Windows 환경에서 설치된 pysvn은 전역에 설치되므로 가상환경을 구성할 경우 아래 명령으로 전역에 설치된 pysvn 패키지를 사용할 수 있도록 한다.
```
virtualenv --system-site-packages
```

프로젝트에서 사용되는 필수 패키지를 설치한다.
```
$ pip install -r requirements.txt
```

# 실행하기

```
// Database 생성
$ python manage.py migrate

// 서버 실행
$ python manage.py run
```



#db file creation
sqlite3 database.db < schema.sql
