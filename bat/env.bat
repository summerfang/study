echo %HOMEPATH%
echo %HOMEDRIVE%

REM "The /c argument tells the command processor to open, run the specified command, then close when it's done. You can also use the /k argument, which tells CMD.exe to open, run the specified command, then keep the window open."
cd %HOMEPATH%
%comspec% /k

