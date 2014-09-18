import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "excludes": []}

base = None

if sys.platform == "win32":
    base =  "Win32GUI"

setup (
        name = "pySARPP",
        version = "0.1",
        description = "DCS MiG21bis SARPP interpreter",
        options = {"build_exe": build_exe_options},
        executables = [Executable("Sarpp.py", base=base)])
