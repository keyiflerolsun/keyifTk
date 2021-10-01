#!/usr/bin/python
# -*- coding: utf-8 -*-
from cx_Freeze import setup, Executable
from sys import platform

exe = Executable(
    script      = 'basla.py',
    base        = 'Win32GUI' if platform=='win32' else None,
    icon        = 'logo.png',
    targetName  = 'keyifTk.exe'
)

opt = {
    'build_exe': {
        'include_files': ['Temalar']
   }
}

setup(
    name        = 'keyifTk',
    version     = '1.0',
    author      = '@keyiflerolsun',
    description = '@KekikAkademi için Yazılmıştır..',
    executables = [exe],
    options     = opt,
)