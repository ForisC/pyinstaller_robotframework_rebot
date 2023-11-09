@dir venv
@if %ERRORLEVEL%==0 goto :ACTIVATE_VENV
@python -m venv venv
call venv\Scripts\activate.bat
python -m pip install -r requirements.txt

:ACTIVATE_VENV
call venv\Scripts\activate.bat
pyinstaller build.spec