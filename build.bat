dir venv_rebot
@if %ERRORLEVEL%==0 goto :ACTIVATE_VENV
python -m venv venv_rebot
call venv_rebot\Scripts\activate.bat
python -m pip install -r requirements.txt

:ACTIVATE_VENV
call venv_rebot\Scripts\activate.bat

where python
where pyinstaller
pause
pyinstaller build.spec