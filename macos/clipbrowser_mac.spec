# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['/Users/ehh/Desktop/clipbrowser/clipbrowser_mac.py'],
    pathex=[],
    binaries=[],
    datas=[],
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
    name='clipbrowser_mac',
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
    name='ClipBrowser.app',
    icon='clipbrowser.icns',
    bundle_identifier='shystudios.clipbrowser',
    version='1.0.0',
    info_plist={
        'NSPrincipalClass': 'BrowserApplication',
        'NSAppleScriptEnabled': True,
             'CFBundleURLTypes' : [
                {
                    'CFBundleURLName' : 'Web site URL',
                    'CFBundleURLSchemes' : ['http', 'https']
                },
                {
                    'CFBundleURLName' : 'Local file URL',
                    'CFBundleURLSchemes' : ['file']
                },
             ]
    },
)
