# Get URL from user
$url = Read-Host -Prompt "Enter the URL to download"

# Get save path from user
$savePath = Read-Host -Prompt "Enter the save path (e.g., C:\Downloads\file.txt)"

# Extract directory from the full path
$directory = Split-Path -Path $savePath -Parent

# Create directory if it doesn't exist
if (-not (Test-Path -Path $directory -PathType Container)) {
    Write-Host "Creating directory: $directory"
    try {
        New-Item -Path $directory -ItemType Directory -Force | Out-Null
        Write-Host "Directory created successfully." -ForegroundColor Green
    }
    catch {
        Write-Host "Failed to create directory: $_" -ForegroundColor Red
        return
    }
}

# Download the file
try {
    Write-Host "Downloading file from $url to $savePath..."
    $webClient = New-Object System.Net.WebClient
    $webClient.DownloadFile($url, $savePath)
    Write-Host "Download completed successfully!" -ForegroundColor Green
}
catch {
    Write-Host "Error downloading file: $_" -ForegroundColor Red
}

# Pause to show results
Write-Host "`nPress any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")