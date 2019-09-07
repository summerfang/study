@echo %time%
@echo %time:~0%
@echo %time:~0,5%
@echo %time:~0,8%
@echo %time:~3,-3%
@echo %time:~3%
@echo %time:~-3%

@echo %cd:~3%

set a="abcd1234"
echo %a%
set a=%a:1=kk%
echo %a%