
@echo off


rem Set the path to your virtual environment activate script
set VENV_PATH=D:\python\DRAW-RTS\venv\Scripts\activate

rem Activate the virtual environment
call "%VENV_PATH%"

rem Navigate to the directory of your Python script
cd /d D:\python\DRAW-RTS

rem Run your Python script
python run.py

rem Deactivate the virtual environment (optional)
deactivate