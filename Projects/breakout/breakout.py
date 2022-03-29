"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    graphics = BreakoutGraphics()
    graphics.set_life(NUM_LIVES)
    while True:
        graphics.ball.move(graphics.get_dx(), graphics.get_dy())
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.set_dx(-1)
        if graphics.ball.y <= 0:
            graphics.set_dy(-1)
        if graphics.bounce_x() is not None:
            graphics.set_dx(-1)
        elif graphics.bounce_y() is not None:
            graphics.set_dy(-1)
        if graphics.ball.y >= graphics.window_height and graphics.initial_life <= 1:
            graphics.ball_speed(1)


        pause(FRAME_RATE)
    # Add the animation loop here!



if __name__ == '__main__':
    main()
