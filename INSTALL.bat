@echo off
REM Fote CLI Agent Installer
REM Adds fote command to PATH

echo.
echo ========================================
echo   Fote CLI Agent Installer
echo   Author: 765g
echo ========================================
echo.

REM Install required Python package
echo [1/3] Installing dependencies...
pip install requests prompt-toolkit --quiet
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo      Done!

REM Add current directory to PATH (User level)
echo.
echo [2/3] Adding to PATH...
set "CURRENT_DIR=%~dp0"
set "CURRENT_DIR=%CURRENT_DIR:~0,-1%"

REM Add to user PATH
for /f "skip=2 tokens=3*" %%A in ('reg query HKCU\Environment /v PATH 2^>nul') do set "USER_PATH=%%A %%B"
if not defined USER_PATH set "USER_PATH="

REM Check if already in PATH
echo %USER_PATH% | findstr /C:"%CURRENT_DIR%" >nul
if %ERRORLEVEL% EQU 0 (
    echo      Already in PATH!
) else (
    setx PATH "%USER_PATH%;%CURRENT_DIR%"
    echo      Added to PATH!
)

REM Create alias in PowerShell profile
echo.
echo [3/3] Setting up PowerShell alias...
powershell -Command "if (!(Test-Path $PROFILE)) { New-Item -Path $PROFILE -ItemType File -Force | Out-Null }; $aliasLine = \"`nfunction fote { python '%CURRENT_DIR%\fote.py' @args }\"; if (!(Select-String -Path $PROFILE -Pattern 'function fote' -Quiet)) { Add-Content -Path $PROFILE -Value $aliasLine }"
echo      Done!

echo.
echo ========================================
echo   Installation Complete!
echo ========================================
echo.
echo Usage:
echo   fote "your message"
echo   fote -i
echo   fote -l
echo.
echo IMPORTANT: Restart your terminal for changes to take effect!
echo.
pause
