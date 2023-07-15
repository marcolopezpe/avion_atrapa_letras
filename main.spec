# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('./assets/audio/*.mp3', 'assets/audio'),
        ('./assets/images/avion/*.png', 'assets/images/avion'),
        ('./assets/images/hearts/*.png', 'assets/images/hearts'),
        ('./assets/images/letras/*.png', 'assets/images/letras'),
        ('./assets/images/letras_transparentes/*.png', 'assets/images/letras_transparentes'),
        ('./assets/images/numeros/*.png', 'assets/images/numeros'),
        ('./assets/images/vocales/*.png', 'assets/images/vocales'),
        ('./assets/images/*.png', 'assets/images'),
        ('./assets/sounds/*.ogg', 'assets/sounds'),
        ('./assets/sounds/*.mp3', 'assets/sounds')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
app = BUNDLE(
    exe,
    name='main.app',
    icon=None,
    bundle_identifier=None,
)
