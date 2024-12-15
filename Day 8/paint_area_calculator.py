import math

def paint_area(height, width, coverage):
    num_of_cans= math.ceil((height*width)/coverage)
    print(f"You will need {num_of_cans}")

wall_height= int(input("Enter the height of your wall"))
wall_width= int(input("Enter the width of your wall"))
coverage_per_can= int(input("Enter the coverage per can"))
paint_area(height=wall_height, width=wall_width, coverage=coverage_per_can)