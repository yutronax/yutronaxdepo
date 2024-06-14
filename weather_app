from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QComboBox, QApplication, QMainWindow, QLabel,QListWidget,QWidget, QVBoxLayout, QPushButton, QLineEdit
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from selenium.webdriver.chrome.options import Options
import sys
import time
import requests
from selenium.webdriver.common.by import By
from PyQt5.QtGui import QIcon

import re
from PyQt5.QtSvg import QSvgWidget
import threading
app = QApplication(sys.argv)
global metin
global hava
global event
global driver
class havadurumu():
    
    def __init__(self):
        self.num=0
        self.driver = None
        self.gecmısarama=[]
        self.win = None
        self.genelpencere = None 
        self.tahmin = None
        self.surucu = None
        self.gunsirasi=[]
        self.tarihlistesi=[]
        
    def haritaresmi(self):
      try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.surucu=webdriver.Chrome(options=options)
        self.surucu.minimize_window()
        self.surucu.get("https://www.mgm.gov.tr/tahmin/turkiye.aspx")
        
       
        for i in range(1,6):
         tarih= WebDriverWait(self.surucu,10).until(EC.presence_of_element_located(("xpath",f"//a[@href='?g={i}#sfB']"))).text
         WebDriverWait(self.surucu,10).until(EC.presence_of_element_located(("xpath",f"//a[@href='?g={i}#sfB']"))).click()
         
         
         
         image=WebDriverWait(self.surucu,10).until(EC.presence_of_element_located(("xpath",".//img[@id='cph_body_haritabuyukTek']"))).get_attribute("src")
         print(self.gunsirasi)
         self.tarihlistesi.append(tarih)
         
         yerlestır=requests.get(image)
         resımadı=f"havadurumu{i}.jpg"
         with open(resımadı,"wb") as file:
             file.write(yerlestır.content)
         self.gunsirasi.append(f"havadurumu{i}.jpg")
       

        
      except Exception as e:
         print("Hata",e)
      finally:
         self.win.close()
         
         self.turkiyegeneli()
         
           

                               

        
    
    def button(self):
       self.girdi()
       self.kapa()

    def button2(self):
       self.yok.close()
       self.girdi()
    def button3(self):
       self.gec.close()
       self.girdi()
        
       
    def kapa(self):
        self.hava.close()       
    def kapa2(self):
       self.win.close() 
    
   
    def girdi(self):
        self.win = QMainWindow()
        self.win.setGeometry(100, 100, 300, 300)
        self.win.setWindowTitle('Ana Pencere') 
        self.win.move(800, 350)
        
        # arama alanı 
        self.arama = QLabel(self.win)
        self.arama.setText("Şehir Adı giriniz")
        self.arama.move(100, 50)
        self.arama.setFixedSize(100, 50)

        self.aranan = QLineEdit(self.win)
        self.aranan.move(100, 100)
        self.aranan.setFixedSize(126, 50)
        self.aranan.returnPressed.connect(self.aramamotoru)
        self.aranan.returnPressed.connect(self.gecmiseyukle)
        self.aranan.textChanged.connect(self.degisim)
        
        self.sehirler = [
            "Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Aksaray", "Amasya", "Ankara", "Antalya",
            "Ardahan", "Artvin", "Aydın", "Balıkesir", "Bartın", "Batman", "Bayburt", "Bilecik", 
            "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", 
            "Denizli", "Diyarbakır", "Düzce", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", 
            "Gaziantep", "Giresun", "Gümüşhane", "Hakkari", "Hatay", "Iğdır", "Isparta", "İstanbul", 
            "İzmir", "Kahramanmaraş", "Karabük", "Karaman", "Kars", "Kastamonu", "Kayseri", 
            "Kırıkkale", "Kırklareli", "Kırşehir", "Kilis", "Kocaeli", "Konya", "Kütahya", 
            "Malatya", "Manisa", "Mardin", "Mersin", "Muğla", "Muş", "Nevşehir", "Niğde", 
            "Ordu", "Osmaniye", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", 
            "Şanlıurfa", "Şırnak", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Uşak", "Van", 
            "Yalova", "Yozgat", "Zonguldak"
        ]

        self.gecmisbutton = QPushButton(self.win)
        self.gecmisbutton.setText("Geçmiş")
        self.gecmisbutton.move(200, 0)
        self.gecmisbutton.setFixedSize(100, 50)
        self.gecmisbutton.clicked.connect(self.gecmis)

        self.genelbutton=QPushButton(self.win)
        self.genelbutton.setText("harita")
        self.genelbutton.move(100, 0)
        self.genelbutton.setFixedSize(100, 50)
        self.genelbutton.clicked.connect(self.haritaresmi)

        self.aramabutonu = QPushButton(self.win)
        self.aramabutonu.setText("ARA")
        self.aramabutonu.move(100, 160)
        self.aramabutonu.setFixedSize(50, 50)
        self.aramabutonu.clicked.connect(self.aramamotoru)
        self.aramabutonu.clicked.connect(self.gecmiseyukle)
        widget = QWidget(self.win) 
        widget.setGeometry(88, 125,150,55)
        
      
        
        self.tahmin = QListWidget(self.win)
        self.tablo2 = QVBoxLayout(widget)
        self.tablo2.addWidget(self.tahmin)
      
        self.tahmin.itemClicked.connect(self.arayanmotoru2)  
       
        self.win.show()

      
    
    def turkiyegeneli(self): 
       
       
       
       self.genelpencere=QMainWindow()
       self.genelpencere.setGeometry(500,700,800,800)
       self.genelpencere.move(800,350)
       self.genelpencere.setWindowTitle("Türkiye Geneli")
       self.havaresmi=QLabel(self.genelpencere)
       self.havaresmi.move(100,0)
       self.havaresmi.setFixedSize(500,400)
       self.ileritus=QPushButton(self.genelpencere)
       self.ileritus.move(250,450)
       self.ileritus.setFixedSize(200,50)
       self.geridon=QPushButton(self.genelpencere)
       self.geridon.move(100,450)
       self.geridon.setFixedSize(100,50)
       self.geridon.setText("Geri Dön")
       self.geridon.clicked.connect(lambda x:self.girdi())
       self.geridon.clicked.connect(lambda y:self.genelpencere.close())
       resmim=QPixmap(self.gunsirasi[self.num])
       self.havaresmi.setPixmap(resmim.scaled(500,400))
      
       
       self.geritus=QPushButton(self.genelpencere)
       self.geritus.move(250,450)
       self.geritus.setFixedSize(200,50)

       self.geritus.setText(f"{self.tarihlistesi[self.num-1]}")
       self.ileritus.setText(f"{self.tarihlistesi[self.num]}")


       
       

      
       self.ileritus.clicked.connect(self.ileri)
       self.geritus.clicked.connect(self.geri)
       self.genelpencere.show()
    def ileri(self): 
          self.num+=1
          if self.num>4:
             self.num=0
          resmim=QPixmap(self.gunsirasi[self.num])
          self.ileritus.setText(f"{self.tarihlistesi[self.num]}")
          self.havaresmi.setPixmap(resmim.scaled(500,400))
          self.geritus.setText(f"{self.tarihlistesi[self.num-1]}")

      
             

         
          
    def geri(self):
         self.num-=1
         
         if self.num<0:
             self.num=4
         
         resmim=QPixmap(self.gunsirasi[self.num])
         self.geritus.setText(f"{self.tarihlistesi[self.num-1]}")
         self.havaresmi.setPixmap(resmim.scaled(500,400))
         self.ileritus.setText(f"{self.tarihlistesi[self.num]}")
         
       
         

         
    def degisim(self, text):
        

        self.tahmin.clear()
        for sehir in self.sehirler:
            if re.search(text,sehir,re.IGNORECASE):
                self.tahmin.addItem(sehir)
          
   
       
    def gecmiseyukle(self):
       self.gecmısarama.append(str(self.aranan.text()))
       
       
    def gecmis(self):
       
       self.win.close()

       
       self.gec=QMainWindow()
       self.gec.setGeometry(300,300,500,500)
       self.gec.move(800,350)
       self.gec.setWindowTitle("hava durumu geçmiş aramalar")
      
       self.gecmısmetin=QLabel(self.gec)
       self.gecmısmetin.setText("GEÇMİŞ ARAMALAR")
       self.gecmısmetin.move(100,0)
       self.gecmısmetin.setFixedSize(200,100)

       self.gecmisliste=QListWidget(self.gec)
       
       self.gecmisliste.setFixedSize(250,500)
       self.gecmisliste.move(100,100)
       self.gecmisliste.clear()

       self.gecmisliste.addItems(self.gecmısarama)
       self.gecmisliste.itemClicked.connect(self.arayanmotoru)
       self.tablom=QVBoxLayout(self.gec)
       self.tablom.addWidget(self.gecmisliste)

       
       self.geridon=QPushButton(self.gec)
       self.geridon.setText("GERİ DÖN")
       self.geridon.move(400,100)
       self.geridon.setFixedSize(100,50)
       self.geridon.setStyleSheet("background-color:red")
       self.geridon.clicked.connect(self.button3)
       
       
       
       self.gec.show()
 
       

    def sonucbulunamadı(self):
       
       self.win.close()
       self.yok=QMainWindow()
       self.yok.setGeometry(100, 100, 300, 300)
       self.yok.move(800,350)
       
       self.yok.setWindowTitle('Hava Durumu')
       self.sonucyok=QLabel(self.yok)
       self.sonucyok.setText("Sonuç Bulunamadı")
       self.sonucyok.move(100,50)
       self.sonucyok.setFixedSize(200,50)
       self.geridon=QPushButton(self.yok)
       self.geridon.setText("GERİ DÖN")
       self.geridon.move(100,100)
       self.geridon.setFixedSize(100,50)
       self.geridon.setStyleSheet("background-color:red")
       self.geridon.clicked.connect(self.button2)
       self.yok.show()

     
    
      

    def aramamotoru(self):
     
       
     
     if self.aranan.text()== "" or re.search("\d+",self.aranan.text()):
          self.sonucbulunamadı()
        
     else:
       try:
       
        
  
     
      
      
        
       
        self.driver=webdriver.Chrome()
        
        
      
        self.driver.minimize_window()
        url="https://www.accuweather.com"
        self.driver.get(url)
       
       

        arama=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@class='search-input']")))
        arama.send_keys(f"{self.aranan.text().capitalize()},"*2,Keys.ENTER)
        
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        
        self.gun=WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located(("xpath",".//a[@class='daily-list-item ']/div[1]/p[1]")))
        if  self.gun:
      
         self.sıcaklık=WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located(("xpath",".//a[@class='daily-list-item ']/div[2]/div/span[1]")))
         self.havadurumu=WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located(("xpath",".//a[@class='daily-list-item ']/div[3]/p")))
         self.yagıs=WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located(("xpath",".//a[@class='daily-list-item ']/div[4]")))

         self.metin=[]
         self.ayrıntım=[]
         for i in range(len(self.gun)):
            
            self.metin.append(f"{self.gun[i].text}")
            self.ayrıntım.append(f" hava sıcaklığı: {str(self.sıcaklık[i].text)} \n hava durumu: {self.havadurumu[i].text} \n yağış oranı : {self.yagıs[i].text}")
            

         
         self.sonuc()
        else:
                
                self.driver.close()
                self.driver.quit()
       except Exception as e:
        print("Hata",e)
        self.sonucbulunamadı()
       finally:
        if self.driver:
             self.driver.quit()
        self.win.close()
    def arayanmotoru(self,current):
       self.aranan.setText(current.text())
       self.gec.close()
       self.aramamotoru() 
    def arayanmotoru2(self,item):
         self.aranan.setText(item.text())
         print(item.text())
         self.aramamotoru()
    def sonuc(self):
        x=150
        self.hava=QMainWindow()
        
        self.tablo=QListWidget(self.hava)
        self.tablo.addItems(self.metin)
        self.tablo.move(75,150)
        self.tablo.itemClicked.connect(self.ayrinti)
        self.tablo.setFixedSize(500,200)
        self.havametinkutusu=QVBoxLayout(self.hava)
        self.havametinkutusu.addWidget(self.tablo)
        
        
        self.il=QLabel(self.hava)
        self.il.setText(self.aranan.text().upper())
        
        self.il.move(50,50)
        self.il.setFixedSize(500,50)
        self.hava.setGeometry(750, 750, 750, 750)
        self.hava.move(300,200)
        self.hava.setWindowTitle("hava durumu")
        
        
        
        
        self.geridon=QPushButton(self.hava)
        self.geridon.setText("GERİ DÖN")
        
        self.geridon.setFixedSize(100,50)
        self.geridon.clicked.connect(self.button) 
         
        
        for i in range(len(self.metin)):
           
           x=x+25
        
        self.geridon.move(100,x)
        self.hava.show()
    
    def ayrinti(self,item):
      

     
       self.pencere=QMainWindow()
      
       self.pencere.setGeometry(750, 750, 750, 750)
       self.pencere.move(1050,200)
       self.pencere.setWindowTitle("hava durumu ")
       
       self.il=QLabel(self.pencere)
       self.il.setText(self.aranan.text().upper())
        
       self.il.move(50,50)
       self.il.setFixedSize(500,50)
       self.gun=QLabel(self.pencere)
       self.gun.setText(f"{item.text()}")
    
       
       listesayısı=self.tablo.row(item)
       self.gun.move(50,100)
       self.gun.setFixedSize(200,50)
       self.goster=self.ayrıntım[int(listesayısı)]
       gosterın=QLabel(self.pencere)
       gosterın.setText(self.goster)
       gosterın.move(50,150)
       gosterın.setFixedSize(750,100)
       resim_label = QLabel(self.pencere)
       resim_pixmap = QPixmap()
      
       if re.search("güneşli|güneş", self.goster,re.IGNORECASE) or re.search("çok sıcak|açık", self.goster,re.IGNORECASE) :
            resim_pixmap.load("sun.png")
       elif re.search("yağmur|sağanak", self.goster,re.IGNORECASE) :
           resim_pixmap.load("rain.png")
       elif re.search("bulutlu", self.goster,re.IGNORECASE):
            resim_pixmap.load("cloud.png")
       elif re.search("kar|kar yağış", self.goster,re.IGNORECASE) or re.search("soğuk", self.goster,re.IGNORECASE):
            resim_pixmap.load("snow.png")
       resimayar= resim_pixmap.scaled(100,100)
       resim_label.setPixmap(resimayar)
       resim_label.move(600, 100)
       resim_label.setFixedSize(200, 200)

         
        
      
       self.pencere.show()
    

   

        
    
    


     
        
   
        
    


calıstır=havadurumu()
calıstır.girdi()
sys.exit(app.exec_())  


