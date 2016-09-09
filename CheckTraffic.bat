@ECHO OFF

SET ORIGIN=XXX
SET DESTINATION=XXX

IF "%1"=="" GOTO :CheckTraffic
IF "%1"=="setup" GOTO :CheckTraffic_setup
ECHO Invalid input: %1
GOTO :EOF

:CheckTraffic
SET STARTING_DIRECTORY=%CD%
CD %~dp0
CALL python CheckTraffic.py "%ORIGIN%" "%DESTINATION%"
CD %STARTING_DIRECTORY%
GOTO :EOF

:CheckTraffic_setup
SETX PATH "%PATH%;%CD%" >NUL
ECHO Done setting up CheckTraffic.