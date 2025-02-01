def winning(player_now):
    global points_1, points_2

    if series_no % 2!= 0:
        if dict_1.get(frame_1)==dict_1.get(frame_2)==dict_1.get(frame_3):# 1,2,3
            if dict_1.get(frame_1) == image_1:
                
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
                

        elif dict_1.get(frame_4)==dict_1.get(frame_5)==dict_1.get(frame_6):
            if dict_1.get(frame_4) == image_1:
                
                label_player_1.place(x = 45,y = 450)
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))
            else:
                label_player_2.place(x = 45,y = 450)
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_4,frame_5,frame_6)
            
            frame_4.config(bg = "light green")
            frame_5.config(bg = "light green")
            frame_6.config(bg = "light green")
                

        elif dict_1.get(frame_7)==dict_1.get(frame_8)==dict_1.get(frame_9):
            if dict_1.get(frame_7) == image_1:
                
                label_player_1.place(x = 45,y = 450)
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))
            else:
                label_player_2.place(x = 45,y = 450)
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_7,frame_8,frame_9)
            
            frame_7.config(bg = "light green")
            frame_8.config(bg = "light green")
            frame_9.config(bg = "light green")                
            

        elif dict_1.get(frame_1)==dict_1.get(frame_4)==dict_1.get(frame_7):
            if dict_1.get(frame_7) == image_1:
                
                label_player_1.place(x = 45,y = 450)
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))
            else:
                label_player_2.place(x = 45,y = 450)
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_1,frame_4,frame_7)
            
            frame_1.config(bg = "light green")
            frame_4.config(bg = "light green")
            frame_7.config(bg = "light green")
                

        elif dict_1.get(frame_2)==dict_1.get(frame_5)==dict_1.get(frame_8):
            if dict_1.get(frame_2) == image_1:
                
                label_player_1.place(x = 45,y = 450)
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))
            else:
                label_player_2.place(x = 45,y = 450)
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_2,frame_5,frame_8)
            
            frame_2.config(bg = "light green")
            frame_5.config(bg = "light green")
            frame_8.config(bg = "light green")
                
                
        elif dict_1.get(frame_3)==dict_1.get(frame_6)==dict_1.get(frame_9):
            if dict_1.get(frame_3) == image_1:
                
                label_player_1.place(x = 45,y = 450)
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))
            else:
                label_player_2.place(x = 45,y = 450)
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_3,frame_6,frame_9)
                
            frame_3.config(bg = "light green")
            frame_6.config(bg = "light green")
            frame_9.config(bg = "light green")
                

                
        elif dict_1.get(frame_1)==dict_1.get(frame_5)==dict_1.get(frame_9):
            if dict_1.get(frame_1) == image_1:
                
                label_player_1.place(x = 45,y = 450)
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))
            else:
                label_player_2.place(x = 45,y = 450)
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_1,frame_5,frame_9)
            
            frame_1.config(bg = "light green")
            frame_5.config(bg = "light green")
            frame_9.config(bg = "light green")
            
                
        elif dict_1.get(frame_3)==dict_1.get(frame_5)==dict_1.get(frame_7):
            if dict_1.get(frame_3) == image_1:
                
                label_player_1.place(x = 45,y = 450)
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))
            else:
                label_player_2.place(x = 45,y = 450)
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_3,frame_5,frame_7)
            
            frame_3.config(bg = "light green")
            frame_5.config(bg = "light green")
            frame_7.config(bg = "light green")

else:
        if dict_1.get(frame_1)==dict_1.get(frame_2)==dict_1.get(frame_3):# 1,2,3
            if dict_1.get(frame_1) == image_1:
                
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
                

        elif dict_1.get(frame_4)==dict_1.get(frame_5)==dict_1.get(frame_6):
            if dict_1.get(frame_4) == image_1:
                
                label_player_1.place(x = 45,y = 450)
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))
            else:
                label_player_2.place(x = 45,y = 450)
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_4,frame_5,frame_6)
            
            frame_4.config(bg = "light green")
            frame_5.config(bg = "light green")
            frame_6.config(bg = "light green")
                

        elif dict_1.get(frame_7)==dict_1.get(frame_8)==dict_1.get(frame_9):
            if dict_1.get(frame_7) == image_1:
                
                label_player_1.place(x = 45,y = 450)
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))
            else:
                label_player_2.place(x = 45,y = 450)
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_7,frame_8,frame_9)
            
            frame_7.config(bg = "light green")
            frame_8.config(bg = "light green")
            frame_9.config(bg = "light green")                
            

        elif dict_1.get(frame_1)==dict_1.get(frame_4)==dict_1.get(frame_7):
            if dict_1.get(frame_7) == image_1:
                
                label_player_1.place(x = 45,y = 450)
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))
            else:
                label_player_2.place(x = 45,y = 450)
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_1,frame_4,frame_7)
            
            frame_1.config(bg = "light green")
            frame_4.config(bg = "light green")
            frame_7.config(bg = "light green")
                

        elif dict_1.get(frame_2)==dict_1.get(frame_5)==dict_1.get(frame_8):
            if dict_1.get(frame_2) == image_1:
                
                label_player_1.place(x = 45,y = 450)
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))
            else:
                label_player_2.place(x = 45,y = 450)
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_2,frame_5,frame_8)
            
            frame_2.config(bg = "light green")
            frame_5.config(bg = "light green")
            frame_8.config(bg = "light green")
                
                
        elif dict_1.get(frame_3)==dict_1.get(frame_6)==dict_1.get(frame_9):
            if dict_1.get(frame_3) == image_1:
                
                label_player_1.place(x = 45,y = 450)
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))
            else:
                label_player_2.place(x = 45,y = 450)
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_3,frame_6,frame_9)
                
            frame_3.config(bg = "light green")
            frame_6.config(bg = "light green")
            frame_9.config(bg = "light green")
                

                
        elif dict_1.get(frame_1)==dict_1.get(frame_5)==dict_1.get(frame_9):
            if dict_1.get(frame_1) == image_1:
                
                label_player_1.place(x = 45,y = 450)
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))
            else:
                label_player_2.place(x = 45,y = 450)
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_1,frame_5,frame_9)
            
            frame_1.config(bg = "light green")
            frame_5.config(bg = "light green")
            frame_9.config(bg = "light green")
            
                
        elif dict_1.get(frame_3)==dict_1.get(frame_5)==dict_1.get(frame_7):
            if dict_1.get(frame_3) == image_1:
                
                label_player_1.place(x = 45,y = 450)
                points_1 += 1
                score_player_1.config(text = "Player 1: "+str(points_1))
            else:
                label_player_2.place(x = 45,y = 450)
                points_2 += 1
                score_player_2.config(text = "Player 2: "+str(points_2))
            button_next_game.place(x = 55, y = 500)
            button_next_game["command"] = lambda: clear_game(frame_3,frame_5,frame_7)
            
            frame_3.config(bg = "light green")
            frame_5.config(bg = "light green")
            frame_7.config(bg = "light green")    
        
            
            
