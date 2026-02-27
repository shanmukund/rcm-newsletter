# RCM Newsletter - Weekly Scheduling Setup

## Overview
This setup will automatically generate your RCM Pulse Weekly newsletter every Friday at 9:00 AM.

## Quick Setup (Recommended)

### Option 1: Use the Setup Script
1. Right-click on `create_task.bat`
2. Select **"Run as administrator"**
3. The task will be created automatically

### Option 2: Manual Task Scheduler Setup
If the automated script doesn't work, follow these steps:

1. **Open Task Scheduler**
   - Press `Win + R`
   - Type `taskschd.msc` and press Enter

2. **Create a New Task**
   - Click "Create Task" (not "Create Basic Task")
   - Name: `RCM Newsletter Weekly Generation`
   - Description: `Automatically generates the RCM Pulse Weekly newsletter every Friday`
   - Select "Run whether user is logged on or not"
   - Check "Run with highest privileges"

3. **Set the Trigger**
   - Go to the "Triggers" tab
   - Click "New..."
   - Begin the task: "On a schedule"
   - Settings: Weekly
   - Days: Friday
   - Start time: 9:00 AM
   - Click "OK"

4. **Set the Action**
   - Go to the "Actions" tab
   - Click "New..."
   - Action: "Start a program"
   - Program/script: Browse to and select `run_newsletter_generation.bat`
   - Start in: Browse to and select this folder
   - Click "OK"

5. **Configure Settings**
   - Go to the "Settings" tab
   - Check "Allow task to be run on demand"
   - Check "Run task as soon as possible after a scheduled start is missed"
   - Uncheck "Stop the task if it runs longer than"
   - Click "OK"

6. **Save the Task**
   - Click "OK" to save
   - You may need to enter your Windows password

## Testing the Setup

To test if the schedule works, run this command in PowerShell:
```powershell
Start-ScheduledTask -TaskName "RCM_Newsletter_Weekly"
```

Or right-click the task in Task Scheduler and select "Run".

## Schedule Details

- **Frequency**: Every Friday
- **Time**: 9:00 AM
- **First Run**: This Friday (or tomorrow if today is Thursday)
- **Action**: Runs `run_newsletter_generation.bat` which calls `generate_newsletter.py`

## Files Created

- `generate_newsletter.py` - Python script that triggers newsletter generation
- `run_newsletter_generation.bat` - Batch wrapper for the Python script
- `create_task.bat` - Automated task creation script
- `setup_schedule.ps1` - PowerShell alternative for task creation
- `SCHEDULING_INSTRUCTIONS.md` - This file

## Logs

Each run creates a log file in this directory:
```
newsletter_generation_YYYYMMDD_HHMMSS.log
```

Check these logs if something goes wrong.

## Troubleshooting

### Task doesn't run
- Check Task Scheduler history (enable it in the Actions menu)
- Verify Python is installed and in your PATH
- Check the log files for errors

### Permission denied errors
- Run `create_task.bat` as Administrator
- Or manually create the task in Task Scheduler with elevated privileges

### Claude CLI not found
- Ensure Claude Code CLI is installed
- Make sure `claude` command is in your Windows PATH
- Test by running `claude --version` in a command prompt

## Manual Execution

If you want to generate a newsletter manually at any time:
```bash
python generate_newsletter.py
```

Or simply ask Claude to "generate the next weekly newsletter" in this project directory.
