@echo off
SETLOCAL ENABLEDELAYEDEXPANSION
cd /D "%~dp0"
for /R "D:\SimC Scripts\Dump\Input\Base" %%X IN (*.*) do (
    SET spec=%%~nX
    SET "ourDirectory=D:\SimC Scripts\Dump\Input\Cov\R1\!spec!"
    SET "baseFile=%%X"
    call :loopSoulbinds1 ourDirectory!, baseFile, spec
)
for /R "D:\SimC Scripts\Dump\Input\Base" %%X IN (*.*) do (
    SET spec=%%~nX
    SET "ourDirectory=D:\SimC Scripts\Dump\Input\Cov\R5\!spec!"
    SET "baseFile=%%X"
    call :loopSoulbinds5 ourDirectory!, baseFile, spec
)
for /R "D:\SimC Scripts\Dump\Input\Base" %%X IN (*.*) do (
    SET spec=%%~nX
    SET "ourDirectory=D:\SimC Scripts\Dump\Input\Cov\R7\!spec!"
    SET "baseFile=%%X"
    call :loopSoulbinds5 ourDirectory!, baseFile, spec
)
for /R "D:\SimC Scripts\Dump\Input\Base" %%X IN (*.*) do (
    SET spec=%%~nX
    SET "ourDirectory=D:\SimC Scripts\Dump\Input\Cov\R10\!spec!"
    SET "baseFile=%%X"
    call :loopSoulbinds10 ourDirectory!, baseFile, spec
)
for /R "D:\SimC Scripts\Dump\Input\Base" %%X IN (*.*) do (
    SET spec=%%~nX
    SET "ourDirectory=D:\SimC Scripts\Dump\Input\Cov\R15\!spec!"
    SET "baseFile=%%X"
    call :loopSoulbinds15 ourDirectory!, baseFile, spec
)

:loopSoulbinds1
set "specDirectory=!%1!"
set "baseFile=!%2!"
set "spec=!%3!"
for /R "%specDirectory%" %%Y IN (*.*) do (
    set soulbind=%%~nY
    CALL "..\simc.exe" "GenericOptions.simc" "!baseFile!" "%%Y"
    MOVE /Y "output.txt" "D:\SimC Scripts\Dump\Output\Cov\5T\R1\!spec!_!soulbind!.txt"
    MOVE /Y "output.json" "D:\SimC Scripts\Dump\Output\Cov\5T\R1\!spec!_!soulbind!.json"
)
exit /B 0

:loopSoulbinds5
set "specDirectory=!%1!"
set "baseFile=!%2!"
set "spec=!%3!"
for /R "%specDirectory%" %%Y IN (*.*) do (
    set soulbind=%%~nY
    CALL "..\simc.exe" "GenericOptions.simc" "!baseFile!" "%%Y"
    MOVE /Y "output.txt" "D:\SimC Scripts\Dump\Output\Cov\5T\R5\!spec!_!soulbind!.txt"
    MOVE /Y "output.json" "D:\SimC Scripts\Dump\Output\Cov\5T\R5\!spec!_!soulbind!.json"
)
exit /B 0

:loopSoulbinds7
set "specDirectory=!%1!"
set "baseFile=!%2!"
set "spec=!%3!"
for /R "%specDirectory%" %%Y IN (*.*) do (
    set soulbind=%%~nY
    CALL "..\simc.exe" "GenericOptions.simc" "!baseFile!" "%%Y"
    MOVE /Y "output.txt" "D:\SimC Scripts\Dump\Output\Cov\5T\R7\!spec!_!soulbind!.txt"
    MOVE /Y "output.json" "D:\SimC Scripts\Dump\Output\Cov\5T\R7\!spec!_!soulbind!.json"
)
exit /B 0

:loopSoulbinds10
set "specDirectory=!%1!"
set "baseFile=!%2!"
set "spec=!%3!"
for /R "%specDirectory%" %%Y IN (*.*) do (
    set soulbind=%%~nY
    CALL "..\simc.exe" "GenericOptions.simc" "!baseFile!" "%%Y"
    MOVE /Y "output.txt" "D:\SimC Scripts\Dump\Output\Cov\5T\R10\!spec!_!soulbind!.txt"
    MOVE /Y "output.json" "D:\SimC Scripts\Dump\Output\Cov\5T\R10\!spec!_!soulbind!.json"
)
exit /B 0

:loopSoulbinds15
set "specDirectory=!%1!"
set "baseFile=!%2!"
set "spec=!%3!"
for /R "%specDirectory%" %%Y IN (*.*) do (
    set soulbind=%%~nY
    CALL "..\simc.exe" "GenericOptions.simc" "!baseFile!" "%%Y"
    MOVE /Y "output.txt" "D:\SimC Scripts\Dump\Output\Cov\5T\R15\!spec!_!soulbind!.txt"
    MOVE /Y "output.json" "D:\SimC Scripts\Dump\Output\Cov\5T\R15\!spec!_!soulbind!.json"
)
exit /B 0