@echo off
REM Create Windows Scheduled Task for RCM Newsletter
REM Run this as Administrator

echo Creating scheduled task for RCM Newsletter...
echo.

schtasks /Create ^
  /SC WEEKLY ^
  /D FRI ^
  /TN "RCM_Newsletter_Weekly" ^
  /TR "\"%~dp0run_newsletter_generation.bat\"" ^
  /ST 09:00 ^
  /F

if %ERRORLEVEL% EQU 0 (
    echo.
    echo SUCCESS! Task created successfully.
    echo.
    echo Task will run every Friday at 9:00 AM
    echo First run: This Friday
    echo.
    echo To view the task: Open Task Scheduler ^(taskschd.msc^)
    echo To test now: schtasks /Run /TN "RCM_Newsletter_Weekly"
) else (
    echo.
    echo ERROR: Failed to create task.
    echo Please run this batch file as Administrator.
    echo Right-click and select "Run as administrator"
)

pause
