#!D:\Documents\redditpy\RedditPy\RedditPy\env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pyjade==4.0.0','console_scripts','pyjade'
__requires__ = 'pyjade==4.0.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pyjade==4.0.0', 'console_scripts', 'pyjade')()
    )
