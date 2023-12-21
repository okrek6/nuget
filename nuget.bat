: : Is Python installed?

python --version >NUL 2>&1
if errorlevel 1 (
    powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.9.1/python-3.9.1-amd64.exe -OutFile python-3.9.1-amd64.exe"

    start /wait python-3.9.1-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

    del python-3.9.1-amd64.exe

    goto :EOF
)

python nuget.py