@echo off
for /R %%G in (*.bat) do (
    if not "%%G" == "%~f0" start /wait "%%G" CMD /c "%%G"
)
