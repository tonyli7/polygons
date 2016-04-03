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

edges=new_matrix(4,0)
add_box(edges,0,0,0,200,100,400)
#print_matrix(edges)
#print edges

matrix_mult(make_rotX(20),edges)
matrix_mult(make_rotY(20),edges)
matrix_mult(make_translate(100,100,0),edges)


draw_polygons(edges, screen, color)
display(screen)
#f.close()
