# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Developer\\NRB Pickle Boats'],
             binaries=[],
             datas=[('pickle.ico','.'),('.env','.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='NRB Boats Folder Pickler',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='pickle.ico')