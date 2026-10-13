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
def pilihan():
    while True:
        try:
          pilih_ =input("mau mengurangi total:ya/n:").strip().lower()
          if pilih_ =="":
             print("pilihan harus di isi!")
             continue
          if pilih_.isdigit():
             print("pilihan harus berupa huruf")
             continue
          if  not pilih_ in ["ya","n"]:
              print("pilihan hanya boleh di isi ya dan n")
              continue
          return pilih_
        except Exception as o:
            print(f"error:{o}")

def kurang():
    while True:
        try:
          kurang =input("masukan jumlah yang mau di kurang:").strip()
          if kurang =="":
             print("pilihan tidak boleh kosong!")
             continue
          if  not kurang.isdigit():
              print(f"{kurang} wajib di isi dengan angka")
              continue
          
          
          ubl =int(kurang)
          if ubl <= 0:
             print("tidak boleh 0")
             continue
          return ubl
        except ValueError:
            print("kode mengalami error")
            continue
        except Exception as d:
            print(f"error {d}")
          
            
          
if __name__ =="__main__":
   kurang()
  
     
   