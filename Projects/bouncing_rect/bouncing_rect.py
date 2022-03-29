"""
File: bouncing_rect.py
Name: 
------------------------
This file shows how to make a simple 
animation by campy library
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause

# This controls the width and height of the rect
SIZE = 30

# This controls the pause time (in millisecond) for the animation
DELAY = 10

from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gwindow import GWindow

def main():
	window = GWindow()
	rect = set_up_rect()
	window.add(rect, x=(window.width - SIZE)/3, y=(window.height - SIZE)/2)

	# rect_2 = set_up_rect()
	# window.add(rect_2, x=(window.width - SIZE)*2 / 3, y=(window.height - SIZE) / 2)

	vx = 5
	vx2 = 5
	while True:
		rect.move(vx, 0)
		# rect_2.move(-vx2, 0)
		if rect.x <= 0 or rect.x + SIZE >= window.width:
			vx = -vx
		# if rect_2.x <= 0 or rect_2.x + SIZE >= window.width:
		# 	vx2 = -vx2
		pause(DELAY)


def set_up_rect():
	rect = GRect(SIZE, SIZE)
	rect.filled = True
	rect.color = 'magenta'
	rect.fill_color = 'magenta'
	return rect


if __name__ == '__main__':
	main()
