@echo off
cd /d "%~dp0"
set "PATH=%~dp0.venv\Scripts;%PATH%"
echo AzurPilot 启动中...
"%~dp0.venv\Scripts\python.exe" "%~dp0launcher.py"
pause