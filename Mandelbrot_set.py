# This program plots a Mandelbrot set with N iterations

# struttura del programma:
# 1 selezionare un punto nel piano complesso
# 2 girare l'itarazione sul quel punto
# 3 linea di controllo se z>2
# 4 metterlo in diversi insiemi a seconda della linea di controllo
# 5 fare un plot

# 1

import numpy as np

x_min = -2
x_max = 2
y_min = -2
y_max = 2

points=100
delta_x=(x_max-x_min)/points
delta_y=(y_max-y_min)/points

x = np.arange(x_min, x_max, de)

print re
