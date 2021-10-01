# keyifTk

Tkinter Taban Dosyaları

## Kopya Kağıdı

```ps1
python -m nuitka --onefile --follow-imports --include-plugin-directory=Temalar --windows-icon-from-ico=logo.png basla.py

pyinstaller --noconfirm --onefile --windowed --icon "logo.png" --hidden-import "tkinter" --add-data "Temalar;Temalar"  "basla.py"

pyminifier --gzip --lzma --destdir=tmp/. *.py
```
