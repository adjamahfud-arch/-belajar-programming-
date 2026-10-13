import json
from datetime import datetime

import validation as ls

NAMA_FILE ="data_.json"
format_waktu ="%H:%M %d %A %Y"

class Users:
   def __init__(self,waktu,masuk,keluar,uang=0):
       self.waktu =waktu
       self.masuk =masuk
       self.keluar =keluar
       self.uang = uang
   @classmethod
   def from_dict(cls,data):
       data_ =cls(data["waktu"],data["masuk"],data["keluar"],data["uang"])
       return data_
   def to_dict(self):
       return {
         "waktu":self.waktu,
         "masuk":self.masuk,
         "keluar":self.keluar,
         "uang":self.uang
       }
   def tambah_data(self,data):
       self.uang += data
     
class Program:
   def __init__(self,file_path):
       self.file =file_path
       self.data_center =self.load()
   def load(self):
       try:
         with open(self.file,"r",encoding="utf-8") as file:
              data_semen =json.load(file)
              return [Users.from_dict(x) for x in data_semen]
           
       except FileNotFoundError:
             return []
       except Exception as i:
             print(f"error:{i}")
             return []
   def simpan(self):
       try:
         with open(self.file,"w",encoding="utf-8") as file:
              data_m =[y.to_dict() for y in self.data_center]
              json.dump(data_m,file,indent=4)
              print("data berhasil di simpan")
       except Exception as l:
            print(f"error:{l}")
   def tambah(self,data):
       self.data_center.append(data)
   #menambah uang masuk,keluar, dan menjumlah uang masuk
   def isi(self,waktu,masuk,keluar):
       try:
         if self.data_center:
            total =self.data_center[-1].uang
         else:
            total = 0
         user =Users(waktu,masuk,keluar)
         hasil =total + masuk
         user.tambah_data(hasil)
         self.tambah(user)
         self.simpan()
       except Exception as e:
           print(f"error:{e}")
         
     
   #sistem penampil data
   def tampilkan(self):
       if len(self.data_center) ==0:
          print("data belum ada")
          return
       dtal =self.data_center[-1]
       print(f"{dtal.masuk:<12} | {dtal.keluar:12} | {dtal.uang}")
   def kurangi(self,kurang):
       if self.data_center:
          data =self.data_center[-1].uang
          kurangi =data - kurang
          self.data_center[-1].uang =kurangi
          self.simpan()
          

class Waktu:
    @staticmethod
    def timel():
        times =datetime.now().strftime(format_waktu)
        return times
   
#input Program
def main():
   sk =Waktu()
   sy =Program(NAMA_FILE)
   while True:
       msk =ls.masuk()
       klr =ls.keluar()
       timep =sk.timel()
       pilih_2 =ls.tampil()
       sy.isi(timep,msk,klr)
       if pilih_2 == "Y":
          sy.tampilkan()
      
       pilihlah =ls.pilihan()
       if pilihlah =="ya":
          kurangi_ =ls.kurang()
          sy.kurangi(kurangi_)   
       pilihan_ =ls.pilih()
       if pilihan_ =="y":
          continue
       elif pilihan_ =="n":
            break
       else:
          continue
   print("terimakasih (:")
if __name__ =="__main__":
   main()
      
      
    
  

     
       