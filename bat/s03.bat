@echo off
FOR /F "tokens=1,2,3,4 delims=,:" %%G IN ("deposit,$4500,123.4,12-AUG-09:Test") DO @echo Date paid %%G %%H %%I %%J
