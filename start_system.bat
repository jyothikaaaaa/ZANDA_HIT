@echo off
echo Starting Janata Audit System...
echo ==============================

REM Set environment variables
set NODE_ENV=development
set BACKEND_PORT=3001
set FRONTEND_PORT=3000
set PYTHONHTTPSVERIFY=0

echo Setting up Python environment...
if not exist ".venv" (
    python -m venv .venv
    call .venv\Scripts\activate
    pip install -r python_scripts\requirements.txt
) else (
    call .venv\Scripts\activate
)

REM Kill any existing processes on our ports
echo Cleaning up existing processes...
for /f "tokens=5" %%a in ('netstat -aon ^| find ":%BACKEND_PORT%" ^| find "LISTENING"') do taskkill /F /PID %%a >nul 2>&1
for /f "tokens=5" %%a in ('netstat -aon ^| find ":%FRONTEND_PORT%" ^| find "LISTENING"') do taskkill /F /PID %%a >nul 2>&1

REM Install backend dependencies
echo Installing backend dependencies...
cd backend
call npm install
if %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to install backend dependencies
    goto error
)
cd ..

REM Install frontend dependencies
echo Installing frontend dependencies...
call npm install --legacy-peer-deps
if %ERRORLEVEL% NEQ 0 (
    echo Error: Failed to install frontend dependencies
    goto error
)

echo Starting components in order...

REM Start Backend Server
echo Starting Backend Server...
start "Backend Server" cmd /k "cd backend && set PORT=%BACKEND_PORT% && node server.js"

REM Wait for backend to initialize
echo Waiting for backend to start...
timeout /t 5
netstat -ano | find ":%BACKEND_PORT%" | find "LISTENING" >nul
if %ERRORLEVEL% NEQ 0 (
    echo Error: Backend failed to start on port %BACKEND_PORT%
    goto error
)

REM Start Hybrid Health Engine
echo Starting AI Models...
start "Hybrid Health Engine" cmd /k "C:/Users/Jyothika/Desktop/jannat_audit/.venv/Scripts/python.exe python_scripts/hybrid_health_engine/run.py"

REM Wait for AI models to load
timeout /t 3

REM Start Data Scrapers
echo Starting Data Scrapers...
start "Project Scraper" cmd /k "C:/Users/Jyothika/Desktop/jannat_audit/.venv/Scripts/python.exe python_scripts/robust_scraper.py"

REM Wait for scrapers to initialize
timeout /t 3

REM Start Frontend Application
echo Starting Frontend Application...
start "Frontend" cmd /k "set PORT=%FRONTEND_PORT% && npm start"

echo.
echo Checking component status...
timeout /t 10

REM Check if frontend started
netstat -ano | find ":%FRONTEND_PORT%" | find "LISTENING" >nul
if %ERRORLEVEL% NEQ 0 (
    echo Warning: Frontend might not have started properly on port %FRONTEND_PORT%
) else (
    echo Frontend is running on port %FRONTEND_PORT%
)

REM Check if backend is still running
netstat -ano | find ":%BACKEND_PORT%" | find "LISTENING" >nul
if %ERRORLEVEL% NEQ 0 (
    echo Warning: Backend might not be running on port %BACKEND_PORT%
) else (
    echo Backend is running on port %BACKEND_PORT%
)

echo.
echo System URLs:
echo -----------
echo Frontend: http://localhost:%FRONTEND_PORT%
echo Backend API: http://localhost:%BACKEND_PORT%
echo Health Dashboard: http://localhost:%FRONTEND_PORT%/health-dashboard
echo Project List: http://localhost:%FRONTEND_PORT%/projects
echo Analytics: http://localhost:%FRONTEND_PORT%/analytics

echo.
echo System Components:
echo ----------------
echo 1. Backend Server [Port %BACKEND_PORT%]
echo 2. Frontend Application [Port %FRONTEND_PORT%]
echo 3. Hybrid Health Engine
echo 4. Project Scrapers
echo.
echo To stop all components, run stop_all.bat
echo Press any key to exit this window (other components will keep running)
goto end

:error
echo.
echo Error: System failed to start properly
echo Running cleanup...
call stop_all.bat
exit /b 1

:end
pause > nul