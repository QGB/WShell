@for %%i in (%f%) do @set fDriver=%%~di
@for %%i in (%f%) do @set folder=%%~dpi

@%fDriver%&cd %folder%
: echo %d%