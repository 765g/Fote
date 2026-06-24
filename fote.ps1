# Fote CLI - PowerShell Wrapper
# Quick access to AI models from command line

$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
$pythonScript = Join-Path $scriptPath "fote.py"

# Check if Python is available
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Python not found. Please install Python 3.8 or higher." -ForegroundColor Red
    exit 1
}

# Pass all arguments to Python script
python $pythonScript $args
