print("Welcome to a paint can calculator: ")
wall_height=int(input("Height of wall ?"))
wall_width=int(input("weight of wall ? "))
coverage= 5 
num_of_cans= (wall_height*wall_width) /coverage
#import math
#def paint_calc(height,weight,cover):
 #area=height*weight 
# num_of_cans = math.ceil(area/cover)
print(f"You will need {num_of_cans} cans of paint.")