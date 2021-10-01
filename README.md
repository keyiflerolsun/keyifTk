# keyifTk

Tkinter Taban Dosyaları

## Kopya Kağıdı

```ps1
## Linux
python3 -m nuitka --onefile --follow-imports --include-plugin-directory=Temalar --windows-icon-from-ico=logo.png basla.py

## Windows
python -m nuitka --plugin-enable=tk-inter --windows-disable-console --onefile --follow-imports --include-plugin-directory=Temalar --windows-icon-from-ico=logo.png basla.py

pyinstaller --noconfirm --onefile --windowed --icon "logo.png" --hidden-import "tkinter" --add-data "Temalar;Temalar"  "basla.py"

pyminifier --gzip --lzma --destdir=tmp/. *.py
```
