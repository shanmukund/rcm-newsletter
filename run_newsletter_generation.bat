@echo off
REM RCM Newsletter Weekly Generation - Task Scheduler Wrapper
REM This script is called by Windows Task Scheduler every Friday

cd /d "%~dp0"
echo Starting RCM Newsletter generation at %date% %time%

REM Run the Python script
python generate_newsletter.py

REM Log completion
echo Completed at %date% %time%
exit /b %ERRORLEVEL%
