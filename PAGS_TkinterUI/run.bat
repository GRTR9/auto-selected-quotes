@echo off
cd /d %~dp0

call .venv\Scripts\activate
python --version
echo Running...
python main.py

pause
