set path=G:\QGB\Anaconda3\share\sdl2\bin\;%path%
set path=G:\QGB\Anaconda3\share\glew\bin\;%path%

@REM test 
python3 -c "from kivy.core.window._window_sdl2 import _WindowSDL2Storage"