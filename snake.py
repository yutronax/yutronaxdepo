import cv2
import random
import sys
import numpy as np

sys.setrecursionlimit(1500)
class snake:
  
  def __init__(self):
    self.x1=250
    self.y1=250
    self.x2=250
    self.y2=250
    self.boyut=7
    self.miktar=0
    self.xmeyve=random.randint(0,51)*10
    self.ymeyve=random.randint(0,51)*10
    self.xengel=random.randint(0,51)*10
    self.yengel=random.randint(0,51)*10
    self.resim2=cv2.imread("indir.jpeg")
    self.engel=[]
    self.son=None
    self.recursion_counter=0
    self.skorresim=cv2.imread("indir.jpeg")
    
    
  def oyunkontrol(self):
    self.goster=cv2.imshow("bulut",self.resim2)
    while True:
        

        tus=cv2.waitKey(0)

        if tus==ord("w"):
           self.wkontrol()
            
        elif tus==ord("s"):
         self.skontrol()

        elif tus==ord("a"):            
          self.akontrol()
            
        elif tus==ord("d"):
          self.dkontrol()
        elif tus==ord("q"):
         cv2.destroyAllWindows()
       
  def oyun(self):
                
                self.recursion_counter += 1
                if self.recursion_counter > 1400: 
                    self.recursion_counter = 0 
                    self.reset_window()
                    
                self.resim2=cv2.imread("indir.jpeg")   
                self.skorresim=cv2.imread("indir.jpeg")
                self.skorresim=cv2.resize(self.skorresim,(512,512))
                cv2.putText(self.skorresim,f"Skor :{str(self.miktar)}",(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
                self.resim2=cv2.resize(self.resim2,(512,512))              
                self.cisim=cv2.line(self.resim2,(self.x1,self.y1),(self.x2,self.y2),(0,0,255),self.boyut)
                self.meyve=cv2.line(self.resim2,(self.xmeyve,self.ymeyve),(self.xmeyve,self.ymeyve),(0,255,0),5)
                
                
                if self.x2==self.xmeyve and self.y2==self.ymeyve:
                    self.xmeyve=random.randint(0,51)*10
                    self.ymeyve=random.randint(0,51)*10
                    self.miktar+=5
                    
                                  
                    self.xengel = random.randint(0, 51) * 10
                    self.yengel = random.randint(0, 51) * 10
                    self.engel.append((self.xengel,self.yengel))
                   
                for (self.m,self.n) in self.engel:
                     i=cv2.line(self.resim2, (self.m,self.n), (self.m,self.n), (0, 0, 255), 7)
                
                for (self.m,self.n) in self.engel:   
                    if self.xmeyve==self.m and self.ymeyve==self.n:
                                self.ymeyve=random.randint(0,51)*10
                                self.xmeyve<=random.randint(0,51)*10
                    elif self.x2==self.m  and self.y2==self.n:
                            self.miktar-=1
                            if self.son=="w":
                                self.y2+=20
                                self.y1+=20
                            elif self.son=="s":
                                self.y2-=20
                                self.y1-=20
                            elif self.son=="a":
                                self.x2+=20
                                self.x1+=20
                            elif self.son=="d":
                                self.x2-=20
                                self.x1-=20
                
                buyukresim=np.vstack((self.resim2,self.skorresim))
                cv2.imshow("bulut",buyukresim)
                key=cv2.waitKey(100)& 0xFF
                if key==ord("s"):
                    self.son="s"
                    
                    self.skontrol()
                    

                    

                elif key==ord("w"):
                    self.son="w"
                    
                    
                  
                    
                    self.wkontrol()

                    
                elif key==ord("a"):
                    self.son="a"
                    
                    
                    self.akontrol()
                elif key==ord("d"):
                    self.son="d"
                   
                    self.dkontrol()


                elif key==ord("q"):
                   self.oyunkontrol()
 
      

  def wkontrol(self):
    while True:
                    self.y1-=10
                    self.y2-=10
                    if self.y2<0:
                        self.y1=510
                        self.y2=510
                    self.oyun()
                    
  def skontrol(self):
       while True:
            
            self.y1+=10
            self.y2+=10
            if self.y2>510:
                self.y2=0
                self.y1=0 
            self.oyun()
 
  def akontrol(self):
       while True:
            self.x2-=10
            self.x1-=10
            if self.x2<0:
                self.x2=510
                self.x1=510
            self.oyun()
            
  def dkontrol(self):
        while True:
            cv2.imread("indir.jpeg")
            self.x2+=10
            self.x1+=10
            if self.x2>510:
                self.x2=0
                self.x1=0
            self.oyun()
 
  def reset_window(self):
        cv2.destroyAllWindows()

        self.oyunkontrol()
  
      


        
            


        
        
 
oyun1=snake()
oyun1.oyunkontrol()
