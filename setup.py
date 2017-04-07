from cx_Freeze import setup, Executable

exe = [Executable("Alert Manager.py", base = "Win32GUI")]

setup(
    name = "Alert Manager",
    version = "1.0.0",
    description = "Alert Manager e-Vertical",
    executables = exe)
