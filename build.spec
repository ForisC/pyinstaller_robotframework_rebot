# -*- mode: python ; coding: utf-8 -*-
def get_datas():
    import robot
    from robot.htmldata import rebot
    from robot.htmldata import common
    from robot.htmldata import lib as _lib

    from pathlib import Path
    result = []

    folder = Path(rebot.__file__).parent
    folders = [
        Path(rebot.__file__).parent,
        Path(common.__file__).parent,
        Path(_lib.__file__).parent,
    ]
    files = []
    for folder in folders:
        files += folder.iterdir()

    files = [x for x in files if x.is_file() and x.suffix != ".py"]
    site_package_path = Path(robot.__file__).parent.parent
    for file in files:
        result.append((str(file), str(file.relative_to(site_package_path).parent)))
    return result

a = Analysis(
    ['rebot_wrapper.py'],
    pathex=[],
    binaries=[],
    datas=get_datas(),
    hiddenimports=[
        "robot.htmldata.rebot",
        "robot.htmldata.common",
        "robot.htmldata.lib",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='rebot',
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
    icon='icon.ico',
)
