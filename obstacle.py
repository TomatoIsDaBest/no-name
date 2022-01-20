from pgzero.screen import Screen
try:
    import pgzrun
    import pygame
    import json
    import time
    import sys
    import traceback
    from random import randint
    from pygame.locals import *
    pygame.init()
    WIDTH = 1200
    HEIGHT = 600          
    TITLE = "Obstacle | V1"   
    c = True
    d = True
    huongdan = False
    aboutme = False
    start = False
    diamond_easy = False
    diamond_normal = False
    diamond_hard = False
    thanhtich = False
    nhiemvu = False
    claim1 = False
    claim2 = False
    buy1 = False
    buy2 = False
    shopping = False
    a = False
    b = False
    score = 0
    live = 10
    gravity = 15
    level = 1       
    player = Actor("jumper-1",(200,300))
    diamond = Actor("diamond_s",(400,500))
    enemy = Actor("bug",(1200,200))
    bg_x = 0
    bat_nhac_button = Rect((1100,560),(100,40))
    tat_nhac_button = Rect((0,560),(100,40))
    buy_button1 = Rect((1000,50),(100,50))
    buy_button2 = Rect((1000,150),(100,50))
    sell_button1 = Rect((100,50),(350,50))
    sell_button2 = Rect((100,150),(350,50))
    mission1 = Rect((100,50),(350,50))
    mission2 = Rect((100,120),(350,50))
    claim_button2 = Rect((800,120),(100,50))
    claim_button = Rect((800,50),(100,50))
    nut_thanh_tich = Rect((50,500),(115,50))
    nut_nhiem_vu = Rect((250,500),(115,50))
    nut_huong_dan = Rect((850,500),(115,50))
    aboutme_button = Rect((1050,500),(115,50))
    return_button = Rect((0,0),(30,30))
    restart_button = Rect((600,500),(100,50))
    easy_button = Rect((50,100),(100,50))
    normal_button = Rect((600,100),(100,50))
    hard_button = Rect((1050,100),(100,50))
    shop_button = Rect((600,300),(100,50))
    floor = Rect((0,580),(1200,20))
    rect1 = Rect((400,500),(100,10))
    rect2 = Rect((550,400),(100,10))
    rect3 = Rect((650,275),(100,10))
    rect4 = Rect((800,400),(100,10))
    rect5 = Rect((150,550),(100,10))
    rect6 = Rect((650,560),(100,10))
    rect7 = Rect((900,550),(100,10))
    rect8 = Rect((300,275),(100,10))
    rect9 = Rect((480,200),(100,10))
    rect10 = Rect((900,300),(100,10))
    rects = [rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9, rect10]

    data_score = {
        "score": 0
    }

    coins = {
        "coins": 0
    }

    try:
        with open("score.txt") as score_file:
            data_score = json.load(score_file)
    except:
        print("Hello")

    try:
        with open("coins.txt") as coins_file:
            coins = json.load(coins_file)
    except:
        print("hi")    
   

    def draw():
        global score, bg_x, level, live, start, aboutme, huongdan, thanhtich, nhiemvu, data_score, claim1, coins, claim2, buy1, buy2, shopping, a, b, c, d

        if start == False:               
            screen.clear()  
            screen.blit("menu_bg", (300,270))
            screen.blit("menu_bg", (850,270))      
            screen.draw.filled_rect(easy_button,(255,255,255))
            screen.draw.text("Easy",color = "black",topleft = (70,120))
            screen.draw.filled_rect(normal_button,(255,255,255))
            screen.draw.text("Normal",color = "blue",topleft = (620,120))
            screen.draw.filled_rect(hard_button,(255,255,255))
            screen.draw.text("Hard",color = "red",topleft = (1070,120))
            screen.draw.filled_rect(nut_huong_dan,(255,255,255))
            screen.draw.text("Guide",color = "black",topleft = (870,520))
            screen.draw.filled_rect(aboutme_button,(255,255,255))
            screen.draw.text("About me",color = "black",topleft = (1070,520))
            screen.draw.filled_rect(nut_thanh_tich,(255,255,255))
            screen.draw.text("Achievements",color = "black",topleft = (50,520))
            screen.draw.filled_rect(nut_nhiem_vu,(255,255,255))
            screen.draw.text("Missions",color = "black",topleft = (270,520))
            screen.draw.filled_rect(shop_button,(255,255,255))
            screen.draw.text("Shop",color = "black",topleft = (620,320))             
            
            screen.draw.text("Obstacle",color = "white",topleft = (610,25))             
            screen.draw.text("Background images, sounds and music I got from Google",color = "red",topleft = (380,550))
            screen.draw.text("Character image by Phil Hiett on YouTube", color = "red", topleft = (430,570))

        if huongdan == True:
            screen.clear()
            screen.draw.text("Press left key to go left. Press right key to go right. Press space to jump. Hope you enjoy :)",color = "white",topleft = (320,150))
            screen.draw.filled_rect(return_button,(255,255,255))
            screen.draw.text("<-",color = "black",topleft = (10,10))
            screen.draw.text("Press f for full screen and press q to exit full screen",color = "white",topleft = (450,350))
            

        if aboutme == True:
            screen.clear()
            screen.draw.filled_rect(return_button,(255,255,255))
            screen.draw.text("<-",color = "black",topleft = (10,10))
            screen.draw.text("Hello everyone, my name is Phuc Bao, I'm from VietNam\nI am currently studying at Nui Sap town secondary school\nThe year I made this game, I was 12 years old.",color = "white",topleft = (400,300))
            screen.draw.text("If you have any feedback, please contact us via email phucbaonn@gmail.com",color = "white",topleft = (300,450))

        if nhiemvu == True:
            screen.clear()
            screen.draw.filled_rect(return_button,(255,255,255))
            screen.draw.text("<-",color = "black",topleft = (10,10))        
            screen.draw.filled_rect(mission1,(255,255,255))
            screen.draw.filled_rect(claim_button,(255,255,255))
            screen.draw.text("Claim",color = "black",topleft = (820,70))
            screen.draw.text("Reach total score up to 500 to get 10 coins",color = "black",topleft = (110,70))
            screen.draw.filled_rect(mission2,(255,255,255))
            screen.draw.filled_rect(claim_button2,(255,255,255))
            screen.draw.text("Claim",color = "black",topleft = (820,140))
            screen.draw.text("Reach total score up to 1000 to get 20 coins",color = "black",topleft = (110,140))
                    

        if thanhtich == True:
            screen.clear()
            screen.draw.filled_rect(return_button,(255,255,255))
            screen.draw.text("<-",color = "black",topleft = (10,10))
            screen.draw.text("Total score: "+str(data_score["score"]),color = "white",topleft = (40,10))                
            screen.draw.text("Total coin: "+str(coins["coins"]),color = "white",topleft = (40,50))            
            

        if claim1 == True: 
            claim1 = False
            claim2 = False            
            if int(data_score["score"]) >= 500:
                screen.draw.text("Sccessfully claimed",color = "white",topleft = (600,300))
                time.sleep(1)
                data_score["score"] -= 500
                coins["coins"] += 10        
            claim1 = False

        if claim2 == True:  
            claim1 = False
            claim2 = False       
            if int(data_score["score"]) >= 1000:
                screen.draw.text("Sccessfully claimed",color = "white",topleft = (600,300))
                data_score["score"] -= 1000
                coins["coins"] += 20        
            claim2 = False

        if shopping == True:            
            screen.clear()
            music.stop()
            screen.draw.filled_rect(return_button,(255,255,255))
            screen.draw.text("<-",color = "black",topleft = (10,10))
            screen.draw.filled_rect(sell_button1,(255,255,255))
            screen.draw.text("Speed + 1 (10 coins)",color = "black",topleft = (140,70))
            screen.draw.filled_rect(sell_button2,(255,255,255))
            screen.draw.text("Gravity - 5 (20 coins)",color = "black",topleft = (140,170))        
            screen.draw.filled_rect(buy_button1,(255,255,255))
            screen.draw.text("Buy",color = "black",topleft = (1020,70))
            screen.draw.filled_rect(buy_button2,(255,255,255))
            screen.draw.text("Buy",color = "black",topleft = (1020,170))

        if buy1 == True and claim1 == False:
            a = True        
            screen.draw.text("Successfully purchase",color = "white",topleft = (580,300))
            if coins["coins"] >= 10:
                coins["coins"] -= 10
            buy1 = False 
            buy2 = False        
                    
            
        if buy2 == True and claim2 == False:  
            b = True          
            screen.draw.text("Successfully purchase",color = "white",topleft = (580,300))                 
            if coins["coins"] >= 20:                      
                coins["coins"] -= 20
            buy2 = False
            buy1 = False
        
    
        #level 1
        if start == True:                                          
            if score >= 0 and level <= 95:                                
                level = 1
                screen.blit("bg_nui",(bg_x,0))
                screen.blit("bg_nui",(bg_x + 1200,0))
                screen.draw.filled_rect(floor,(255,0,0))        
                for i in rects:
                    screen.draw.filled_rect(i,(0,0,139))                
                screen.draw.text("Score: "+str(score),color = "black",topleft = (40,10))  
                screen.draw.text("Level: "+str(level),color = "black",topleft = (250,10))
                screen.draw.text("Live: "+str(live),color = "black",topleft = (460,10))
                player.draw()
                diamond.draw()                                                          
                screen.draw.filled_rect(return_button,(255,255,255))
                screen.draw.text("<-",color = "black",topleft = (10,10)) 
                screen.draw.filled_rect(tat_nhac_button,(255,255,255))
                screen.draw.text("Stop music",color = "black",topleft = (5,570))
                screen.draw.filled_rect(bat_nhac_button,(255,255,255))
                screen.draw.text("Play music",color = "black",topleft = (1105,570))
                if diamond_easy == True:
                    screen.draw.text("Mode: Easy",color = "black",topleft = (1060,10))
                if diamond_normal == True:
                    screen.draw.text("Mode: Normal",color = "black",topleft = (1060,10))
                if diamond_hard == True:
                    screen.draw.text("Mode: Hard",color = "black",topleft = (1060,10))
        

            #level 2 
            if score >= 100 and score <= 195:        
                level = 2 
                screen.clear()  
                screen.blit("bg_hill",(bg_x,0))
                screen.blit("bg_hill",(bg_x + 1200,0))
                screen.draw.filled_rect(floor,(255,0,0))        
                for i in rects:
                    screen.draw.filled_rect(i,(64,64,64))                                                   
                screen.draw.text("Score: "+str(score),color = "black",topleft = (40,10))
                screen.draw.text("Level: "+str(level),color = "black",topleft = (250,10))    
                screen.draw.text("Live: "+str(live),color = "black",topleft = (460,10))
                player.draw()
                diamond.draw()                
                screen.draw.filled_rect(return_button,(255,255,255))
                screen.draw.text("<-",color = "black",topleft = (10,10))
                screen.draw.filled_rect(tat_nhac_button,(255,255,255))
                screen.draw.text("Stop music",color = "black",topleft = (5,570))
                screen.draw.filled_rect(bat_nhac_button,(255,255,255))
                screen.draw.text("Play music",color = "black",topleft = (1105,570))
                if diamond_easy == True:
                    screen.draw.text("Mode: Easy",color = "black",topleft = (1060,10))
                if diamond_normal == True:
                    screen.draw.text("Mode: Normal",color = "black",topleft = (1060,10))
                if diamond_hard == True:
                    screen.draw.text("Mode: Hard",color = "black",topleft = (1060,10))

        

            #level 3
            if score >= 200 and score <= 295:           
                screen.clear()
                level = 3
                screen.blit("bg_city",(bg_x,0))
                screen.blit("bg_city",(bg_x + 1200,0))
                screen.draw.filled_rect(floor,(255,0,0))        
                for i in rects:
                    screen.draw.filled_rect(i,(41,59,222))
                screen.draw.text("Score: "+str(score),color = "black",topleft = (40,10))
                screen.draw.text("Level: "+str(level),color = "black",topleft = (250,10))    
                screen.draw.text("Live: "+str(live),color = "black",topleft = (460,10))
                player.draw()
                diamond.draw()
                screen.draw.filled_rect(return_button,(255,255,255))
                screen.draw.text("<-",color = "black",topleft = (10,10))
                screen.draw.filled_rect(tat_nhac_button,(255,255,255))
                screen.draw.text("Stop music",color = "black",topleft = (5,570))
                screen.draw.filled_rect(bat_nhac_button,(255,255,255))
                screen.draw.text("Play music",color = "black",topleft = (1105,570))
                if diamond_easy == True:
                    screen.draw.text("Mode: Easy",color = "black",topleft = (1060,10))
                if diamond_normal == True:
                    screen.draw.text("Mode: Normal",color = "black",topleft = (1060,10))
                if diamond_hard == True:
                    screen.draw.text("Mode: Hard",color = "black",topleft = (1060,10))


            #level 4
            if score >= 300 and score <= 395:           
                screen.clear()
                screen.fill((255,255,255))
                level = 4
                screen.blit("skyline_large",(bg_x,0))
                screen.blit("skyline_large",(bg_x + 1200,0))
                screen.draw.filled_rect(floor,(255,0,0))        
                for i in rects:
                    screen.draw.filled_rect(i,(41,59,222))
                screen.draw.text("Score: "+str(score),color = "black",topleft = (40,10))
                screen.draw.text("Level: "+str(level),color = "black",topleft = (250,10))    
                screen.draw.text("Live: "+str(live),color = "black",topleft = (460,10))
                player.draw()
                diamond.draw()
                screen.draw.filled_rect(return_button,(255,255,255))
                screen.draw.text("<-",color = "black",topleft = (10,10))
                screen.draw.filled_rect(tat_nhac_button,(255,255,255))
                screen.draw.text("Stop music",color = "black",topleft = (5,570))
                screen.draw.filled_rect(bat_nhac_button,(255,255,255))
                screen.draw.text("Play music",color = "black",topleft = (1105,570))
                if diamond_easy == True:
                    screen.draw.text("Mode: Easy",color = "black",topleft = (1060,10))
                if diamond_normal == True:
                    screen.draw.text("Mode: Normal",color = "black",topleft = (1060,10))
                if diamond_hard == True:
                    screen.draw.text("Mode: Hard",color = "black",topleft = (1060,10))



            #level 5
            if score >= 400 and score <= 495:            
                screen.clear()
                level = 5
                screen.blit("bg_forest",(bg_x,0))
                screen.blit("bg_forest",(bg_x + 1200,0))
                screen.draw.filled_rect(floor,(255,0,0))        
                for i in rects:
                    screen.draw.filled_rect(i,(102,0,0))
                screen.draw.text("Score: "+str(score),color = "black",topleft = (40,10))
                screen.draw.text("Level: "+str(level),color = "black",topleft = (250,10))    
                screen.draw.text("Live: "+str(live),color = "black",topleft = (460,10))
                player.draw()
                diamond.draw()
                screen.draw.filled_rect(return_button,(255,255,255))
                screen.draw.text("<-",color = "black",topleft = (10,10))
                screen.draw.filled_rect(tat_nhac_button,(255,255,255))
                screen.draw.text("Stop music",color = "black",topleft = (5,570))
                screen.draw.filled_rect(bat_nhac_button,(255,255,255))
                screen.draw.text("Play music",color = "black",topleft = (1105,570))
                if diamond_easy == True:
                    screen.draw.text("Mode: Easy",color = "black",topleft = (1060,10))
                if diamond_normal == True:
                    screen.draw.text("Mode: Normal",color = "black",topleft = (1060,10))
                if diamond_hard == True:
                    screen.draw.text("Mode: Hard",color = "black",topleft = (1060,10))



            #level 6
            if score >= 500 and score <= 595:            
                screen.clear()
                level = 6
                screen.blit("bg_forest2",(bg_x,0))
                screen.blit("bg_forest2",(bg_x + 1200,0))
                screen.draw.filled_rect(floor,(255,0,0))        
                for i in rects:
                    screen.draw.filled_rect(i,(102,0,0))
                screen.draw.text("Score: "+str(score),color = "black",topleft = (40,10))
                screen.draw.text("Level: "+str(level),color = "black",topleft = (250,10))    
                screen.draw.text("Live: "+str(live),color = "black",topleft = (460,10))
                player.draw()
                diamond.draw()  
                screen.draw.filled_rect(return_button,(255,255,255))
                screen.draw.text("<-",color = "black",topleft = (10,10))  
                screen.draw.filled_rect(tat_nhac_button,(255,255,255))
                screen.draw.text("Stop music",color = "black",topleft = (5,570))
                screen.draw.filled_rect(bat_nhac_button,(255,255,255))
                screen.draw.text("Play music",color = "black",topleft = (1105,570))
                if diamond_easy == True:
                    screen.draw.text("Mode: Easy",color = "black",topleft = (1060,10))
                if diamond_normal == True:
                    screen.draw.text("Mode: Normal",color = "black",topleft = (1060,10))
                if diamond_hard == True:
                    screen.draw.text("Mode: Hard",color = "black",topleft = (1060,10))



            #level 7
            if score >= 600 and score <= 695:           
                screen.clear()
                level = 7
                screen.blit("bg_forest_night",(bg_x,0))
                screen.blit("bg_forest_night",(bg_x + 1200,0))
                screen.draw.filled_rect(floor,(255,0,0))        
                for i in rects:
                    screen.draw.filled_rect(i,(41,59,222))
                screen.draw.text("Score: "+str(score),color = "black",topleft = (40,10))
                screen.draw.text("Level: "+str(level),color = "black",topleft = (250,10))    
                screen.draw.text("Live: "+str(live),color = "black",topleft = (460,10))
                player.draw()
                diamond.draw()
                screen.draw.filled_rect(return_button,(255,255,255))
                screen.draw.text("<-",color = "black",topleft = (10,10))
                screen.draw.filled_rect(tat_nhac_button,(255,255,255))
                screen.draw.text("Stop music",color = "black",topleft = (5,570))
                screen.draw.filled_rect(bat_nhac_button,(255,255,255))
                screen.draw.text("Play music",color = "black",topleft = (1105,570))
                if diamond_easy == True:
                    screen.draw.text("Mode: Easy",color = "black",topleft = (1060,10))
                if diamond_normal == True:
                    screen.draw.text("Mode: Normal",color = "black",topleft = (1060,10))
                if diamond_hard == True:
                    screen.draw.text("Mode: Hard",color = "black",topleft = (1060,10))



            #level 8
            if score >= 700 and score <= 795:           
                screen.clear()
                screen.fill((255,255,255))
                level = 8
                screen.blit("bg_cave",(bg_x,0))
                screen.blit("bg_cave",(bg_x + 1200,0))
                screen.draw.filled_rect(floor,(255,0,0))        
                for i in rects:
                    screen.draw.filled_rect(i,(41,59,222))
                screen.draw.text("Score: "+str(score),color = "white",topleft = (40,10))
                screen.draw.text("Level: "+str(level),color = "white",topleft = (250,10))    
                screen.draw.text("Live: "+str(live),color = "white",topleft = (460,10))
                player.draw()
                diamond.draw()
                screen.draw.filled_rect(return_button,(255,255,255))
                screen.draw.text("<-",color = "black",topleft = (10,10))
                screen.draw.filled_rect(tat_nhac_button,(255,255,255))
                screen.draw.text("Stop music",color = "black",topleft = (5,570))
                screen.draw.filled_rect(bat_nhac_button,(255,255,255))
                screen.draw.text("Play music",color = "black",topleft = (1105,570))
                if diamond_easy == True:
                    screen.draw.text("Mode: Easy",color = "white",topleft = (1060,10))
                if diamond_normal == True:
                    screen.draw.text("Mode: Normal",color = "white",topleft = (1060,10))
                if diamond_hard == True:
                    screen.draw.text("Mode: Hard",color = "white",topleft = (1060,10))


            #level 9
            if score >= 800 and score <= 895:           
                screen.clear()
                screen.fill((255,255,255))
                level = 9
                screen.blit("bg_gold_mine",(bg_x,0))
                screen.blit("bg_gold_mine",(bg_x + 1200,0))
                screen.draw.filled_rect(floor,(255,0,0))        
                for i in rects:
                    screen.draw.filled_rect(i,(41,59,222))
                screen.draw.text("Score: "+str(score),color = "white",topleft = (40,10))
                screen.draw.text("Level: "+str(level),color = "white",topleft = (250,10))    
                screen.draw.text("Live: "+str(live),color = "white",topleft = (460,10))
                player.draw()
                diamond.draw()
                screen.draw.filled_rect(return_button,(255,255,255))
                screen.draw.text("<-",color = "black",topleft = (10,10))
                screen.draw.filled_rect(tat_nhac_button,(255,255,255))
                screen.draw.text("Stop music",color = "black",topleft = (5,570))
                screen.draw.filled_rect(bat_nhac_button,(255,255,255))
                screen.draw.text("Play music",color = "black",topleft = (1105,570))
                if diamond_easy == True:
                    screen.draw.text("Mode: Easy",color = "white",topleft = (1060,10))
                if diamond_normal == True:
                    screen.draw.text("Mode: Normal",color = "white",topleft = (1060,10))
                if diamond_hard == True:
                    screen.draw.text("Mode: Hard",color = "white",topleft = (1060,10))


            #level 10
            if score >= 900 and score <= 995:
                screen.clear()
                screen.fill((255,255,255))
                level = 10
                screen.blit("bg_level_10",(bg_x,0))
                screen.blit("bg_level_10",(bg_x + 1200,0))
                screen.draw.filled_rect(floor,(255,0,0))        
                for i in rects:
                    screen.draw.filled_rect(i,(255,255,255))
                screen.draw.text("Score: "+str(score),color = "white",topleft = (40,10))
                screen.draw.text("Level: "+str(level),color = "white",topleft = (250,10))    
                screen.draw.text("Live: "+str(live),color = "white",topleft = (460,10))
                player.draw()
                diamond.draw()
                enemy.draw()                    
                enemy.angle = -90
                screen.draw.filled_rect(return_button,(255,255,255))
                screen.draw.text("<-",color = "black",topleft = (10,10))
                screen.draw.filled_rect(tat_nhac_button,(255,255,255))
                screen.draw.text("Stop music",color = "black",topleft = (5,570))
                screen.draw.filled_rect(bat_nhac_button,(255,255,255))
                screen.draw.text("Play music",color = "black",topleft = (1105,570))
                if diamond_easy == True:
                    screen.draw.text("Mode: Easy",color = "white",topleft = (1060,10))
                if diamond_normal == True:
                    screen.draw.text("Mode: Normal",color = "white",topleft = (1060,10))
                if diamond_hard == True:
                    screen.draw.text("Mode: Hard",color = "white",topleft = (1060,10))    
                       
                    

            #level 11
            if score >= 1000 and score <= 1095:               
                screen.clear()
                screen.fill((255,255,255))
                level = 11
                screen.blit("bg_level_11",(bg_x,0))
                screen.blit("bg_level_11",(bg_x + 1200,0))
                screen.draw.filled_rect(floor,(255,0,0))        
                for i in rects:
                    screen.draw.filled_rect(i,(255,255,255))
                screen.draw.text("Score: "+str(score),color = "white",topleft = (40,10))
                screen.draw.text("Level: "+str(level),color = "white",topleft = (250,10))    
                screen.draw.text("Live: "+str(live),color = "white",topleft = (460,10))
                player.draw()
                diamond.draw()
                enemy.draw()                    
                enemy.angle = -90
                screen.draw.filled_rect(return_button,(255,255,255))
                screen.draw.text("<-",color = "black",topleft = (10,10))
                screen.draw.filled_rect(tat_nhac_button,(255,255,255))
                screen.draw.text("Stop music",color = "black",topleft = (5,570))
                screen.draw.filled_rect(bat_nhac_button,(255,255,255))
                screen.draw.text("Play music",color = "black",topleft = (1105,570))
                if diamond_easy == True:
                    screen.draw.text("Mode: Easy",color = "white",topleft = (1060,10))
                if diamond_normal == True:
                    screen.draw.text("Mode: Normal",color = "white",topleft = (1060,10))
                if diamond_hard == True:
                    screen.draw.text("Mode: Hard",color = "white",topleft = (1060,10))

            #level 12
            if score >= 1100 and score <= 1195:               
                screen.clear()
                screen.fill((255,255,255))
                level = 12
                screen.blit("bg_level_12",(bg_x,0))
                screen.blit("bg_level_12",(bg_x + 1200,0))
                screen.draw.filled_rect(floor,(255,0,0))        
                for i in rects:
                    screen.draw.filled_rect(i,(255,255,255))
                screen.draw.text("Score: "+str(score),color = "white",topleft = (40,10))
                screen.draw.text("Level: "+str(level),color = "white",topleft = (250,10))    
                screen.draw.text("Live: "+str(live),color = "white",topleft = (460,10))
                player.draw()
                diamond.draw()
                enemy.draw()                    
                enemy.angle = -90
                screen.draw.filled_rect(return_button,(255,255,255))
                screen.draw.text("<-",color = "black",topleft = (10,10))
                screen.draw.filled_rect(tat_nhac_button,(255,255,255))
                screen.draw.text("Stop music",color = "black",topleft = (5,570))
                screen.draw.filled_rect(bat_nhac_button,(255,255,255))
                screen.draw.text("Play music",color = "black",topleft = (1105,570))
                if diamond_easy == True:
                    screen.draw.text("Mode: Easy",color = "white",topleft = (1060,10))
                if diamond_normal == True:
                    screen.draw.text("Mode: Normal",color = "white",topleft = (1060,10))
                if diamond_hard == True:
                    screen.draw.text("Mode: Hard",color = "white",topleft = (1060,10))

            #level 13
            if score >= 1200 and score <= 1295:               
                screen.clear()
                screen.fill((255,255,255))
                level = 13
                screen.blit("bg_level_13",(bg_x,0))
                screen.blit("bg_level_13",(bg_x + 1200,0))
                screen.draw.filled_rect(floor,(255,0,0))        
                for i in rects:
                    screen.draw.filled_rect(i,(117,82,80))
                screen.draw.text("Score: "+str(score),color = "white",topleft = (40,10))
                screen.draw.text("Level: "+str(level),color = "white",topleft = (250,10))    
                screen.draw.text("Live: "+str(live),color = "white",topleft = (460,10))
                player.draw()
                diamond.draw()
                enemy.draw()                    
                enemy.angle = -90
                screen.draw.filled_rect(return_button,(255,255,255))
                screen.draw.text("<-",color = "black",topleft = (10,10))
                screen.draw.filled_rect(tat_nhac_button,(255,255,255))
                screen.draw.text("Stop music",color = "black",topleft = (5,570))
                screen.draw.filled_rect(bat_nhac_button,(255,255,255))
                screen.draw.text("Play music",color = "black",topleft = (1105,570))
                if diamond_easy == True:
                    screen.draw.text("Mode: Easy",color = "white",topleft = (1060,10))
                if diamond_normal == True:
                    screen.draw.text("Mode: Normal",color = "white",topleft = (1060,10))
                if diamond_hard == True:
                    screen.draw.text("Mode: Hard",color = "white",topleft = (1060,10))

            #level 14
            if score >= 1300 and score <= 1395:               
                screen.clear()
                screen.fill((255,255,255))
                level = 14
                screen.blit("bg_level_14",(bg_x,0))
                screen.blit("bg_level_14",(bg_x + 1200,0))
                screen.draw.filled_rect(floor,(255,0,0))        
                for i in rects:
                    screen.draw.filled_rect(i,(117,82,80))
                screen.draw.text("Score: "+str(score),color = "white",topleft = (40,10))
                screen.draw.text("Level: "+str(level),color = "white",topleft = (250,10))    
                screen.draw.text("Live: "+str(live),color = "white",topleft = (460,10))
                player.draw()
                diamond.draw()
                enemy.draw()                    
                enemy.angle = -90
                screen.draw.filled_rect(return_button,(255,255,255))
                screen.draw.text("<-",color = "black",topleft = (10,10))
                screen.draw.filled_rect(tat_nhac_button,(255,255,255))
                screen.draw.text("Stop music",color = "black",topleft = (5,570))
                screen.draw.filled_rect(bat_nhac_button,(255,255,255))
                screen.draw.text("Play music",color = "black",topleft = (1105,570))
                if diamond_easy == True:
                    screen.draw.text("Mode: Easy",color = "white",topleft = (1060,10))
                if diamond_normal == True:
                    screen.draw.text("Mode: Normal",color = "white",topleft = (1060,10))
                if diamond_hard == True:
                    screen.draw.text("Mode: Hard",color = "white",topleft = (1060,10))

            #level 15
            if score >= 1400 and score <= 1495:               
                screen.clear()
                screen.fill((255,255,255))
                level = 15
                screen.blit("bg_level_15",(bg_x,0))
                screen.blit("bg_level_15",(bg_x + 1200,0))
                screen.draw.filled_rect(floor,(255,0,0))        
                for i in rects:
                    screen.draw.filled_rect(i,(110,255,74))
                screen.draw.text("Score: "+str(score),color = "black",topleft = (40,10))
                screen.draw.text("Level: "+str(level),color = "black",topleft = (250,10))    
                screen.draw.text("Live: "+str(live),color = "black",topleft = (460,10))
                player.draw()
                diamond.draw()
                enemy.draw()                    
                enemy.angle = -90
                screen.draw.filled_rect(return_button,(255,255,255))
                screen.draw.text("<-",color = "black",topleft = (10,10))
                screen.draw.filled_rect(tat_nhac_button,(255,255,255))
                screen.draw.text("Stop music",color = "black",topleft = (5,570))
                screen.draw.filled_rect(bat_nhac_button,(255,255,255))
                screen.draw.text("Play music",color = "black",topleft = (1105,570))
                if diamond_easy == True:
                    screen.draw.text("Mode: Easy",color = "black",topleft = (1060,10))
                if diamond_normal == True:
                    screen.draw.text("Mode: Normal",color = "black",topleft = (1060,10))
                if diamond_hard == True:
                    screen.draw.text("Mode: Hard",color = "black",topleft = (1060,10))

            #level 16
            if score >= 1500 and score <= 1595:               
                screen.clear()
                screen.fill((255,255,255))
                level = 16
                screen.blit("bg_level_16",(bg_x,0))
                screen.blit("bg_level_16",(bg_x + 1200,0))
                screen.draw.filled_rect(floor,(255,0,0))        
                for i in rects:
                    screen.draw.filled_rect(i,(255,255,255))
                screen.draw.text("Score: "+str(score),color = "white",topleft = (40,10))
                screen.draw.text("Level: "+str(level),color = "white",topleft = (250,10))    
                screen.draw.text("Live: "+str(live),color = "white",topleft = (460,10))
                player.draw()
                diamond.draw()
                enemy.draw()                    
                enemy.angle = -90
                screen.draw.filled_rect(return_button,(255,255,255))
                screen.draw.text("<-",color = "black",topleft = (10,10))
                screen.draw.filled_rect(tat_nhac_button,(255,255,255))
                screen.draw.text("Stop music",color = "black",topleft = (5,570))
                screen.draw.filled_rect(bat_nhac_button,(255,255,255))
                screen.draw.text("Play music",color = "black",topleft = (1105,570))
                if diamond_easy == True:
                    screen.draw.text("Mode: Easy",color = "white",topleft = (1060,10))
                if diamond_normal == True:
                    screen.draw.text("Mode: Normal",color = "white",topleft = (1060,10))
                if diamond_hard == True:
                    screen.draw.text("Mode: Hard",color = "white",topleft = (1060,10))

            #level 17
            if score >= 1600 and score <= 1695:               
                screen.clear()
                screen.fill((255,255,255))
                level = 17
                screen.blit("bg_level_17",(bg_x,0))
                screen.blit("bg_level_17",(bg_x + 1200,0))
                screen.draw.filled_rect(floor,(255,0,0))        
                for i in rects:
                    screen.draw.filled_rect(i,(255,255,255))
                screen.draw.text("Score: "+str(score),color = "black",topleft = (40,10))
                screen.draw.text("Level: "+str(level),color = "black",topleft = (250,10))    
                screen.draw.text("Live: "+str(live),color = "black",topleft = (460,10))
                player.draw()
                diamond.draw()
                enemy.draw()                    
                enemy.angle = -90
                screen.draw.filled_rect(return_button,(255,255,255))
                screen.draw.text("<-",color = "black",topleft = (10,10))
                screen.draw.filled_rect(tat_nhac_button,(255,255,255))
                screen.draw.text("Stop music",color = "black",topleft = (5,570))
                screen.draw.filled_rect(bat_nhac_button,(255,255,255))
                screen.draw.text("Play music",color = "black",topleft = (1105,570))
                if diamond_easy == True:
                    screen.draw.text("Mode: Easy",color = "black",topleft = (1060,10))
                if diamond_normal == True:
                    screen.draw.text("Mode: Normal",color = "black",topleft = (1060,10))
                if diamond_hard == True:
                    screen.draw.text("Mode: Hard",color = "black",topleft = (1060,10))

            #level 18
            if score >= 1700 and score <= 1795:               
                screen.clear()
                screen.fill((255,255,255))
                level = 18
                screen.blit("bg_level_18",(bg_x,0))
                screen.blit("bg_level_18",(bg_x + 1200,0))
                screen.draw.filled_rect(floor,(255,0,0))        
                for i in rects:
                    screen.draw.filled_rect(i,(0,255,0))
                screen.draw.text("Score: "+str(score),color = "black",topleft = (40,10))
                screen.draw.text("Level: "+str(level),color = "black",topleft = (250,10))    
                screen.draw.text("Live: "+str(live),color = "black",topleft = (460,10))
                player.draw()
                diamond.draw()
                enemy.draw()                    
                enemy.angle = -90
                screen.draw.filled_rect(return_button,(255,255,255))
                screen.draw.text("<-",color = "black",topleft = (10,10))
                screen.draw.filled_rect(tat_nhac_button,(255,255,255))
                screen.draw.text("Stop music",color = "black",topleft = (5,570))
                screen.draw.filled_rect(bat_nhac_button,(255,255,255))
                screen.draw.text("Play music",color = "black",topleft = (1105,570))
                if diamond_easy == True:
                    screen.draw.text("Mode: Easy",color = "black",topleft = (1060,10))
                if diamond_normal == True:
                    screen.draw.text("Mode: Normal",color = "black",topleft = (1060,10))
                if diamond_hard == True:
                    screen.draw.text("Mode: Hard",color = "black",topleft = (1060,10))

            #level 19
            if score >= 1800 and score <= 1895:               
                screen.clear()
                screen.fill((255,255,255))
                level = 19
                screen.blit("bg_level_19",(bg_x,0))
                screen.blit("bg_level_19",(bg_x + 1200,0))
                screen.draw.filled_rect(floor,(255,0,0))        
                for i in rects:
                    screen.draw.filled_rect(i,(0,255,0))
                screen.draw.text("Score: "+str(score),color = "black",topleft = (40,10))
                screen.draw.text("Level: "+str(level),color = "black",topleft = (250,10))    
                screen.draw.text("Live: "+str(live),color = "black",topleft = (460,10))
                player.draw()
                diamond.draw()
                enemy.draw()                    
                enemy.angle = -90
                screen.draw.filled_rect(return_button,(255,255,255))
                screen.draw.text("<-",color = "black",topleft = (10,10))
                screen.draw.filled_rect(tat_nhac_button,(255,255,255))
                screen.draw.text("Stop music",color = "black",topleft = (5,570))
                screen.draw.filled_rect(bat_nhac_button,(255,255,255))
                screen.draw.text("Play music",color = "black",topleft = (1105,570))
                if diamond_easy == True:
                    screen.draw.text("Mode: Easy",color = "black",topleft = (1060,10))
                if diamond_normal == True:
                    screen.draw.text("Mode: Normal",color = "black",topleft = (1060,10))
                if diamond_hard == True:
                    screen.draw.text("Mode: Hard",color = "black",topleft = (1060,10))

            #level 20
            if score >= 1900 and score <= 1995:               
                screen.clear()
                screen.fill((255,255,255))
                level = 20
                screen.blit("bg_level_20",(bg_x,0))
                screen.blit("bg_level_20",(bg_x + 1200,0))
                screen.draw.filled_rect(floor,(255,0,0))        
                for i in rects:
                    screen.draw.filled_rect(i,(255,255,255))
                screen.draw.text("Score: "+str(score),color = "black",topleft = (40,10))
                screen.draw.text("Level: "+str(level),color = "black",topleft = (250,10))    
                screen.draw.text("Live: "+str(live),color = "black",topleft = (460,10))
                player.draw()
                diamond.draw()
                enemy.draw()                    
                enemy.angle = -90
                screen.draw.filled_rect(return_button,(255,255,255))
                screen.draw.text("<-",color = "black",topleft = (10,10))
                screen.draw.filled_rect(tat_nhac_button,(255,255,255))
                screen.draw.text("Stop music",color = "black",topleft = (5,570))
                screen.draw.filled_rect(bat_nhac_button,(255,255,255))
                screen.draw.text("Play music",color = "black",topleft = (1105,570))
                if diamond_easy == True:
                    screen.draw.text("Mode: Easy",color = "black",topleft = (1060,10))
                if diamond_normal == True:
                    screen.draw.text("Mode: Normal",color = "black",topleft = (1060,10))
                if diamond_hard == True:
                    screen.draw.text("Mode: Hard",color = "black",topleft = (1060,10))



            if score >= 2000: 
                if c == True:
                    music.play("win")  
                    c = False
                screen.fill((0,0,0))
                screen.draw.text("You win!",color = "black",topleft = (590,300))
                screen.draw.filled_rect(return_button,(255,255,255))
                screen.draw.text("<-",color = "black",topleft = (10,10)) 

        
        if live <= 0:          
            if d == True:
                music.play("lose")
                d = False                 
            screen.fill((0,0,0))
            score = 0
            screen.draw.filled_rect(restart_button,(255,255,255))
            screen.draw.text("You lose!",color = "white",topleft = (615,270))
            screen.draw.text("Restart",color = "black",topleft = (615,520))     
            

    def update():        
        global bg_x, gravity, level, score, live, data_score, coins 

        if score >= 2000:
            player.y = 999999999999999999999999999999999              

        if score >= 900 and score <= 9995:                            
            enemy.x -= 4
            if player.colliderect(enemy):
                live -= 1
                player.x = 200
                player.y = 300
                place_enemy()
            if enemy.x <= -80:
                place_enemy()
            

        if player.x >= 400:
            bg_x -= 5
            enemy.x -= 5
            if bg_x + 1200 <= 0:
                bg_x = 0
            for i in rects:
                i.x -= 5
                if i.x <= -0:
                    i.x = 950        
            diamond.x -= 5
            if diamond.x <= 0:
                place_diamond()              
                

        if diamond_easy == True:
            screen.draw.text("Mode: Easy",color = "red",topleft = (250,10))
            if player.colliderect(diamond):
                data_score["score"] += 5 
                sounds.loot.play()          
                score += 5
                place_diamond()
            if player.colliderect(floor):
                data_score["score"] -= 5            
                score -= 5
                if score <= 0:
                    score = 0
                    player.x = 200
                    player.y = 300
                live -= 1
                player.x = 200
                player.y = 300
            if live <= 0:
                screen.fill((0,0,0))
                score = 0
                screen.draw.filled_rect(restart_button,(255,255,255))
                screen.draw.text("You lose!",color = "white",topleft = (615,270))
                screen.draw.text("Restart",color = "black",topleft = (615,310))

        if diamond_normal == True:
            if player.colliderect(diamond):
                data_score["score"] += 10   
                sounds.loot.play()               
                score += 10
                place_diamond()
            if player.colliderect(floor):
                data_score["score"] -= 10            
                score -= 10
                if score <= 0:
                    score = 0
                    player.x = 200
                    player.y = 300
                live -= 1
                player.x = 200
                player.y = 300
            if live <= 0:
                screen.fill((0,0,0))            
                screen.draw.filled_rect(restart_button,(255,255,255))
                screen.draw.text("You lose!",color = "white",topleft = (615,270))
                screen.draw.text("Restart",color = "black",topleft = (615,310))

        if diamond_hard == True:
            if player.colliderect(diamond):
                data_score["score"] += 20          
                score += 20
                sounds.loot.play()
                place_diamond()
            if player.colliderect(floor):
                data_score["score"] -= 20
                
                score -= 20
                if score <= 0:
                    score = 0
                    player.x = 200
                    player.y = 300
                live -= 1
                player.x = 200
                player.y = 300
            if live <= 0:
                screen.fill((0,0,0))
                score = 0
                screen.draw.filled_rect(restart_button,(255,255,255))
                screen.draw.text("You lose!",color = "white",topleft = (615,270))
                screen.draw.text("Restart",color = "black",topleft = (615,310))

        with open("score.txt","w") as score_file:
            json.dump(data_score,score_file)   

        with open("coins.txt","w") as coins_file:
            json.dump(coins,coins_file)

        player_move()


    def on_key_down(key):
        if key == keys.F:
            screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        elif key == keys.Q:            
            screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))


    def on_mouse_down(pos):
        global live, start, score, aboutme, huongdan, level, diamond_easy, diamond_hard, diamond_normal, thanhtich, nhiemvu, claim1, data_score, claim2, buy1, buy2, shopping, a, b, c, d

        if bat_nhac_button.collidepoint(pos):
            music.unpause()

        if tat_nhac_button.collidepoint(pos):
            music.pause()

        if shop_button.collidepoint(pos):
            shopping = True             

        if buy_button1.collidepoint(pos):
            claim1 = False
            claim2 = False
            if coins["coins"] >= 10:
                buy1 = True
            if coins["coins"] < 10:
                buy1 = False
            
        if buy_button2.collidepoint(pos):
            claim1 = False
            claim2 = False
            if coins["coins"] >= 20:
                buy2 = True
            if coins["coins"] < 20:
                buy2 = False
            
        if claim_button.collidepoint(pos): 
            buy1 = False
            buy2 = False        
            if int(data_score["score"]) >= 500:            
                claim1 = True
            if int(data_score["score"]) < 500:
                claim1 = False
                

        if claim_button2.collidepoint(pos):
            buy1 = False
            buy2 = False
            if int(data_score["score"]) >= 1000:
                claim2 = True
            if int(data_score["score"]) < 1000:
                claim2 = False
                

        if restart_button.collidepoint(pos):
            d = True
            
            if diamond_easy == True:
                live = 5
                music.play("legendary")
            if diamond_normal == True:
                live = 3
                music.play("legendary")
            if diamond_hard == True:
                live = 2
                music.play("legendary")


        if easy_button.collidepoint(pos):
            music.play("legendary")
            start = True
            diamond_easy = True
            diamond_normal = False
            diamond_hard = False
            live = 5
            score = 0
            player.x = 200
            player.y = 300
            

        if normal_button.collidepoint(pos):
            music.play("legendary")
            start = True
            diamond_normal = True
            diamond_easy = False
            diamond_hard = False
            live = 3
            score = 0
            player.x = 200
            player.y = 300
            
        if hard_button.collidepoint(pos):
            music.play("legendary")
            start = True
            diamond_hard = True
            diamond_normal = False
            diamond_easy = False
            live = 2
            score = 0
            player.x = 200
            player.y = 300
            
        
        if return_button.collidepoint(pos):
            start = False
            aboutme = False        
            huongdan = False
            thanhtich = False
            nhiemvu = False
            shopping = False
            c = True
            music.stop()

        if aboutme_button.collidepoint(pos):
            aboutme = True   

        if nut_huong_dan.collidepoint(pos):
            huongdan = True

        if nut_thanh_tich.collidepoint(pos):
            thanhtich = True

        if nut_nhiem_vu.collidepoint(pos):
            nhiemvu = True

    
    def collidecheck():
        collide = False
        for i in rects:
            if player.colliderect(i) or player.colliderect(floor):
                collide = True    
        return collide

    def place_enemy():
        enemy.x = randint(1000,1200)
        enemy.y = randint(100,500)

    def place_diamond():
        diamond.x = randint(410, (WIDTH - 200))
        diamond.y = randint(200, (HEIGHT - 200))



    def player_move():
        global gravity, score, live, buy1, buy2, a, b, bg_x
        if not collidecheck():        
            if b == False:
                player.y += gravity
                if gravity < 20:
                    gravity += 0.5
                player.image = "jumper-fall"

            if b == True:
                gravity = 10
                player.y += gravity
                if gravity < 20:
                    gravity += 0.5 
                player.image = "jumper-fall"
            
            
            

        if collidecheck():
            gravity = 1
            player.image = "jumper-1"
        
        #move left
        if keyboard.left and a == True:        
            player.x -= 6        
            player.image = "jumper-left"    
        if keyboard.left and not a:
            player.x -= 5
            
            player.image = "jumper-left"
            
            
        #move right 
        if keyboard.right and a == True:
            player.x += 6
            
            player.image = "jumper-right"    
        if keyboard.right and a == False:        
            player.x += 5
            
            player.image = "jumper-right" 

        #move up  
        if keyboard.space:
            if b == True:
                player.y -= 15
                player.image = "jumper-up"
            if b == False:
                player.y -= 10
                player.image = "jumper-up"
        
        if keyboard.space and keyboard.left:
            player.image = "jumper-jleft"
        if keyboard.space and keyboard.right:
            player.image = "jumper-jright"
        
 
 
        if player.x < -10 or player.x > 1210:
            player.x = 200
            player.y = 300


    pgzrun.go()

except Exception as bug:
    print(bug)