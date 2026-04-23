# -*- mode: python ; coding: utf-8 -*-

NAME = "mlapi_server"


a = Analysis(
    ['mlapi_server.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=NAME,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=NAME,
)

import shutil
import os

dist_folder = os.path.join('dist', NAME)

frontend_src = 'frontend'
frontend_dst = os.path.join(dist_folder, 'frontend')

if os.path.exists(dist_folder):
    if os.path.exists(frontend_dst):
        shutil.rmtree(frontend_dst)
    shutil.copytree(frontend_src, frontend_dst)
