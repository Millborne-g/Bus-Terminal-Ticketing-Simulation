# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'STart.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import time
import pygame
import time
from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets
#
from end import Ui_ResultWindow
pygame.init()
class Ui_MainWindow(object):
    def end(self):
       # app = QtWidgets.QApplication(sys.argv)
        #Dialog = QtWidgets.QDialog()
        #ui = Ui_Dialog()
        #ui.setupUi(Dialog)
        #Dialog.show()
        #sys.exit(app.exec_())
        self.window = QtWidgets.QMainWindow()  
        self.ui = Ui_ResultWindow()
        
        self.ui.setupUi(self.window)
        #self.ui.retranslateUi_1(self.Resultbus_1,self.Resultbus_2,self.Resultbus_3,self.Resultbus_4,self.Resultbus_5)
        self.ui.process(self.busTotal_1,self.busTotal_2,self.busTotal_3,self.busTotal_4,self.busTotal_5,self.Resultbus_1,self.Resultbus_2,self.Resultbus_3,self.Resultbus_4,self.Resultbus_5)
        #self.ui.retranslateUi(self.window)
        MainWindow.hide()
        self.window.show()
        
        #sys.exit(app.exec_())
    def check(self):
        
        if self.textEdit.toPlainText() == '' or self.textEdit_2.toPlainText()== '*Input Destination':
            self.label.setText('*Input Destination')
        elif self.textEdit_2.toPlainText()== '' or self.textEdit_2.toPlainText()=='*Input fare':
            self.label.setText('        *Input fare')
        else:
            self.label.setText('ENTER 5 DESTINATIONS')
            self.Destination_Count -= 1
            self.label_3.setText(str(self.Destination_Count))
            if self.Destination_Count == 0:
                self.destination.append(self.textEdit.toPlainText())
                self.fares.append(self.textEdit_2.toPlainText())
                self.textEdit.setEnabled(False)
                self.textEdit_2.setEnabled(False)
                self.textEdit.setText('')
                self.textEdit_2.setText('')
                self.pushButton.setText('PROCESSESING.....')
                time.sleep(2)
                #import FinalPaynal
                width = 1200
                height = 600
    
                win =pygame.display.set_mode((width, height))
                pygame.display.set_caption("Paynal")
                background = pygame.image.load('FinalBackground.png')
                
                names = ['Ariel','Bob','Cassy','Del','El','Frank','Gil','Her','Bill','John','Kan','Lem','Mill','Nancy','Op','Pat','Quill','Rhan','Sef','Tang']
                ForTable= []
                ForInOut= []
                ForPayment= []
                ForDestination= []
                
                run = True
                
                def FinalPaynal(a, b):
                    bus=[]
                    bus = a
                    print(bus)
                        
                
                
                class Queue:
                    def __init__(self):
                        self.elements = []
                        
                    # return True if the stack is empty, False otherwise. 
                    def isEmpty(self):
                        return self.elements==[]  # or   len(self.elements)==0
                            
                    # return the number of elements in the stack.
                    def size(self):
                        return len(self.elements)
                    
                    # inserts/adds a new element at the REAR of the Queue
                    def enqueue(self,new_item):
                        self.elements.append(new_item)  # or  self.elements.insert(0,new_item)
                          
                    # removes the element at the FRONT of the Queue and return it
                    def dequeue(self):
                        if self.isEmpty():
                            print("Cannot dequeue. Queue is empty.")
                            return None
                        else:       
                            return self.elements.pop(0) # or   self.elements.pop()
                
                
                
                
                class bussClass:
                    def __init__(self):
                        self.x = 50
                        self.y = 50
                        self.width = 40
                        self.length = 60
                        self.vel = 10
                        #pygame.draw.rect(win,(255,255,255),(x,y,width,length))
                        
                class humans:
                    def __init__(self):
                        self.x = 500
                        self.y = 50
                        self.width = 20
                        self.length = 20
                        self.vel = 10
                        #pygame.draw.rect(win,(255,255,255),(self.x,self.y,self.width,self.length))
                        
                    
                    def move_1(self,X,Y):
                
                        y = X-self.vel
                        return y
                    def move_2(self,X,Y):
                        if Y != 150:
                            y1 = Y+self.vel
                            return y1
                        if Y == 150:
                            y = X-self.vel
                            return y
                    def move_3(self,X,Y):
                
                        if Y != 250:
                            y1 = Y+self.vel
                            return y1
                        if Y == 250:
                            y = X-self.vel
                            return y
                    def move_4(self,X,Y):
                
                        if Y != 350:
                            y1 = Y+self.vel
                            return y1
                        if Y == 350:
                            y = X-self.vel
                            return y
                    def move_5(self,X,Y):
                
                        if Y != 450:
                            y1 = Y+self.vel
                            return y1
                        if Y == 450:
                            y = X-self.vel
                            return y
                            
                        #y = self.x-self.vel
                        #return y
                
                q = Queue()
                
                x = 1
                
                fonta = pygame.font.SysFont('mingliu-xtb', 22, True)
                fontNum = pygame.font.SysFont('Arial', 28, True)
                fontNumUp = pygame.font.SysFont('Calibre', 18, True)
                
                                        
                passNum= int(randint(1,15))
                numPass = passNum
                #label = makeLabel("hi",30,50,50,"red","Arial")
                print('passNum',passNum)
                for i in range(passNum):
                    rand= int(randint(0,14))
                    ForTable.append(names[rand])
                    q.enqueue(names[rand])
                    ForInOut.append('out')
                    ForPayment.append(0)
                    ForDestination.append('')
                print('size',q.size())
                    
                     
                
                #font = pygame.font.SysFont(None , 25)
                #def message_to_Screen(msg,color):
                 #   screen_text = font.render(msg,True,color)
                def table(deq,payment,destination):
                    s2 = 50
                    s22 = 80
                    #tableTop = fonta.render('Ticket Number  |   Name   |   Payment  |  Destination   |    In', 1, (255,255,255))
                    #win.blit(tableTop, (580, s2))
                    for i in range(len(ForTable)):
                        
                        Data = fonta.render('            '+str(i)+'                   '+ForTable[i]+'                  '+str(ForPayment[i])+'            '+str(ForDestination[i])+'                   '+ForInOut[i], 1, (255,255,255))   
                        
                        win.blit(Data, (625, s22))
                
                        s22 = s22+30
                        s2 = s2 +30
                               
                        
                        #pygame.display.update()
                def line():
                    s1 = 350
                    s2 = 100
                    s22 = 100
                    #text1 = fonta.render('Name', 1, (255,255,255))
                    head = fontNumUp.render('Passenger Count', 1, (255,255,255))
                    win.blit(head, (5, 8))  
                    text111 = fontNum.render(str(self.bus_1), 1, (255,255,255))   
                    win.blit(text111, (60, 30))
                    text111 = fontNum.render(str(self.bus_2), 1, (255,255,255))   
                    win.blit(text111, (60, 110)) 
                    text111 = fontNum.render(str(self.bus_3), 1, (255,255,255))   
                    win.blit(text111, (60, 210)) 
                    text111 = fontNum.render(str(self.bus_4), 1, (255,255,255))   
                    win.blit(text111, (60, 300)) 
                    text111 = fontNum.render(str(self.bus_5), 1, (255,255,255))   
                    win.blit(text111, (60, 390))     
                    for i in range(numPass):
                        text1 = fonta.render(q.elements[i], 1, (255,255,255))   
                        win.blit(text1, (573, s2))
                        #pygame.draw.rect(win,(255,255,255),(548,s22,passengers.width,passengers.length))
                        win.blit(self.ch, (540, s2))
                        s22 = s22+30
                        s2 = s2 +30
                       
                    pygame.display.update()
                    #time.sleep(0.5)
                        
                            
                def Lane():
                    
                    lane= int(randint(0,2))
                    if lane == 0:
                        sizeX = 350
                        sizeY = 50
                    if lane == 1:
                        sizeX = 355
                        sizeY = 50
                    if lane == 2:
                        sizeX = 360
                        sizeY = 50 
                         
                buss = bussClass()
                def bussSize():
                    y = 20
                    print('destination size',len(self.destination))
                    for i in range(len(self.destination)):
                        
                        text111 = fonta.render(self.destination[i], 1, (255,255,255))   
                        win.blit(text111, (185, y))
                        
                        y+=95
                      
                    
                    
                    #pygame.draw.rect(win,(255,255,255),(175,35,130,60))
                    #text1111 = fonta.render('BUKIDNON', 1, (255,255,255))   
                    #win.blit(text1111, (185, 110))
                    #pygame.draw.rect(win,(255,255,255),(175,130,130,60))
                    #text11111 = fonta.render('MARAWI', 1, (255,255,255))   
                    #win.blit(text11111, (185, 210))
                    #pygame.draw.rect(win,(255,255,255),(175,225,130,60)) 
                    
                    
                #clock =pygame.time.Clock()
                #FPS = 150   
                #fade(width, height)
                win.fill((255,255,255))
                pygame.display.update()
                run =True
                passengers = humans()
                while run:
                    pygame.time.delay(100)
                    
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run =False
                        print(event)
                    
                    
                    keys = pygame.key.get_pressed()
                
                    #if keys[pygame.K_LEFT] and x > vel:
                     #   x-=vel
                
                    #if keys[pygame.K_RIGHT] and x < 500 - width - vel:
                     #   x+=vel
                
                    #if keys[pygame.K_UP] and y > vel:
                     #   y-=vel
                
                    #if keys[pygame.K_DOWN] and y < 500 - length - vel:
                     #   y+=vel
                
                    #if event.type == pygame.MOUSEBUTTONDOWN:
                    #pygame.draw.rect(win,(255,255,255),(buss.x,buss.y,buss.width,buss.length))    
                
                      
                    if keys[pygame.K_p]:
                        #pygame.draw.rect(win,(255,255,255),(350,50,passengers.width,passengers.length))
                        sizeX =500
                        sizeY = 50
                        j=0
                        while True: 
                            X=sizeX
                            Y= sizeY
                            print('X',x)
                            ForInOut[j]='In'
                            
                            
                            #pygame.draw.rect(win,(255,255,255),(X,Y,passengers.width,passengers.length))
                            random = int(randint(1,13))
                            print(random)
                            if random == 1 or random == 4 or random == 7 or random == 0:
                                numPass = numPass-1
                                ForPayment[j]=self.fares[0]
                                ForDestination[j]=self.destination[0]
                                ForInOut[j]='In'
                                self.Resultbus_1.append(q.elements[0])
                                q.dequeue()
                                self.busTotal_1+=int(self.fares[0])
                                while True:
                                    
                                    
                                    pygame.display.update()
                                    
                                    
                                    X= passengers.move_1(X,Y)
                                    print('X',X)
                                    #line()
                                    time.sleep(0.01)
                                    win.fill((0,0,0))
                                    win.blit(background,(0,0))
                                    bussSize() 
                                    #ForInOut[j]='In'
                                    
                                    table('','','') 
                                    line() 
                                    win.blit(self.ch, (X, Y))
                                    #pygame.draw.rect(win,(255,255,255),(X,Y,passengers.width,passengers.length))
                                    pygame.display.update()
                                    
                                    
                                    #table('','','')  
                                    if X == 300:
                                        #ForInOut[j]='In'
                                        #ForPayment[j]=150
                                        win.blit(background,(0,0))
                                        self.bus_1+=1#int(self.fares[0])
                                        line() 
                                        break
                                
                                
                                
                    
                                    
                            elif random == 2 or random == 5 or random == 8:
                                numPass = numPass-1
                                ForPayment[j]=self.fares[1]
                                ForDestination[j]=self.destination[1]
                                ForInOut[j]='In'
                                self.Resultbus_2.append(q.elements[0])
                                q.dequeue()
                                self.busTotal_2+=int(self.fares[1])
                                cnt=0
                                while True:
                                    if X != 452 and cnt ==0:  
                                        print('yowi')                 
                                        while True:
                                            time.sleep(0.01)
                                            win.fill((0,0,0))
                                            
                                            win.blit(background,(0,0))
                                            bussSize()
                                            table('','','')
                                            line()
                                            win.blit(self.ch, (X, Y))
                                            #pygame.draw.rect(win,(255,255,255),(X,Y,passengers.width,passengers.length))
                                            #table('','','')
                                            pygame.display.update()
                                            print('X ni',X)
                                            
                                            if X == 452:
                                                cnt=1
                                                break
                                            X = X-6
                                    
                                    if Y != 150:
                                        Y= passengers.move_2(X,Y)
                                #passengers.x= passengers.move_2()
                                    if Y == 150 :
                                        X= passengers.move_2(X,Y)
                                    
                                    time.sleep(0.01)
                                    win.fill((0,0,0))
                                    win.blit(background,(0,0))
                                    #table()
                                    bussSize()
                                    #ForInOut[j]='In'
                                    table('','','')
                                    win.blit(self.ch, (X, Y))
                                    #pygame.draw.rect(win,(255,255,255),(X,Y,passengers.width,passengers.length))
                                    line()
                                    pygame.display.update()
                                    #ForInOut[j]='In'
                                    #table('','','') 
                                    print('current',X)
                                    if X == 302: 
                                        #ForInOut[j]='In'
                                        #ForPayment[j]=250
                                        self.bus_2+=1
                                        line()
                                        break
                                
                                
                                #line()
                
                            elif random == 3 or random == 6 or random == 9:
                                numPass = numPass-1
                                ForPayment[j]=self.fares[2]
                                ForDestination[j]=self.destination[2]
                                ForInOut[j]='In'
                                self.Resultbus_3.append(q.elements[0])
                                deq = q.dequeue()
                                self.busTotal_3+=int(self.fares[2])
                                cnt = 0
                                #table()
                                while True:
                                    #table()
                                    if X != 452 and cnt ==0:  
                                        print('yowi')                 
                                        while True:
                                            time.sleep(0.01)
                                            win.fill((0,0,0))
                                            win.blit(background,(0,0))
                                            bussSize()
                                            win.blit(self.ch, (X, Y))
                                            #pygame.draw.rect(win,(255,255,255),(X,Y,passengers.width,passengers.length))
                                            #table()
                                            table('','','')
                                            
                                            line()
                                            pygame.display.update()
                                            print('X2 ni',X)
                                            #line()
                                            #table()
                                            if X == 452:
                                                cnt=1
                                                break
                                            X = X-6
                                            #table()
                                    if Y != 250:
                                        Y= passengers.move_3(X,Y)
                                #passengers.x= passengers.move_2()
                                    if Y == 250:
                                        X= passengers.move_3(X,Y)
                                    time.sleep(0.01)
                                    
                                    win.fill((0,0,0))
                                    
                                    #ForInOut[j]='In'
                                    
                                    win.blit(background,(0,0))
                                    bussSize()
                                    table('','','')
                                    #pygame.draw.rect(win,(255,255,255),(X,Y,passengers.width,passengers.length))
                                    win.blit(self.ch, (X, Y))
                                    line()
                                    
                                    pygame.display.update()
                                    
                                    #ForInOut[j]='In'
                                    #table('','','') 
                                    #table(deq,'','')
                                    if X == 302 : 
                                        #ForPayment[j]=150
                                        self.bus_3+=1#int(self.fares[0])
                                        line()
                                        break
                                    #table()
                                
                                #line()
                            elif random == 10 or random == 12 :
                                numPass = numPass-1
                                ForPayment[j]=self.fares[3]
                                ForDestination[j]=self.destination[3]
                                ForInOut[j]='In'
                                self.Resultbus_4.append(q.elements[0])
                                deq = q.dequeue()
                                self.busTotal_4+=int(self.fares[3])
                                cnt = 0
                                #table()
                                while True:
                                    #table()
                                    if X != 452 and cnt ==0:  
                                        print('yowi')                 
                                        while True:
                                            time.sleep(0.01)
                                            win.fill((0,0,0))
                                            win.blit(background,(0,0))
                                            bussSize()
                                            win.blit(self.ch, (X, Y))
                                            #pygame.draw.rect(win,(255,255,255),(X,Y,passengers.width,passengers.length))
                                            #table()
                                            table('','','')
                                            
                                            line()
                                            pygame.display.update()
                                            print('X2 ni',X)
                                            #line()
                                            #table()
                                            if X == 452:
                                                cnt=1
                                                break
                                            X = X-6
                                            #table()
                                    if Y != 350:
                                        print('Y2 ni',Y)
                                        Y= passengers.move_4(X,Y)
                                #passengers.x= passengers.move_2()
                                   
                                    if Y == 350:
                                        X= passengers.move_4(X,Y)
                                    time.sleep(0.01)
                                    
                                    win.fill((0,0,0))
                                    
                                    #ForInOut[j]='In'
                                    
                                    win.blit(background,(0,0))
                                    bussSize()
                                    table('','','')
                                    #pygame.draw.rect(win,(255,255,255),(X,Y,passengers.width,passengers.length))
                                    win.blit(self.ch, (X, Y))
                                    line()
                                    
                                    pygame.display.update()
                                    
                                    #ForInOut[j]='In'
                                    #table('','','') 
                                    #table(deq,'','')
                                    if X == 302 : 
                                        #ForPayment[j]=150
                                        self.bus_4+=1#int(self.fares[0])
                                        line()
                                        break
                                    #table()
                                
                                #line()
                            elif random == 11 or random == 13 :
                                numPass = numPass-1
                                ForPayment[j]=self.fares[4]
                                ForDestination[j]=self.destination[4]
                                ForInOut[j]='In'
                                self.Resultbus_5.append(q.elements[0])
                                deq = q.dequeue()
                                self.busTotal_5+=int(self.fares[4])
                                cnt = 0
                                #table()
                                while True:
                                    #table()
                                    if X != 452 and cnt ==0:  
                                        print('yowi')                 
                                        while True:
                                            time.sleep(0.01)
                                            win.fill((0,0,0))
                                            win.blit(background,(0,0))
                                            bussSize()
                                            win.blit(self.ch, (X, Y))
                                            #pygame.draw.rect(win,(255,255,255),(X,Y,passengers.width,passengers.length))
                                            #table()
                                            table('','','')
                                            
                                            line()
                                            pygame.display.update()
                                            print('X2 ni',X)
                                            #line()
                                            #table()
                                            if X == 452:
                                                cnt=1
                                                break
                                            X = X-6
                                            #table()
                                    if Y != 450:
                                        Y= passengers.move_5(X,Y)
                                #passengers.x= passengers.move_2()
                                    if Y == 450:
                                        X= passengers.move_5(X,Y)
                                    time.sleep(0.01)
                                    
                                    win.fill((0,0,0))
                                    
                                    #ForInOut[j]='In'
                                    
                                    win.blit(background,(0,0))
                                    bussSize()
                                    table('','','')
                                    #pygame.draw.rect(win,(255,255,255),(X,Y,passengers.width,passengers.length))
                                    win.blit(self.ch, (X, Y))
                                    line()
                                    
                                    pygame.display.update()
                                    
                                    #ForInOut[j]='In'
                                    #table('','','') 
                                    #table(deq,'','')
                                    if X == 302 : 
                                        #ForPayment[j]=150
                                        self.bus_5+=1#int(self.fares[0])
                                        line()
                                        break
                                    #table()
                                
                                #line()   
                            #time.sleep(0.01)
                            bussSize()
                            table('','','')
                            win.blit(background,(0,0))
                            #pygame.display.update()
                            j=j+1
                            
                            #table('','','')
                            #pygame.display.update()
                            #ForInOut[j]='In'
                            
                            print('X sa last')
                            if x == passNum:
                                break
                            
                            x = x+1
                    win.blit(background,(0,0)) 
                    line()
                    table('','','')
                    bussSize() 
                    pygame.display.update()
                
                     #   y-=vel
                    
                
                
                
                    if q.isEmpty():
                        print('hi')
                        
                        self.end()
                        break
                    
                   
                    
                    
                
    
                #sys.exit()
            
                
                #exec('FinalPaynal.py')
            else:
                self.destination.append(self.textEdit.toPlainText())
                self.fares.append(self.textEdit_2.toPlainText())
                print('fares',self.fares,'and destination',self.destination)
                self.textEdit.setText('')
                self.textEdit_2.setText('')
            self.retranslateUi(MainWindow)
            
            
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600)
        MainWindow.setStyleSheet("border-color: rgb(117, 242, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 190, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(27)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(500, 260, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(560, 310, 81, 20))
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(540, 330, 104, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 400, 131, 41))
        #********************************************
        self.pushButton.clicked.connect(self.check)
        #********************************************
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(590, 370, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
       
        self.label_3.setObjectName("label_3")
         #*************************************
        
         #*************************************
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.Destination_Count = 5
        self.label_3.setText(str(self.Destination_Count))
        self.destination = []
        self.fares = []
        self.Resultbus_1 = []
        self.Resultbus_2 = []
        self.Resultbus_3 = []
        self.Resultbus_4 = []
        self.Resultbus_5 = []
        self.bus_1= 0
        self.bus_2= 0
        self.bus_3= 0
        self.bus_4= 0
        self.bus_5= 0
        self.busFare_1= 0
        self.busFare_2= 0
        self.busFare_3= 0
        self.busFare_4= 0
        self.busFare_5= 0
        self.busTotal_1= 0
        self.busTotal_2= 0
        self.busTotal_3= 0
        self.busTotal_4= 0
        self.busTotal_5= 0
        self.ch = pygame.image.load('Tao.png')
        self.ch = pygame.transform.scale(self.ch, (30, 30))
        
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ENTER 5 DESTINATIONS"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "ENTER FARE:"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "ADD"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
