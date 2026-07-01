@echo off
cd /d "%~dp0"
set "PATH=%~dp0.venv\Scripts;%~dp0.venv\Scripts\git\cmd;%PATH%"
title AzurPilot
start "" "%~dp0.venv\Scripts\pythonw.exe" "%~dp0gui.py"
timeout /t 3 >nul
start http://127.0.0.1:25548