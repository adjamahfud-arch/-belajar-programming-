def masuk():
    while True:
       try:
         masuk_ =input("uang masuk:").strip()
         if masuk_ =="":
            return 0
           
         if not masuk_.isdigit():
            print(f"data {masuk_} mengandung huruf!")
            continue
      
         masuk =int(masuk_)
         return masuk
       except Exception as e:
            print(f"error:{e}")
         
def keluar():
    while True:
       try:
         keluar =input("uang keluar:").strip()
         if keluar =="":
            return 0
           
         if not keluar.isdigit():
            print("isian harus di isi dengan angka!")
            continue
           
         keluar_ =int(keluar)
         return keluar_
       except Exception as p:
            print(f"error:{p}")

def pilih():
    while True:
       try:
         pilih =str(input("masukan lagi Y/N:")).lower()
         if pilih =="":
            print("pilihan wajib di isi")
            continue
         if pilih.isdigit():
            print("pilihan harus berupa huruf")
            continue
         return pilih
       except Exception as e:
            print(f"error:{e}")
         
def tampil():
    while True:
       try:
         ui =str(input("tampilkan data?Y/N")).upper().strip()
         if ui =="":
            print("pilihan di atas wajib di isi!")
            continue
         if not ui.isalpha():
            print("harus di isi degan hiruf!")
            continue
         return ui
       except Exception as l:
           print(f"error{l}")
      
         
if __name__ =="__main__":
   tampil()
  
     
   