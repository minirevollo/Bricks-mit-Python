# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 20:45:34 2018

@author: Mini Revollo

member of the erfindergarden
"""

from tkinter import *
from time import *
from random import randint
import time

class EINLEITUNG:
    ###Stellt alle Einstellungen für die erste Ansicht zur Verfügung.###
   
    def  __init__(self):
        ###Iniziert die Einleitung.###
        
        print("EINLEITUNG  initiert")
        self.breite = 600
        self.hoehe = 500
        self.info_hoehe = 20
        self.anzeige = Frame(root, bg = "black")
        self.anzeige.place(x = 0, y = 0, width = self.breite, height = self.hoehe)
        self.einleitung_logo = Label(root, font = "Consolas", 
                                     text = " bricks \n by mini revollo\n from\n the erfindergarden",
                                     bg = "black", fg = "green")
        self.einleitung_info = Label(root, font = "Consolas", 
                                     text = " press < s > for start ",
                                     bg = "black", fg = "green")
        self.einblenden()
        
    def einblenden(self):
        ###Blendet die inizierte Einleitung ein.###
        
        self.einleitung_logo.place(x = (self.breite - 200) / 2 ,
                                   y = 100, width = 200, height = 80)
        self.einleitung_info.place(x = (self.breite - 200) / 2,
                                   y = self.hoehe - self.info_hoehe,
                                   width = 200, height = self.info_hoehe)

    def ausblenden(self):
        ###Blendet die Einleitung wieder aus.###
        
        self.einleitung_logo.place_forget()
        self.einleitung_info.place_forget()
        
                
class SPIEL:
    ###Stellt alles für das Spiel zur verfügung.###
    
    def __init__(self):
        ###Initiert das Spiel.###
        
        print("SPIEL initialisieren")
        self.breite = 300
        self.status = 0
        self.score = 0 #Spielstand 
        self.score_hoehe = 20
        self.info_hoehe = 20
        self.spiel_score = Label(root, font = "Consolas", 
                                 text = "score: " + str(self.score) , 
                                 bg = "black", fg = "green")
        self.spiel_info = Label(root, font = "Consolas", 
                                text = " press arrow < and > for moving ", 
                                bg = "black", fg = "green")

    def einblenden(self):
        ###Blendet alles für das Spiel ein.###
        
        self.spiel_score.place(x = (einleitung.breite - self.breite) / 2 , 
                               y = 0, width = self.breite, height = 20)
        self.spiel_info.place(x = (einleitung.breite - self.breite) / 2, 
                              y = einleitung.hoehe - self.info_hoehe, 
                              width = self.breite, height = 20)

    def ausblenden(self):
        ###Blendet alles wieder aus.###
        
        self.spiel_score.place_forget()
        self.spiel_info.place_forget()

    def score_aktualisieren(self):
        ###Aktualisiert die Ansicht des Punktestandes.###
        
        self.spiel_score.config(text = "score: " + str(self.score))
        spiel.einblenden()
        
class PUNKTE:
    ###Initiert alles für die Highscoreansicht.###
    
    
    def __init__(self):
        ###Initiert die Highscoreansicht.###
        
        self.breite = 300
        self.highscore = [0, 0, 0, 0, 0] 
        self.info_hoehe = 20
        self.score_info = Label(root, font = "Consolas", 
                                text = " press - n - for a new game ", 
                                bg = "black", fg = "green")
        
    def einblenden(self):
        ###Blendet die Highscoreansicht ein.###
        
        self.score_info.place(x = (einleitung.breite - self.breite) / 2, 
                              y = einleitung.hoehe - self.info_hoehe, 
                              width = self.breite, height = 20)
    
    def ausblenden(self):
        ###Blendet die Highscoreansicht wieder aus.###
        
        self.score_info.place_forget()
      
    

class BLOCK:
    ###Alles um die Blöcke anzuzeigen.###
    
    
    blocks = [] #Hält die einzelne Blöcke in einer Liste

    def __init__(self, x, y):
        ###Initiert einen Block.###
        
        print("Block initialisieren")
        self.breite = 40
        self.hoehe = 20
        self.pos_x = x
        self.pos_y = y
        self.block = Label(root, font = "Consolas", 
                           text = "[___]", bg = "black", fg = "green")
        
    def initialisieren_alle():
        ###Loop um alle Blöcke zu initialisieren.###
        
        print("Blocks setzen")
        for item in range(30):
            b = "block" + str(item)  #block0, block1, ...
            print(b)
            x = item * 40
            y = 20
            if item > 14:  #zweite Reihe setzen
                x -= 600
                y = 40
            b = BLOCK(x, y)
            BLOCK.blocks.append(b)  #Der neue Block wird in die List eingeführt
            print(BLOCK.blocks[item].pos_x)
            print(BLOCK.blocks[item].pos_y)
        print(BLOCK.blocks)          
   
    def einblenden(self):
        ###Blendet einen Block ein.###
        
        self.block.place(x = self.pos_x, y = self.pos_y, 
                         width = self.breite, height = self.hoehe)
    
    def einblenden_alle():
        ###Loop um alle Blocks einzublenden.###
        
        print("Blocks einblenden")
        for item in BLOCK.blocks:
            item.einblenden()   
            
    def ausblenden(self):
        ###Blendet einen Block aus.###
        
        self.block.place_forget() 
        
           
    def ausblenden_alle():
        ###Loop um alle Blocks auszublenden.###
        
        for item in BLOCK.blocks:
            item.ausblenden()            
    
    def löschen_alle():
        ###Loop um alle Blöcke aus der Liste zu löschen.###
        
        for item in range(len(BLOCK.blocks)):
            BLOCK.blocks.pop()
            
class BALL:
    ###Alles um den Ballzu steuern.###
    
    def __init__(self):
        ###Initialisiert den Ball.###
        
        print("Ball initialisieren")  
        self.breite = 8
        self.hoehe = 12
        self.speed = -4 #Bewegung in der y-Achse
        self.steigung = 0.2 #Verhältnis von x- zu y- Bewegung
        self.pos_x = 300 
        self.pos_y = 250
        self.ball = Label(root, font = "Consolas", text = "o", 
                          fg = "green", bg = "black")
              
    def berechnen(self):
        ###Berechnet die neue Position in jedem Loop neu.###
        
        self.pos_y = self.pos_y + self.speed #Bewegung auf der y-Achse
        if self.pos_y < spiel.score_hoehe or (brett.pos_y > self.pos_y > brett.pos_y - brett.hoehe and brett.pos_x < self.pos_x < brett.pos_x + brett.breite):
            #Kontrolliert ob der Ball das Brett trifft.
            self.speed = self.speed * -1  #Richtungsumkehr
            self.steigung = self.steigung * -1  #Steigungsumkehr
            self.steigung = self.steigung + brett.geschwindigkeit/1000  
            #Anpassung der Steigung durch die Brettgeschwindigkeit
        if self.pos_y > einleitung.hoehe: #Kontrolliert ob der Ball unten raus fällt.
            spiel.status = 2 #Wechselt in highscore-modus
            ball.ausblenden()
            brett.ausblenden()
            spiel.ausblenden()
            BLOCK.ausblenden_alle()
            BLOCK.löschen_alle()
            score.ermitteln()
            score.einblenden()
        self.pos_x = self.pos_x + self.speed * self.steigung
            #Seitwertsbewegung des Balls.
        if self.pos_x < 0 + self.breite or self.pos_x > einleitung.breite - self.breite:
            #Abprallen links und rechts
            self.steigung = self.steigung * -1
    
    def kontakt_kontrollieren(self):
        ###Kontrolliert ob der Ball einen Block getroffen hat.###
        
        flag = 0 #ob ein Block getroffen wird und dieser gelöscht werden soll.
        for item in BLOCK.blocks:
            if item.pos_x < self.pos_x < item.pos_x + item.breite and item.pos_y < self.pos_y < item.pos_y + item.hoehe:
                item.ausblenden() #Blendet den Block aus
                löschen = BLOCK.blocks.index(item) 
                #Listen-indes des zu löschenden Blocks
                flag = 1
                self.speed = self.speed * -1.02 #Steigerung der Geschwindigkeit
                self.steigung = self.steigung * -1  #Richtungsumkehr
                spiel.score += 1 #Punkte werden gesteigert
                break
        if flag == 1:
            BLOCK.blocks.pop(löschen) #Getroffener Block wird gelöscht
            flag = 0
 
    def ursprung(self):
        ###Informationen um bei einem neuen Spiel den Ball 
        ###wieder richtig zu positionieren.###
        
        self.speed = -3  #Geschwindigkeit, - bedeutete nach oben
        self.pos_x = randint(50, einleitung.breite - 50 )
        self.pos_y = 250
        self.drehung = 0
        self.steigung = 0.2
        
    def einblenden(self):
        ###Der Ball wird eingeblendet.###
        
        self.ball.place(x = int(self.pos_x), y = int(self.pos_y), 
                        width = self.breite, height = self.hoehe)
        
    def ausblenden(self):
        ###Der Ball wird ausgeblendet.###
        
        self.ball.place_forget()
        
        
class BRETT:
    ###Alles um das Brett zu steuern.###
    
    def __init__(self):
        ###Initiert das Brett.###
        
        print("BRETT initialisieren")
        self.breite = 50
        self.hoehe  = 10
        self.geschwindigkeit = 0
        self.zeit= 0 #Zeitpunkt der letzten Brettbewegung
        self.pos_x = randint(0, einleitung.breite - self.breite)
        self.pos_y = einleitung.hoehe - einleitung.info_hoehe - self.hoehe 
        self.pos_x_alt = self.pos_x
        self.brett = Label(root, text = "xxxxxxx", bg = "black", fg = "green")
        
    def einblenden(self):
        ###Blendet das Brett ein.###
        
        self.brett.place(x = self.pos_x, y = self.pos_y , 
                         width = self.breite, height = self.hoehe)
        
    def ausblenden(self):
        ###Blendet das Brett wieder aus.###
        
        self.brett.place_forget()
        
    def geschwindigkeit_berechnen(self):
        ###Berechnet die Geschwindigkeit des Brettes anhand der 
        ###Positionsveränderung innerhalb der messdauer.###
        
        messdauer = 0.1 #Abstand der zwischen den Positionsbestimmungen.
        if time.time() - self.zeit > messdauer:
            self.geschwindigkeit = (self.pos_x - self.pos_x_alt) / messdauer
            print("Geschwindigkeit: " + str(self.geschwindigkeit))
            self.pos_x_alt = self.pos_x
            self.zeit = time.time()
        

class SCORE:
    ###Alles um den Highscore anzuzeigen.###
    
    def __init__(self):
        ###Initialisiert den Highscore.###
        
        print("SCORE initialisieren")
        self.breite = 200
        self.hoehe = 50
        self.rekord_name = [ 65, 65, 65] #ASII-code für die Buchstabeneingabe.
        self.rekord_buchstabenposition = 0 #Position des gerade veränderbaren Buchstabens.
        self.rekord_position = 0 #Position des letzten spiel-scores in der HS-Liste
        self.rekord_setzen = 0 #ob der neue Rekord eingetragen werden soll
        self.rekord_hoehe = 150
        self.rekord_breite = 150
        self.rekord = [ ("___", 0), ("___", 0), ("___", 0), ("___", 0), ("___", 0)] 
        #Redordliste mit Name und Punkten
        self.info_hoehe = 20
        self.info_breite = 400
        self.info_rekord = Label(root, 
                                 text = chr(self.rekord_name[0]) + chr(self.rekord_name[1]) + chr(self.rekord_name[2]), 
                            font = "Consolas", 
                            bg = "black", 
                            fg = "green")
        self.punkte = Label(root, text = "  highscore: " 
                            + "\n pos 1.   " + self.rekord[0][0] + "   " + str(self.rekord[0][1])
                            + "\n pos 2.   " + self.rekord[1][0] + "   " + str(self.rekord[1][1])
                            + "\n pos 3.   " + self.rekord[2][0] + "   " + str(self.rekord[2][1])
                            + "\n pos 4.   " + self.rekord[3][0] + "   " + str(self.rekord[3][1])
                            + "\n pos 5.   " + self.rekord[4][0] + "   " + str(self.rekord[4][1]),
                            font = "Consolas", 
                            fg = "green", 
                            bg = "black")
        self.score_info = Label(root, font = "Consolas", 
                                text = " press - n - for a new game ", 
                                bg = "black", fg = "green")

    def einblenden(self):
        ###Blendet Liste und Info ein.###
        
        self.punkte.place(x = (einleitung.breite - self.breite) / 2, 
                          y = 130, width = self.breite, height = 120)
        self.score_info.place(x = (einleitung.breite - self.info_breite) / 2, 
                              y = einleitung.hoehe - self.info_hoehe, 
                              width = self.info_breite, height = self.info_hoehe)
   
    def namen_einblenden(self):
        ###Blendet die Namenseingabe ein.###
        
        self.info_rekord.place(x = (einleitung.breite - self.info_breite) / 2, y = 100, 
                               width = self.info_breite, height = self.info_hoehe)

    
    def ausblenden(self):
        ###Blendet alles um den Highscore wieder aus.###
        
        self.info_rekord.place_forget()
        self.punkte.place_forget()
        self.score_info.place_forget()
        
    def aktualisieren(self):
        ###Aktualisiert die Highscoreliste mit dem neuen Namen und Punkten.###
        
        self.info_rekord.config(text = chr(self.rekord_name[0]) 
        + chr(self.rekord_name[1]) + chr(self.rekord_name[2]))
        self.punkte.config(text = "  highscore: " 
                            + "\n pos 1.   " + self.rekord[0][0] + "   " + str(self.rekord[0][1])
                            + "\n pos 2.   " + self.rekord[1][0] + "   " + str(self.rekord[1][1])
                            + "\n pos 3.   " + self.rekord[2][0] + "   " + str(self.rekord[2][1])
                            + "\n pos 4.   " + self.rekord[3][0] + "   " + str(self.rekord[3][1])
                            + "\n pos 5.   " + self.rekord[4][0] + "   " + str(self.rekord[4][1]))
        
    def uebergeben(self):
        ###Übergibt den eingegebenen Namen an die Highscoreliste.###
        
        if self.rekord_setzen == 1:
            text = chr(self.rekord_name[0]) + chr(self.rekord_name[1]) + chr(self.rekord_name[2])
            pos = self.rekord_position
            punkte =  self.rekord[pos][1]
            self.rekord[pos] = (text, punkte)
            self.rekord_setzen = 0
            self.rekord_name = [ 65, 65, 65]
            self.aktualisieren()
            
    def ermitteln(self):
        ###Ermittelt ob der Spiel-Score in die HS-Liste soll und an welcher Position.###
        
        for item in range(5):
            if spiel.score > score.rekord[item][1]:
                self.rekord.insert(item, ("___", spiel.score))
                self.rekord.pop(5) #Löscht den kleinsten Rekordhalter raus
                self.rekord_position = item #Hält die Position des aktuellen Punkte
                self.rekord_setzen = 1 
                spiel.score= 0 #löscht die Punkte für das neue Spiel
                self.namen_einblenden()
                                                       
def tastenabfrage(key):
    ###Ordnet je nach spielmodus die Tasten-Events Ereignissen zu.###
    
    print(key.char)
    if spiel.status == 0: #Einleitung
        if key.char == "s": #Startet das Spiel
            spiel.status = 1
            einleitung.ausblenden()
            spiel.einblenden()
            brett.einblenden()
            ball.einblenden()
            BLOCK.einblenden_alle()
    if spiel.status == 1:  #Spiel
        if key.keysym == "Right": #Bewegt das Brett nach rechts. 
            if brett.pos_x + brett.breite < einleitung.breite:
                brett.pos_x += 10
                brett.einblenden()
        if key.keysym == "Left":  #Bewegt das Brett nach links.
            if brett.pos_x > 0:
                brett.pos_x -= 10
                brett.einblenden()
    if spiel.status == 2: #Highscoreanzeige
        if key.keysym == "Right": 
            #Wechselt auf den nächsten zu verändernden Buchstabens
            score.rekord_buchstabenposition += 1
            if score.rekord_buchstabenposition > 2:
                score.rekord_buchstabenposition = 0
        if key.keysym == "Left": 
            #Wechselt auf den nächsten zu verändernden Buchstabens
            score.rekord_buchstabenposition -= 1
            if score.rekord_buchstabenposition < 0:
                score.rekord_buchstabenposition = 2
        if key.keysym == "Up": #Verändert den aktuellen Buchstaben.
            score.rekord_name[score.rekord_buchstabenposition] += 1
            if score.rekord_name[score.rekord_buchstabenposition] > 120:
                score.rekord_buchstanbeposition = 65
        if key.keysym == "Down": #Verändert den aktuellen Buchstaben.
            score.rekord_name[score.rekord_buchstabenposition] -= 1
            if score.rekord_name[score.rekord_buchstabenposition] < 65:
                score.rekord_buchstanbeposition = 120
        if key.keysym == "Return": #Name wird in die Liste eingetragen.
            score.uebergeben()
        if key.char == "n": #Neues Spiel wird gestartet
            BLOCK.initialisieren_alle()
            BLOCK.einblenden_alle()
            spiel.status = 1
            punkte.ausblenden()
            spiel.einblenden()
            brett.einblenden()
            ball.ursprung()
            ball.einblenden()
            score.ausblenden()
            
    

""" Setup """

root = Tk()         #ein Fenster erstellen
root.geometry("600x500")          #Größe zuordnen
root.title("           bricks - by mini revollo              ")

 #Fenster mit einem Titel versehen 
root.bind_all("<KeyPress>", tastenabfrage)    
 #Tastendruck abfangen 

einleitung = EINLEITUNG()
brett = BRETT()
spiel = SPIEL()
ball = BALL()
punkte = PUNKTE()
BLOCK.initialisieren_alle()
score = SCORE()


""" Loop """
   
def das_spiel():
    ###Der eigentliche Loop der das Spiel durchführt.###
    
    print("status: " + str(spiel.status))
    if spiel.status == 0:
        print("einleitung")
    elif spiel.status == 1:
        print("spiel")
        spiel.score_aktualisieren()
        ball.berechnen()
        ball.einblenden()
        ball.kontakt_kontrollieren()
        brett.geschwindigkeit_berechnen()
    else:
        print("score")
        score.aktualisieren()
        score.einblenden()
        
        
    root.after(10, das_spiel) #Steuert den loop
        

    
root.after(0,das_spiel)    
root.mainloop()