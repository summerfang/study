tasklist /FI "IMAGENAME eq notepad.exe" /FO CSV > search.log

FOR /F %%A IN (search.log) DO IF %%~zA EQU 0 GOTO end

start notepad.exe

:end

del search.log