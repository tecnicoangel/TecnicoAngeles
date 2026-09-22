@echo off
title TecnicoAngel App
color 0A
cls

echo ===========================================
echo   INICIANDO APLICACION TECNICOANGEL
echo ===========================================
echo.

python app.py

if %errorlevel% neq 0 (
    color 0C
    echo.
    echo [ERROR] Ocurrio un problema al abrir la aplicacion.
    pause
)