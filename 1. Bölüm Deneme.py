from tkinter import *
from tkinter import messagebox
from docx import Document
import os

# Bilirkişi raporu oluşturma fonksiyonu
def bilirkisi_raporu():
    # Uyuşmazlık konusuna göre sonuç metni oluştur
    result_text = "Bilirkişi Raporu\n\n"
    result_text += f"Uyuşmazlık Konusu: {uyusmazlik_konusu.get()}\n"

    if uyusmazlik_konusu.get() == "Trafik DK":
        result_text += f"Sigortalı araç plakası: {sigortali_plaka_entry.get()}\n"
        result_text += f"Başvurucuya ait araç plakası: {basvuran_plaka_entry.get()}\n"
        result_text += f"Kaza tarihi: {kaza_tarihi_entry.get()}\n"
        result_text += f"\nSigorta Tahkim Komisyon Başkanlığı tarafından Heyetimize intikal ettirilen uyuşmazlık, davalı sigorta kuruluşuna zorunlu mali sorumluluk sigortalı \"{sigortali_plaka_entry.get()}\" plakalı araç ile başvurucuya ait \"{basvuran_plaka_entry.get()}\" plakalı araç arasında \"{kaza_tarihi_entry.get()}\" tarihinde gerçekleşen trafik kazası sonucu başvurucuya ait araçta oluşan değer kaybı tutarının tazmini amacıyla Komisyona yapılan başvuruda Uyuşmazlık Hakemince verilen Karara davalı sigorta kuruluşunun itirazlarına ilişkindir."

    result_text += f"\n\nİnceleme süresi: {intikal_sureci.get()}\n"

    if intikal_sureci.get() == "Doğrudan hüküm":
        result_text += "\nUyuşmazlık Hakemi Kararına davalı sigorta kuruluşu vekilinin itirazları Komisyon nezdinde öncelikle İtiraz Yetkilisi tarafından incelenmiş ve itirazın süresinde ve usulüne uygun şekilde yapıldığı tespit edildiğinden, davalının itirazlarının değerlendirilmesi ve uyuşmazlığın çözümü için dosya İtiraz Hakem Heyetimize intikal ettirilmiştir.\n\nHeyetimizce yapılan incelemede, dosyada mevcut bilgi ve delillerin uyuşmazlık ve itirazlar konusunda bir kanaate ulaşabilmek için yeterli olduğu kanaatine ulaşılmış ve doğrudan hüküm kurulması yoluna gidilmiştir.\n\nHeyetimizce davalı vekilinin itirazlarına ilişkin olarak karara varılmış ve yargılamaya son verilmiştir."

    # Word dosyasını oluştur ve kaydet
    doc = Document()
    doc.add_paragraph(result_text)
    # Dosya yolunu belirle
    dosya_yolu = os.path.join("C:\\Users\\Beyza\\Desktop", "Bilirkisi_Raporu.docx")
    doc.save(dosya_yolu)

    # Bilgilendirme mesajı
    messagebox.showinfo("Bilgilendirme", f"Bilirkişi raporu oluşturuldu: {dosya_yolu}")

def uyusmazlik_goster():
    # İlgili alanları göster
    if uyusmazlik_konusu.get() == "Trafik DK":
        sigortali_plaka.grid(row=2, column=0, sticky=W)
        sigortali_plaka_entry.grid(row=2, column=1)
        basvuran_plaka.grid(row=3, column=0, sticky=W)
        basvuran_plaka_entry.grid(row=3, column=1)
        kaza_tarihi.grid(row=4, column=0, sticky=W)
        kaza_tarihi_entry.grid(row=4, column=1)
    else:
        sigortali_plaka.grid_remove()
        sigortali_plaka_entry.grid_remove()
        basvuran_plaka.grid_remove()
        basvuran_plaka_entry.grid_remove()
        kaza_tarihi.grid_remove()
        kaza_tarihi_entry.grid_remove()

    intikal_sureci_goster()

def intikal_sureci_goster():
    # İnceleme süresi seçeneklerini göster
    intikal_sureci_label.grid(row=5, column=0, sticky=W)
    for idx, option in enumerate(intikal_secenekleri):
        intikal_sureci_radiobuttons[idx].grid(row=6 + idx, column=0, sticky=W)

    gonder_butonu.grid(row=6 + len(intikal_secenekleri), column=1, sticky=W, pady=4)

# Ana pencereyi oluştur
root = Tk()
root.title("Bilirkişi Raporu")

# Uyuşmazlık Konusu
uyusmazlik_konusu = StringVar()
uyusmazlik_konusu.set("Trafik DK")
Label(root, text="Uyuşmazlığın Konusu:").grid(row=0, column=0, sticky=W)
uyusmazlik_secenekleri = ["Trafik DK", "Trafik Hasar", "Trafik DK ve Hasar", "Kasko", "Trafik SİGT", "Trafik DYKT",
                          "İMM", "Zorunlu Deprem", "Diğer"]
for idx, option in enumerate(uyusmazlik_secenekleri):
    Radiobutton(root, text=option, variable=uyusmazlik_konusu, value=option, command=uyusmazlik_goster).grid(
        row=idx + 1, column=0, sticky=W)

# Trafik DK seçeneği için input alanları (Başlangıçta gizli)
sigortali_plaka = Label(root, text="Sigortalı araç plakası:")
sigortali_plaka_entry = Entry(root)

basvuran_plaka = Label(root, text="Başvurucuya ait araç plakası:")
basvuran_plaka_entry = Entry(root)

kaza_tarihi = Label(root, text="Kaza tarihi (DD/MM/YYYY):")
kaza_tarihi_entry = Entry(root)

# İnceleme süresi seçenekleri (Başlangıçta gizli)
intikal_sureci = StringVar()
intikal_sureci.set("Doğrudan hüküm")
intikal_sureci_label = Label(root, text="İnceleme süresi:")
intikal_secenekleri = ["Doğrudan hüküm", "Taraflardan belge isteme sonrası hüküm", "Bilirkişi tayini sonrası hüküm",
                       "Yeni Rapor istenilmesi sonrası hüküm", "Yeni Rapor istenilmesi ve BK tayini sonrası hüküm"]
intikal_sureci_radiobuttons = [Radiobutton(root, text=option, variable=intikal_sureci, value=option) for option in
                               intikal_secenekleri]

gonder_butonu = Button(root, text='Gönder', command=bilirkisi_raporu)

root.bind('<Return>', lambda event=None: gonder_butonu.invoke())  # Enter tuşu ile gonder_butonu'nu çağır

root.mainloop()
