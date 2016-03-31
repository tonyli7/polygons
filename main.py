from display import *
from draw import *
from parser import *
from matrix import *
import sys

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

"""
if len(sys.argv) == 2:
    f = open(sys.argv[1])

parse_file( f, edges, transform, screen, color )
"""

edges=new_matrix()
add_box(edges,200,200,0,50,50,50)
draw_polygons(edges, screen, color)
display(screen)
#f.close()
