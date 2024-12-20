# -*- mode: python ; coding: utf-8 -*-

added_files = [
    ("image", "image"),  # Includes the entire 'image' folder
    ("image/logo_Mini.png", "image/logo_Mini.png"),
    ("image/Raspberry_4WD_Car.png", "image/Raspberry_4WD_Car.png"),
    ("image/Raspberry_4WD_M_Car.png", "image/Raspberry_4WD_M_Car.png"),
    ("IP.txt", "IP.txt"),
    ("haarcascade_frontalface_default.xml", "haarcascade_frontalface_default.xml")
]


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
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
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
