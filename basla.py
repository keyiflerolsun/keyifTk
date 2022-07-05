# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import tkinter as tk
from tkinter import messagebox
from base64 import encodebytes
from tkinter import ttk
from datetime import datetime

import threading, time

_dur_event = None

class SahteLog(threading.Thread):
    def __init__(self, treeview:ttk.Treeview):
        super().__init__()
        self._dur_event = threading.Event()
        self.treeview   = treeview

        global _dur_event
        _dur_event = self._dur_event

    def run(self):
        say = 1

        bilinen_zaman = -1
        while not self._dur_event.is_set():
            simdiki_zaman = datetime.now()

            if bilinen_zaman != simdiki_zaman.second:
                bilinen_zaman = simdiki_zaman.second

                if simdiki_zaman.second % 5 == 0:
                    self.treeview.insert(parent=say-1, index="end", iid=say, text=simdiki_zaman.strftime("%X"), values="HATA")
                else:
                    self.treeview.insert(parent="", index="end", iid=say, text=simdiki_zaman.strftime("%X"), values="BİLGİ")

                # Scrollbar Kaydır
                self.treeview.see(say)

                say += 1

            time.sleep(0.2)

class Uygulama(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        # Uygulamayı Responsive Hale Getirin
        for index in range(3):  # 3 Satır 3 Sütun
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        # Sağ Alt Köşeye Yeniden Boyutlandırma
        sizegrip = ttk.Sizegrip(self)
        sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))

        # Sağ Tık Menüsü
        sag_tik = tk.Menu(self, tearoff=False)
        sag_tik.add_command(label="Azure Light",      command=lambda : self.tk.call("set_theme", "Azure_light"))
        sag_tik.add_command(label="Azure Dark",       command=lambda : self.tk.call("set_theme", "Azure_dark"))
        sag_tik.add_command(label="Sun Valley Light", command=lambda : self.tk.call("set_theme", "Sun-Valley_light"))
        sag_tik.add_command(label="Sun Valley Dark",  command=lambda : self.tk.call("set_theme", "Sun-Valley_dark"))
        sag_tik.add_separator()
        sag_tik.add_command(label="Çıkış", command=pencereyi_kapat)
        self.bind("<Button-3>", lambda e: sag_tik.tk_popup(e.x_root, e.y_root))

        # Widgetlar
        self.onay_butonlari()
        self.radyo_butonlari()
        self.input_alanlari()
        self.treeview_alani()
        self.sekme_alani()

    def onay_butonlari(self):
        # Onay Butonları için bir Çerçeve Oluşturun
        onay_frame = ttk.LabelFrame(self, text="Onay Butonları", padding=(20, 10))
        onay_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

        # Onay Butonları
        self.onay_d_0 = tk.BooleanVar()
        onay_0 = ttk.Checkbutton(onay_frame, text="İşaretlenmemiş", variable=self.onay_d_0)
        onay_0.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

        self.onay_d_1 = tk.BooleanVar(value=True)
        onay_1 = ttk.Checkbutton(onay_frame, text="İşaretlenmiş", variable=self.onay_d_1)
        onay_1.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

        self.onay_d_2 = tk.BooleanVar()
        onay_2 = ttk.Checkbutton(onay_frame, text="Üçüncü Hal", variable=self.onay_d_2)
        onay_2.state(["alternate"])
        onay_2.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")

        onay_3 = ttk.Checkbutton(onay_frame, text="Pasif", state="disabled")
        onay_3.state(["disabled !alternate"])
        onay_3.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

    def radyo_butonlari(self):
        # Ayırıcı
        ayrac = ttk.Separator(self)
        ayrac.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="ew")

        # Radyo Butonları için Çerçeve Oluşturun
        radyo_frame = ttk.LabelFrame(self, text="Radyo Butonları", padding=(20, 10))
        radyo_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")

        # Radyo Butonları
        self.radyo_d = tk.IntVar(value=2)
        radyo_0 = ttk.Radiobutton(radyo_frame, text="Seçilmemiş", variable=self.radyo_d, value=1)
        radyo_0.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

        radyo_1 = ttk.Radiobutton(radyo_frame, text="Seçilmiş", variable=self.radyo_d, value=2)
        radyo_1.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

        radyo_2 = ttk.Radiobutton(radyo_frame, text="Pasif", state="disabled")
        radyo_2.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")

    def input_alanlari(self):
        # İnput Alanları için bir Çerçeve oluşturun
        inputlar_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
        inputlar_frame.grid(row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3)
        inputlar_frame.columnconfigure(index=0, weight=1)

        # Giriş Alanı
        giris_alani = ttk.Entry(inputlar_frame)
        giris_alani.insert(0, "Giriş Alanı")
        # giris_alani.state(["invalid"])
        giris_alani.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")
        giris_alani.focus()

        # Spin Kutusu
        spin_kutusu = ttk.Spinbox(inputlar_frame, from_=0, to=100, increment=0.1)
        spin_kutusu.insert(0, "Spin Kutusu")
        spin_kutusu.grid(row=1, column=0, padx=5, pady=10, sticky="ew")

        # Açılan Kutu
        acilan_kutu = ttk.Combobox(inputlar_frame, values=["Açılan Kutu", "Düzenlenebilir 1", "Düzenlenebilir 2"])
        acilan_kutu.current(0)
        acilan_kutu.grid(row=2, column=0, padx=5, pady=10, sticky="ew")

        # Okunabilir Açılan Kutu
        acilan_kutu_sabit = ttk.Combobox(inputlar_frame, state="readonly", values=["Okunabilir Açılan Kutu", "Öğe 1", "Öğe 2"])
        acilan_kutu_sabit.current(0)
        acilan_kutu_sabit.grid(row=3, column=0, padx=5, pady=10, sticky="ew")

        # Menü Buton için Menü
        menu = tk.Menu(self)
        menu.add_command(label="Menu Öğe 1")
        menu.add_command(label="Menu Öğe 2")
        menu.add_separator()
        menu.add_command(label="Menu Öğe 3")
        menu.add_command(label="Menu Öğe 4")

        # Menü Buton
        menu_boton = ttk.Menubutton(inputlar_frame, text="Menü Buton", menu=menu, direction="below")
        menu_boton.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")

        # Seçenek Menüsü
        self.secenek_d = tk.StringVar(value="")
        secenek_menusu = ttk.OptionMenu(inputlar_frame, self.secenek_d, *["", "Seçenek Menüsü", "Seçenek 1", "Seçenek 2"])
        secenek_menusu.grid(row=5, column=0, padx=5, pady=10, sticky="nsew")

        # Buton
        buton = ttk.Button(inputlar_frame, text="Buton")
        buton.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")

        # Vurgulu Butonu
        vurgulu_buton = ttk.Button(inputlar_frame, text="Vurgulu Butonu", style="Accent.TButton")
        vurgulu_buton.grid(row=7, column=0, padx=5, pady=10, sticky="nsew")

        # Geçiş Butonu
        gecis_buton = ttk.Checkbutton(inputlar_frame, text="Geçiş Butonu", style="Toggle.TButton")
        gecis_buton.grid(row=8, column=0, padx=5, pady=10, sticky="nsew")

        # Ayırıcı
        ayrac = ttk.Separator(inputlar_frame)
        ayrac.grid(row=9, column=0, padx=(20, 10), pady=10, sticky="ew")

        # Değiştirici
        switch = ttk.Checkbutton(inputlar_frame, text="Değiştirici", style="Switch.TCheckbutton")
        switch.grid(row=10, column=0, padx=5, pady=10, sticky="nsew")

        # Ayırıcı
        ayrac = ttk.Separator(inputlar_frame)
        ayrac.grid(row=11, column=0, padx=(20, 10), pady=10, sticky="ew")

        # Cetvel
        self.cetvel_degeri   = 75
        self.cetvel_degisken = tk.DoubleVar(value=self.cetvel_degeri)

        def deger_dondur(event):
            self.cetvel_degeri = self.cetvel_degisken.get()

            self.cetvel_degisken.set(self.cetvel_degeri)
            self.progress_text.config(text=f"Değer : {self.cetvel_degeri}")

        cetvel = ttk.Scale(inputlar_frame, to=100, from_=0, variable=self.cetvel_degisken, command=deger_dondur)
        cetvel.grid(row=12, column=0, padx=5, pady=10, sticky="nsew")

        # Progressbar
        progress = ttk.Progressbar(inputlar_frame, value=0, variable=self.cetvel_degisken, mode="determinate")
        progress.grid(row=13, column=0, padx=5, pady=10, sticky="nsew")

        # Progressbar Label
        self.progress_text = ttk.Label(inputlar_frame, text=f"Değer : {self.cetvel_degeri}")
        self.progress_text.grid(row=14, column=0, pady=5, sticky="s")

    def treeview_alani(self):
        # Treeview için Çerçeve Oluşturun
        treeview_frame = ttk.Labelframe(self, text="TreeView Log Alan")
        treeview_frame.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew", rowspan=1)

        # Scrollbar
        scrollbar = ttk.Scrollbar(treeview_frame)
        scrollbar.pack(side="right", fill="y")

        # Treeview
        treeview = ttk.Treeview(
            treeview_frame,
            selectmode     = "browse",
            yscrollcommand = scrollbar.set,
            columns        = (1),
            height         = 10,
            # show           = "tree"       # Başlıkları Gizlemek İçin
        )
        treeview.pack(expand=True, fill="both")
        scrollbar.config(command=treeview.yview)

        # Treeview Kolon
        treeview.column("#0", anchor="center", width=160)
        treeview.column(1,    anchor="center", width=60)

        # Treeview Başlık
        treeview.heading("#0", text="Zaman", anchor="center")
        treeview.heading(1,    text="Log",   anchor="center")

        loglar = [
            (0, datetime.now().strftime("%d-%m-%Y %X"), "Start")
        ]
        for satir in loglar:
            _index_id, _tarih, _olay = satir
            treeview.insert(parent="", index="end", iid=_index_id, text=_tarih, values=_olay)

        sahte_log = SahteLog(treeview)
        sahte_log.start()

    def sekme_alani(self):
        # Sekme Alanı için Çerçeve Oluşturun
        sekme_frame = ttk.Frame(self)
        sekme_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew", rowspan=3)

        # Notebook
        notebook = ttk.Notebook(sekme_frame)
        notebook.pack(fill="both", expand=True)

        # Tab #1
        tab_1 = ttk.Frame(notebook)
        for index in [0, 1]:
            tab_1.columnconfigure(index=index, weight=1)
            tab_1.rowconfigure(index=index, weight=1)
        notebook.add(tab_1, text="Tab 1")

        # Label
        tab_1_label = ttk.Label(
            tab_1,
            text    = "@keyiflerolsun",
            justify = "center",
            font    = ("-family", "JetBrainsMono NF", "-size", 15, "-weight", "bold"),
        )
        tab_1_label.grid(row=1, column=0, pady=10, columnspan=2)

        # Tab #2
        tab_2 = ttk.Frame(notebook)
        notebook.add(tab_2, text="Tab 2")

        # Tab #3
        tab_3 = ttk.Frame(notebook)
        notebook.add(tab_3, text="Tab 3")

        # Tab #4
        tab_4 = ttk.Frame(notebook)
        notebook.add(tab_4, text="Tab 4")

def pencereyi_kapat():
    if messagebox.askokcancel("Program Kapanıyor", "Bunu Yapmak İstediğine Emin Misin?"):
        _dur_event.set()
        pencere.destroy()

def tam_ekran():
    pencere.attributes("-fullscreen", not pencere.attributes("-fullscreen"))

    if pencere.attributes("-fullscreen"):
        uygulama.sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))        
    else:
        uygulama.sizegrip.grid_forget()

if __name__ == '__main__':
    pencere = tk.Tk()

    # Pencere Kapanmadan Önce Fonksiyon Tetiklemek
    pencere.protocol("WM_DELETE_WINDOW", pencereyi_kapat)

    # Pencere Özellikleri
    pencere.title("keyiflerolsun GUI")
    pencere.bind("<Escape>", lambda event: pencereyi_kapat()) # ESC ile çıkış
    pencere.bind("<F11>",    lambda event: tam_ekran())       # Tam Ekran

    # Pencere İkonu
    logo_b64 = encodebytes(open("logo.png", "rb").read())
    favicon  = tk.PhotoImage(data=logo_b64)
    pencere.iconphoto(False, favicon)       # Pencere İkonu
    # pencere.tk.call('wm', 'iconphoto', pencere._w, tk.PhotoImage(file='fav2.ico')) # Pencere İkonu

    # Pencere Ek Özellikleri
    # pencere.attributes("-topmost", True)    # Her Zaman Diğer Pencelerin Üstüne Çık
    # pencere.configure(background='#ffffff') # Renk
    # pencere.attributes("-alpha", 0.9)       # Pencere Şeffaflığı

    # Temayı Ayarlayın
    pencere.tk.call("source", "Temalar/Temalar.tcl")
    pencere.tk.call("set_theme", "Sun-Valley_dark")

    # Uygulamamıza Pencerimize Ekleyelim
    uygulama = Uygulama(pencere)
    uygulama.pack(fill="both", expand=True)

    # Pencere için bir minimum boyut ayarlayın ve ortasına yerleştirin
    pencere.update()
    p_genislik  = max(pencere.winfo_width(), 200)
    p_yukseklik = max(pencere.winfo_height(), 200)
    pencere.minsize(p_genislik, p_yukseklik)
    x_kordinat = int((pencere.winfo_screenwidth()  / 2) - (p_genislik  / 2))
    y_kordinat = int((pencere.winfo_screenheight() / 2) - (p_yukseklik / 2))
    pencere.geometry(f"+{x_kordinat}+{y_kordinat - 20}")

    # Pencereyi Gösterin
    pencere.mainloop()
