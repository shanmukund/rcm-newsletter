# PowerShell script to create Windows Scheduled Task for RCM Newsletter
# Run this script as Administrator to set up the weekly Friday schedule

$TaskName = "RCM Newsletter Weekly Generation"
$TaskDescription = "Automatically generates the RCM Pulse Weekly newsletter every Friday"
$ScriptPath = Join-Path $PSScriptRoot "run_newsletter_generation.bat"
$StartTime = "09:00"

Write-Host "Setting up scheduled task: $TaskName" -ForegroundColor Cyan
Write-Host "Script location: $ScriptPath" -ForegroundColor Gray
Write-Host "Schedule: Every Friday at $StartTime" -ForegroundColor Gray
Write-Host ""

# Remove existing task if it exists
$existingTask = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if ($existingTask) {
    Write-Host "Removing existing task..." -ForegroundColor Yellow
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
}

# Create the action
$Action = New-ScheduledTaskAction -Execute $ScriptPath -WorkingDirectory $PSScriptRoot

# Create the trigger - every Friday at 9 AM
$Trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Friday -At $StartTime

# Create task settings
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -RunOnlyIfNetworkAvailable -ExecutionTimeLimit (New-TimeSpan -Hours 2)

# Create the principal
$Principal = New-ScheduledTaskPrincipal -UserId "$env:USERDOMAIN\$env:USERNAME" -LogonType S4U

# Register the scheduled task
try {
    Register-ScheduledTask -TaskName $TaskName -Description $TaskDescription -Action $Action -Trigger $Trigger -Settings $Settings -Principal $Principal | Out-Null

    Write-Host "SUCCESS: Scheduled task created!" -ForegroundColor Green
    Write-Host ""
    Write-Host "Task Details:" -ForegroundColor Cyan
    Write-Host "  Name: $TaskName" -ForegroundColor White
    Write-Host "  Schedule: Every Friday at $StartTime" -ForegroundColor White

    $nextRun = (Get-ScheduledTaskInfo -TaskName $TaskName).NextRunTime
    Write-Host "  Next Run: $nextRun" -ForegroundColor Yellow

    Write-Host ""
    Write-Host "To view in Task Scheduler: taskschd.msc" -ForegroundColor Gray
    Write-Host "To test now: Start-ScheduledTask -TaskName `"$TaskName`"" -ForegroundColor Gray

} catch {
    Write-Host "ERROR: Failed to create task - $_" -ForegroundColor Red
    Write-Host "Run PowerShell as Administrator" -ForegroundColor Yellow
    exit 1
}
