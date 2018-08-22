
# coding: utf-8

# In[3]:


import random
from IPython.display import clear_output
def main_func():
    print("Welcome to game of tic tac tow")
    
    #global varibale declaration
    game_start_flag = False
    pressed_digit_flag = 0
    print_all_digit_flag = 10
    used_number_with_marker_dict = {}
    number_position_dict = {}
    triplet_search_dict = {}
    cell_used_counter = 0
    winner_flag = False
    
    #global varibale declaration ended
    p1 = input("Enter the name of first player: ")
    p2 = input("Enter the name of second player:")
    m1 = input(f"Mr.{p1}, Please select marker:(X/O) ")
    if(m1=="X"):
        m2 = "O"
    else:
        m2 = "X"
    player_details = player_information(p1,p2,m1,m2)
    grid_list = [" ","-"," ","-"," ","-"," ","\n","|"," ","|"," ","|"," ","|","\n"," ","-"," ","-"," ","-"," ","\n","|"," ","|"," ","|"," ","|","\n"," ","-"," ","-"," ","-"," ","\n","|"," ","|"," ","|"," ","|","\n"," ","-"," ","-"," ","-"," "]
    move_ahead_flag = input("Do you want to proceed to next step of game: (Y/N)")
    
    if move_ahead_flag.lower()=="y":
        move_ahead_flag = ""
        grid_display(grid_list)

        #number_position_dict initialization started
        number_position_dict = {1:9,2:11,3:13,4:25,5:27,6:29,7:41,8:43,9:45}
        #number_position_dict[1] = int(9)
        #number_position_dict[2] = int(11)
        #number_position_dict[3] = int(13)
        #number_position_dict[4] = int(25)
        #number_position_dict[5] = int(27)
        #number_position_dict[6] = int(29)
        #number_position_dict[7] = int(41)
        #number_position_dict[8] = int(43)
        #number_position_dict[9] = int(45)
        #number_position_initialization ended
        
        complete_grid_display_flag = input("For gaming, do you want to numbered grid to enter digits: (Y/N)")
        if complete_grid_display_flag.lower()=="y":
            grid_list = update_grid_list(grid_list,number_position_dict,print_all_digit_flag,used_number_with_marker_dict)
            grid_display(grid_list)
        
        move_ahead_flag = input("Do you want to proceed to next step: (Y/N)")
        if move_ahead_flag.lower()=="y":
            print("Lets start the game!!!")
            grid_list = update_grid_list(grid_list,number_position_dict,pressed_digit_flag,used_number_with_marker_dict)
            grid_display(grid_list)
            #triplet_search_dict initialization started
            triplet_search_dict[1] = [[2,3],[5,6],[4,7]]
            triplet_search_dict[2] = [[5,8],[1,3]]
            triplet_search_dict[3] = [[1,2],[6,9],[5,7]]
            triplet_search_dict[4] = [[1,7],[5,6]]
            triplet_search_dict[5] = [[2,8],[4,6]]
            triplet_search_dict[6] = [[3,9],[4,5]]
            triplet_search_dict[7] = [[1,4],[3,5],[8,9]]
            triplet_search_dict[8] = [[7,9],[2,5]]
            triplet_search_dict[9] = [[3,6],[7,8],[1,5]]
            #triplet_search_dict initialization ended
            
            #player_info started
            fp1 = player_details[0]
            fp2 = player_details[1]
            fm1 = player_details[2]
            fm2 = player_details[3]
            #player_info ended
            player_selection_counter = 1
            while cell_used_counter<10 and not winner_flag:
                if player_selection_counter%2==0:
                    cell_index = int(input(f"Mr.{fp2} Please enter the cell Number: "))
                    if cell_index in used_number_with_marker_dict:
                        print("Sorry Entered cell already has been used... Game ended")
                        break
                    else:
                        used_number_with_marker_dict[cell_index] = fm2
                else:
                    cell_index = int(input(f"Mr.{fp1} Please enter the cell Number: "))
                    if cell_index in used_number_with_marker_dict:
                        print("Sorry Entered cell already has been used... Game ended")
                        break
                    else:
                        used_number_with_marker_dict[cell_index] = fm1
                
                grid_list = update_grid_list(grid_list,number_position_dict,cell_index,used_number_with_marker_dict)
                grid_display(grid_list)
                cell_used_counter+=1
                if cell_used_counter>4:
                    winner_details = check_winner_status(triplet_search_dict,used_number_with_marker_dict,cell_index)
                    if type(winner_details[0])==str:
                        winner_flag = True
                        if winner_details[0]==fm1:
                            print(f"The winner of the game is: {fp1}")
                        else:
                            print(f"The winner of game is: {fp2}")
                        break
                #increment player_selection_counter below
                player_selection_counter+=1
            if cell_used_counter==10 and not winner_flag:
                print("There is no winner in this game...Thanks for playing")
            input("Please give us feedback about game!!")
                        
        else:
            print("Thanks for playing !!!")
    else:
        print("Thank you for playing!!!")
    

def player_information(p1,p2,m1,m2):
    clear_output()
    print("Player information is as follows: ")
    random_number = random.randint(1,100001)
    if random_number%2==0:
        fp1=p2
        fp2 = p1
        fm1 = m2
        fm2 = m1
    else:
        fp1 = p1
        fp2 = p2
        fm1 = m1
        fm2 = m2
    print(f"First Player is: {fp1} and his/her marking is: {fm1}")
    print(f"Second player is: {fp2} and his/her marking is: {fm2}")
    player_details = [fp1,fp2,fm1,fm2]
    return player_details

def grid_display(grid_list):
    clear_output()
    print("The current grid for the game is as follows:")
    for i in range (0,len(grid_list)):
        print(grid_list[i],end="")

def update_grid_list(grid_list,number_position_dict,cell_index,used_number_with_marker_dict):
    if cell_index==10:
        for key,val in number_position_dict.items():
            grid_list[val] = key
    elif cell_index==0:
        grid_list = [" ","-"," ","-"," ","-"," ","\n","|"," ","|"," ","|"," ","|","\n"," ","-"," ","-"," ","-"," ","\n","|"," ","|"," ","|"," ","|","\n"," ","-"," ","-"," ","-"," ","\n","|"," ","|"," ","|"," ","|","\n"," ","-"," ","-"," ","-"," "]
    else:
        marker = used_number_with_marker_dict[cell_index]
        print(type(cell_index))
        if cell_index in number_position_dict:
            print("key is present in dict")
        position = number_position_dict.get(cell_index)
        print(position)
        grid_list[position] = marker
    return grid_list

def check_winner_status(triplet_search_dict,used_number_with_marker_dict,cell_index):
    marker_to_be_search = used_number_with_marker_dict[cell_index]
    search_list = triplet_search_dict[cell_index]
    for i in range(0,len(search_list)):
        winner_flag = True
        for j in range(0,2):
            if search_list[i][j] in used_number_with_marker_dict:
                if used_number_with_marker_dict[search_list[i][j]]!=marker_to_be_search:
                    winner_flag=False
                    break
            else:
                winner_flag=False
                break
        if winner_flag:
            break
    if winner_flag:
        winner_details = [marker_to_be_search]
    else:
        winner_details = [winner_flag]
    return winner_details
        
        


# In[ ]:


main_func()

