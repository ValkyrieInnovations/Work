Simple PowerShell scripts that I might use for work and/or homelab
At work, called with batch files from ScreenConnect toolbox

@echo off
powershell -ExecutionPolicy Bypass -Command "& {Invoke-Expression (New-Object Net.WebClient).DownloadString('URL')}"
