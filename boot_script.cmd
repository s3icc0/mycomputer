@echo off
echo.
echo.
echo.
echo    . . . Initial PC setup . . .
timeout /t 10 /nobreak
echo.
echo.
echo.
start C:\Windows\System32\SndVol.exe
echo.
echo Launching Volume Mixer
echo.
timeout /t 1 /nobreak
echo.
echo Launching Repro
echo.
C:\NIRCMD\NIRCMDC setdefaultsounddevice "Repro" 0
C:\NIRCMD\NIRCMDC setdefaultsounddevice "Repro" 1
C:\NIRCMD\NIRCMDC setdefaultsounddevice "Repro" 2
timeout /t 1 /nobreak
echo.
echo Launching Radio
echo.
start E:\Desktop\PLAYLISTY\iRADIO.m3u8
timeout /t 1 /nobreak
echo.
echo Launching Budget
echo.
echo.
echo.

exit
