@echo off
REM DuckDuckGo CLI Installation Script for Windows
REM This script installs the DuckDuckGo CLI tool system-wide on Windows

echo DuckDuckGo CLI Windows Installation Script
echo ==========================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH.
    echo Please install Python 3.8 or higher from https://python.org
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

echo Python is installed.

REM Check if pip is available
pip --version >nul 2>&1
if errorlevel 1 (
    echo Error: pip is not available.
    echo Please ensure pip is installed with Python.
    pause
    exit /b 1
)

echo pip is available.

REM Install the package
echo Installing DuckDuckGo CLI...
pip install .

if errorlevel 1 (
    echo Error: Installation failed.
    echo This might be due to permission issues.
    echo Try running this script as Administrator.
    pause
    exit /b 1
)

echo.
echo Installation completed successfully!
echo.
echo You can now use the DuckDuckGo CLI with the command: ddg-cli
echo.
echo Examples:
echo   ddg-cli search "Python programming"
echo   ddg-cli search "machine learning" --results 15
echo   ddg-cli history list
echo.
echo For more information, run: ddg-cli --help
echo.
pause