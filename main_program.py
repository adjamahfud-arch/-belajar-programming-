import json
from datetime import datetime
import validation as ls

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
   @staticmethod
   def waktu():
       times =datetime.now().strftime("%H:%M %d %A %Y")
       return times
     
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

class Waktu:
    @staticmethod
    def timel():
        times =datetime.now().strftime("%H:%M %d %A %Y")
        return times
   
#input Program
sk =Waktu()
sy =Program("data_.json")
if __name__=="__main__":
   while True:
      msk =ls.masuk()
      klr =ls.keluar()
      timep =sk.timel()
      pilih_2 =ls.tampil()
      sy.isi(timep,msk,klr)
      if pilih_2 == "Y":
         sy.tampilkan()
      pilihan =ls.pilih()
      if pilihan =="y":
         continue
      elif pilihan =="n":
           break
      else:
         continue
print("terimakasih (:")

      
      
    
  

     
       