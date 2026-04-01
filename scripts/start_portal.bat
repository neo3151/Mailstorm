@echo off
set "portal_dir=c:\Users\neo31\Mailstorm\web"

echo Starting the Mailstorm Abyssal Portal...
echo [██████░░░░] 30% ^| Navigating to web directory...
cd /d "%portal_dir%"

echo [████████░░] 60% ^| Checking dependencies...
call npm install

echo [██████████] 100% ^| Launching Vite Development Server...
echo.
call npm run dev
pause
