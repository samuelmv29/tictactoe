from tkinter import *
from PIL import Image,ImageTk
import tkinter.font as font

root = Tk()
root.geometry("900x600")
root.resizable(0,0)

canvas_starting = Canvas(root)
canvas_game = Canvas(root)

logo_font = font.Font(family = "Ariel Black",size = 70)
play_font = font.Font(family = "Ariel Black",size = 40)
user_font = font.Font(family = "Ariel Black",size = 50)
entry_font = font.Font(family = "Ariel Black", size = 20)



cross_0 = ImageTk.PhotoImage(Image.open("cross_1.png").resize((125,135)))
zero_0 = ImageTk.PhotoImage(Image.open("letter_o.png").resize((125,125)))

[cross_1,cross_2,cross_3,cross_4,cross_5] = [cross_0,cross_0,cross_0,cross_0,cross_0]
[zero_1,zero_2,zero_3,zero_4,zero_5] = [zero_0,zero_0,zero_0,zero_0,zero_0]
a = [cross_1,cross_2,cross_3,cross_4,cross_5]
b = [zero_1,zero_2,zero_3,zero_4,zero_5]

dict_1 ={}
num_x = 1
num_y = 1
number_of_turns = 0
points_1 = 0
points_2 = 0



def clear_game(frame_a,frame_b,frame_c):
    global num_x,num_y, dict_1, player_now, series_no, number_of_turns
    matrix = [frame_1,frame_2,frame_3,frame_4,frame_5,frame_6,frame_7,frame_8,frame_9]
    if frame_a != None:
        
        frame_a.config(bg = "SystemButtonFace")
        frame_b.config(bg = "SystemButtonFace")
        frame_c.config(bg = "SystemButtonFace")
    
    for i in matrix:
        print(i.winfo_children())
        if len(i.winfo_children()) == 1:
            ((i.winfo_children())[0]).destroy()
    label_player_1.place_forget()
    label_player_2.place_forget()
    tie_text.place_forget()
    button_next_game.place_forget()

    if series_no+1 > int(series.get()):
        frame_game_over = Frame(canvas_game, height = 550, width = 550)
        frame_game_over.place(x = 310, y = 20)
        game_over = Label(frame_game_over,text = "GAME OVER", font = entry_font)
        game_over.place(x = 215, y = 180)
        if points_1>points_2:
            winner_label_1 = Label(frame_game_over,text = "PLAYER 1 WON!", font = entry_font)
            winner_label_1.place(x = 200, y = 230)
        if points_2>points_1:
            winner_label_2 = Label(frame_game_over,text = "PLAYER 2 WON!", font = entry_font)
            winner_label_2.place(x = 200, y = 230)
        if points_1 == points_2:
            winner_label_tie = Label(frame_game_over,text = "TIE!", font = entry_font)
            winner_label_tie.place(x = 250, y = 230)
    else:
        series_no += 1
    
    game_number.config(text = "GAME NO. :"+" "+str(series_no), font = entry_font)
    
    num_x = 1
    num_y = 1
    dict_1 = {}

    number_of_turns = 0



def winning(player_now):
    global points_1, points_2

#image 1

    if series_no % 2!= 0:            
            if dict_1.get(frame_1)==dict_1.get(frame_2)==dict_1.get(frame_3): # 1,2,3
                if dict_1.get(frame_1)==dict_1.get(frame_2)==dict_1.get(frame_3)==image_1:
                
                    label_player_1.place(x = 45,y = 450)
                    points_1 += 1
                    score_player_1.config(text = "Player 1: "+str(points_1))
                else:
                    label_player_2.place(x = 45,y = 450)
                    points_2 += 1
                    score_player_2.config(text = "Player 2: "+str(points_2))
                    
                button_next_game.place(x = 55, y = 500)
                button_next_game["command"] = lambda: clear_game(frame_1,frame_2,frame_3)
                
                frame_1.config(bg = "light green")
                frame_2.config(bg = "light green")
                frame_3.config(bg = "light green")
            elif dict_1.get(frame_4)==dict_1.get(frame_5)==dict_1.get(frame_6)==image_1: # 4,5,6
                
                label_player_1.place(x = 45,y = 450)
                button_next_game.place(x = 55, y = 500)
                button_next_game["command"] = lambda: clear_game(frame_4,frame_5,frame_6)
                
                frame_4.config(bg = "light green")
                frame_5.config(bg = "light green")
                frame_6.config(bg = "light green")
                
            elif dict_1.get(frame_7)==dict_1.get(frame_8)==dict_1.get(frame_9)==image_1: #7,8,9
                label_player_1.place(x = 45,y = 450)
                button_next_game.place(x = 55, y = 500)
                button_next_game["command"] = lambda: clear_game(frame_7,frame_8,frame_9)
                
                frame_7.config(bg = "light green")
                frame_8.config(bg = "light green")
                frame_9.config(bg = "light green")                

            elif dict_1.get(frame_1)==dict_1.get(frame_4)==dict_1.get(frame_7)==image_1: #1,4,7
                label_player_1.place(x = 45,y = 450)
                button_next_game.place(x = 55, y = 500)
                button_next_game["command"] = lambda: clear_game(frame_1,frame_4,frame_7)
                
                frame_1.config(bg = "light green")
                frame_4.config(bg = "light green")
                frame_7.config(bg = "light green")

            elif dict_1.get(frame_2)==dict_1.get(frame_5)==dict_1.get(frame_8)==image_1: #2,5,8
            
                label_player_1.place(x = 45,y = 450)
                button_next_game.place(x = 55, y = 500)
                button_next_game["command"] = lambda: clear_game(frame_2,frame_5,frame_8)
                
                frame_2.config(bg = "light green")
                frame_5.config(bg = "light green")
                frame_8.config(bg = "light green")
        
        elif dict_1.get(frame_3)==dict_1.get(frame_6)==dict_1.get(frame_9)==image_1: #3,6,9
            
                label_player_1.place(x = 45,y = 450)
                button_next_game.place(x = 55, y = 500)
                button_next_game["command"] = lambda: clear_game(frame_3,frame_6,frame_9)
                
                frame_3.config(bg = "light green")
                frame_6.config(bg = "light green")
                frame_9.config(bg = "light green")
        
        elif dict_1.get(frame_1)==dict_1.get(frame_5)==dict_1.get(frame_9)==image_1: #1,5,9
            
                label_player_1.place(x = 45,y = 450)
                button_next_game.place(x = 55, y = 500)
                button_next_game["command"] = lambda: clear_game(frame_1,frame_5,frame_9)
                
                frame_1.config(bg = "light green")
                frame_5.config(bg = "light green")
                frame_9.config(bg = "light green")


        elif dict_1.get(frame_3)==dict_1.get(frame_5)==dict_1.get(frame_7)==image_1: #3,5,7

                label_player_1.place(x = 45,y = 450)
                button_next_game.place(x = 55, y = 500)
                button_next_game["command"] = lambda: clear_game(frame_3,frame_5,frame_7)
                
                frame_3.config(bg = "light green")
                frame_5.config(bg = "light green")
                frame_7.config(bg = "light green")






            
        else:
            if dict_1.get(frame_1)==dict_1.get(frame_2)==dict_1.get(frame_3)==image_2:
                label_player_2.place(x = 45,y = 450)

        
            
            if series_no % 2== 0:
                label_player_2.place(x = 45,y = 450)
            else:
                label_player_1.place(x = 45,y = 450)
            
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_1,frame_2,frame_3)

            if series_no % 2 == 0:
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))
            else:
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))
            
            frame_1.config(bg = "light green")
            frame_2.config(bg = "light green")
            frame_3.config(bg = "light green")

        elif dict_1.get(frame_4)==dict_1.get(frame_5)==dict_1.get(frame_6)==image_1:
            if series_no % 2== 0:
                label_player_2.place(x = 45,y = 450)
            else:
                label_player_1.place(x = 45,y = 450)
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_4,frame_5,frame_6)
            if series_no % 2 == 0:
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))
            else:
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))            
            frame_4.config(bg = "light green")
            frame_5.config(bg = "light green")
            frame_6.config(bg = "light green")

            

        elif dict_1.get(frame_7)==dict_1.get(frame_8)==dict_1.get(frame_9)==image_1:
            
            if series_no % 2== 0:
                label_player_2.place(x = 45,y = 450)
            else:
                label_player_1.place(x = 45,y = 450)
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_7,frame_8,frame_9)
            if series_no % 2 == 0:
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))
            else:
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))            
            frame_7.config(bg = "light green")
            frame_8.config(bg = "light green")
            frame_9.config(bg = "light green")
        elif dict_1.get(frame_1)==dict_1.get(frame_4)==dict_1.get(frame_7)==image_1:

            if series_no % 2== 0:
                label_player_2.place(x = 45,y = 450)
            else:
                label_player_1.place(x = 45,y = 450)
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_1,frame_4,frame_7)
            if series_no % 2 == 0:
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))
            else:
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))            
            frame_1.config(bg = "light green")
            frame_4.config(bg = "light green")
            frame_7.config(bg = "light green")
        elif dict_1.get(frame_2)==dict_1.get(frame_5)==dict_1.get(frame_8)==image_1:
            
            if series_no % 2== 0:
                label_player_2.place(x = 45,y = 450)
            else:
                label_player_1.place(x = 45,y = 450)
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_2,frame_5,frame_8)
            if series_no % 2 == 0:
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))
            else:
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))            
            frame_2.config(bg = "light green")
            frame_5.config(bg = "light green")
            frame_8.config(bg = "light green")
        elif dict_1.get(frame_3)==dict_1.get(frame_6)==dict_1.get(frame_9)==image_1:
            
            if series_no % 2== 0:
                label_player_2.place(x = 45,y = 450)
            else:
                label_player_1.place(x = 45,y = 450)
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_3,frame_6,frame_9)
            if series_no % 2 == 0:
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))
            else:
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))            
            frame_3.config(bg = "light green")
            frame_6.config(bg = "light green")
            frame_9.config(bg = "light green")
        elif dict_1.get(frame_1)==dict_1.get(frame_5)==dict_1.get(frame_9)==image_1:

            if series_no % 2== 0:
                label_player_2.place(x = 45,y = 450)
            else:
                label_player_1.place(x = 45,y = 450)
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_1,frame_5,frame_9)
            if series_no % 2 == 0:
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))
            else:
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))            
            frame_1.config(bg = "light green")
            frame_5.config(bg = "light green")
            frame_9.config(bg = "light green")
        elif dict_1.get(frame_3)==dict_1.get(frame_5)==dict_1.get(frame_7)==image_1:

            if series_no % 2== 0:
                label_player_2.place(x = 45,y = 450)
            else:
                label_player_1.place(x = 45,y = 450)
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_3,frame_5,frame_7)
            if series_no % 2 == 0:
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))
            else:
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))            
            frame_3.config(bg = "light green")
            frame_5.config(bg = "light green")
            frame_7.config(bg = "light green")

        elif number_of_turns == 9:
            tie_text.place(x = 45,y = 450)
            button_next_game.place(x = 65, y = 500)
            button_next_game["command"] = lambda: clear_game(None,None,None)
            
    if player_now == False:
        
        if dict_1.get(frame_1)==dict_1.get(frame_2)==dict_1.get(frame_3)==image_2:
            
            if series_no % 2== 0:
                label_player_1.place(x = 45,y = 450)
            else:
                label_player_2.place(x = 45,y = 450)
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_1,frame_2,frame_3)
            if series_no % 2 == 0:
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))
            else:
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))            
            frame_1.config(bg = "light green")
            frame_2.config(bg = "light green")
            frame_3.config(bg = "light green")

        elif dict_1.get(frame_4)==dict_1.get(frame_5)==dict_1.get(frame_6)==image_2:
            
            if series_no % 2== 0:
                label_player_1.place(x = 45,y = 450)
            else:
                label_player_2.place(x = 45,y = 450)
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_4,frame_5,frame_6)
            if series_no % 2 == 0:
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))
            else:
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))               
            frame_4.config(bg = "light green")
            frame_5.config(bg = "light green")
            frame_6.config(bg = "light green")

            

        elif dict_1.get(frame_7)==dict_1.get(frame_8)==dict_1.get(frame_9)==image_2:
            
            if series_no % 2== 0:
                label_player_1.place(x = 45,y = 450)
            else:
                label_player_2.place(x = 45,y = 450)
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_7,frame_8,frame_9)
            if series_no % 2 == 0:
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))
            else:
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))               
            frame_7.config(bg = "light green")
            frame_8.config(bg = "light green")
            frame_9.config(bg = "light green")
        elif dict_1.get(frame_1)==dict_1.get(frame_4)==dict_1.get(frame_7)==image_2:

            if series_no % 2== 0:
                label_player_1.place(x = 45,y = 450)
            else:
                label_player_2.place(x = 45,y = 450)
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_1,frame_4,frame_7)
            if series_no % 2 == 0:
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))
            else:
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))               
            frame_1.config(bg = "light green")
            frame_4.config(bg = "light green")
            frame_7.config(bg = "light green")
        elif dict_1.get(frame_2)==dict_1.get(frame_5)==dict_1.get(frame_8)==image_2:
            
            if series_no % 2== 0:
                label_player_1.place(x = 45,y = 450)
            else:
                label_player_2.place(x = 45,y = 450)
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_2,frame_5,frame_8)
            if series_no % 2 == 0:
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))
            else:
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))               
            frame_2.config(bg = "light green")
            frame_5.config(bg = "light green")
            frame_8.config(bg = "light green")
        elif dict_1.get(frame_3)==dict_1.get(frame_6)==dict_1.get(frame_9)==image_2:
            
            if series_no % 2== 0:
                label_player_1.place(x = 45,y = 450)
            else:
                label_player_2.place(x = 45,y = 450)
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_3,frame_6,frame_9)
            if series_no % 2 == 0:
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))
            else:
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))               
            frame_3.config(bg = "light green")
            frame_6.config(bg = "light green")
            frame_9.config(bg = "light green")
        elif dict_1.get(frame_1)==dict_1.get(frame_5)==dict_1.get(frame_9)==image_2:

            if series_no % 2== 0:
                label_player_1.place(x = 45,y = 450)
            else:
                label_player_2.place(x = 45,y = 450)
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_1,frame_5,frame_9)
            if series_no % 2 == 0:
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))
            else:
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))               
            frame_1.config(bg = "light green")
            frame_5.config(bg = "light green")
            frame_9.config(bg = "light green")
        elif dict_1.get(frame_3)==dict_1.get(frame_5)==dict_1.get(frame_7)==image_2:

            if series_no % 2== 0:
                label_player_1.place(x = 45,y = 450)
            else:
                label_player_2.place(x = 45,y = 450)
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_3,frame_5,frame_7)
            if series_no % 2 == 0:
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))
            else:
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))               
            frame_3.config(bg = "light green")
            frame_5.config(bg = "light green")
            frame_7.config(bg = "light green")
        elif number_of_turns == 9:
            tie_text.place(x = 65,y = 450)
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(None,None,None)

def x_and_o(frame):
    global number_of_turns,num_x,num_y,player_now, image_1, image_2, label_pic, frame_1,frame_2,frame_3,frame_4,frame_5,frame_6,frame_7,frame_8,frame_9
    if frame not in dict_1:
        
        
        if player_now == True:
            if series_no % 2 != 0:
                
                image_1 = eval("cross_"+str(num_x))
                label_pic = Label(frame,image = image_1)
                dict_1[frame] = image_1
            else:
                image_2 = eval("zero_"+str(num_y))
                label_pic = Label(frame,image = image_2)
                dict_1[frame] = image_2
            

            label_pic.place(x = 10,y=8)
            
            number_of_turns += 1
            
            num_x+=1
            
            label_player1.config(text = "Player 1:"+" "+user_1.get(), font = entry_font)
            label_player2.config(text = "Player 2:"+" "+user_2.get()+" ←", font = entry_font)
            
            winning(player_now)
            player_now = False
            print(player_now)
        

        else:
            if series_no % 2 == 0:
                
                image_1 = eval("cross_"+str(num_x))
                label_pic = Label(frame,image = image_1)
                dict_1[frame] = image_1
            else:
                image_2 = eval("zero_"+str(num_y))
                label_pic = Label(frame,image = image_2)
                dict_1[frame] = image_2
                
            label_pic.place(x = 10,y=6)
            
            number_of_turns += 1 
            
            num_y+=1
            

            label_player2.config(text = "Player 2:"+" "+user_2.get(), font = entry_font)
            label_player1.config(text = "Player 1:"+" "+user_1.get()+" ←", font = entry_font)
            
            winning(player_now)
            player_now = True
            print(player_now)

        

               
def play(canvas_starting):
    global score_player_1,score_player_2,tie_text,player_now, series_no, game_number, frame_1, frame_2, frame_3, frame_4, frame_5, frame_6,frame_7, frame_8, frame_9, label_player_1, label_player_2, button_next_game, label_player1,label_player2
    
    canvas_starting.pack_forget()
    canvas_game.pack(fill = BOTH, expand = True)
    
                           #TRUE: PLAYER 1                   FALSE:PLAYER 2
    series_no = 1
    
    game_number = Label(text = "GAME NO. :"+" "+str(series_no), font = entry_font)
    game_number.place(x = 20,y = 50)
    label_player1 = Label(text = "Player 1:"+" "+user_1.get()+" ←", font = entry_font)
    label_player1.place(x= 10, y = 100)
    
    label_player2 = Label(canvas_game, text = "Player 2:"+" "+user_2.get(), font = entry_font)
    label_player2.place(x =10, y = 160)

    score_label = Label(canvas_game,text = "SCORE", font = entry_font)
    score_player_1 = Label(canvas_game,text = "Player 1: 0", font = entry_font)
    score_player_2 = Label(canvas_game,text = "Player 2: 0", font = entry_font)

    score_label.place(x = 20, y = 250)
    score_player_1.place(x = 10, y = 300)
    score_player_2.place(x = 10, y = 360)
    
    label_player_1 = Label(canvas_game,text = "Player 1 won!", font = entry_font)
    label_player_2 = Label(canvas_game,text = "Player 2 won!", font = entry_font)
    tie_text = Label(canvas_game,text = "TIE!", font = entry_font)
    button_next_game = Button(canvas_game, text = "Next Game", font = entry_font)


    canvas_game.create_line(302,0,302,900)

    frame_1 = Frame(canvas_game, width = 150, height = 150)
    frame_1.place(x = 350, y = 50)
    a = frame_1.bind('<Button-1>',lambda event:x_and_o(frame_1))



    frame_2 = Frame(canvas_game, width = 150, height = 150)
    frame_2.place(x = 510, y = 50)
    b = frame_2.bind('<Button-1>',lambda event:x_and_o(frame_2))

    frame_3 = Frame(canvas_game, width = 150, height = 150)
    frame_3.place(x = 670, y = 50)
    frame_3.bind('<Button-1>',lambda event:x_and_o(frame_3))

    frame_4 = Frame(canvas_game, width = 150, height = 150)
    frame_4.place(x = 350, y = 210)
    frame_4.bind('<Button-1>',lambda event:x_and_o(frame_4))

    frame_5 = Frame(canvas_game, width = 150, height = 150)
    frame_5.place(x = 510, y = 210)
    frame_5.bind('<Button-1>',lambda event:x_and_o(frame_5))

    frame_6 = Frame(canvas_game, width = 150, height = 150)
    frame_6.place(x = 670, y = 210)
    frame_6.bind('<Button-1>',lambda event:x_and_o(frame_6))

    frame_7 = Frame(canvas_game, width = 150, height = 150)
    frame_7.place(x = 350, y = 370)
    frame_7.bind('<Button-1>',lambda event:x_and_o(frame_7))

    frame_8 = Frame(canvas_game, width = 150, height = 150)
    frame_8.place(x = 510, y = 370)
    frame_8.bind('<Button-1>',lambda event:x_and_o(frame_8))
    
    frame_9 = Frame(canvas_game, width = 150, height = 150)
    frame_9.place(x = 670, y = 370)
    frame_9.bind('<Button-1>',lambda event:x_and_o(frame_9))
    

    canvas_game.create_line(505,40,505,530)
    canvas_game.create_line(665,40,665,530)
    
    canvas_game.create_line(350,205,822,205)
    canvas_game.create_line(350,365,822,365)
    

player_now = True  
canvas_starting = Canvas(root)
canvas_game = Canvas(root)
canvas_starting.pack(fill = BOTH, expand = True)


canvas_starting.create_text(450,100,text = "X AND O", font = logo_font)
canvas_starting.create_text(300,200,text = "USER 1:", font = user_font)
canvas_starting.create_text(300,300,text = "USER 2:", font = user_font)
canvas_starting.create_text(250,400,text = "SERIES OF: ", font = user_font)


user_1 = StringVar()
user_2 = StringVar()
series = StringVar()

username_1 = Entry(canvas_starting, text = user_1, font = entry_font)
username_1.place(x = 480, y = 180)

username_2 = Entry(canvas_starting, text = user_2, font = entry_font)
username_2.place(x = 480, y = 280)

series_entry = Entry(canvas_starting, text = series, font = entry_font)
series_entry.place(x = 480, y = 380)

play_button = Button(canvas_starting, text = "PLAY", font = play_font, command = lambda: play(canvas_starting))
play_button.place(x = 360, y = 450)

root.mainloop()
