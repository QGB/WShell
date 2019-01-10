@cdnote & start "" G:\QGB\Anaconda3\python.exe G:\QGB\Anaconda3\Scripts\jupyter-notebook-script.py --NotebookApp.iopub_data_rate_limit=1.0e10 --ip=0.0.0.0 %*

@REM (
@REM echo #coding:utf-8  this end can not be deleted and unable to append any char (^)
@REM echo import re
@REM echo import sys
@REM echo from notebook.notebookapp import main
@REM echo if __name__ == '__main__':
@REM echo     sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe^)?$', '', sys.argv[0]^)
@REM echo     sys.exit(main(^)^)
@REM )|python


@REM call cdAconda3
@REM start jupyter-notebook.exe