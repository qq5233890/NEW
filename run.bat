@echo off
cd /d "%~dp0"
set "_pyBin=%~dp0.venv\Scripts"
set "_GitBin=%~dp0.venv\Scripts\git\cmd"
set "PATH=%_pyBin%;%_GitBin%;%PATH%"

title AzurPilot Updater
"%_pyBin%\python.exe" -m deploy.installer
if %errorlevel% neq 0 (
    pause >nul
) else (
    start "AzurPilot" "%_pyBin%\pythonw.exe" "%~dp0gui.py" --electron
)