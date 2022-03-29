"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 12        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
score = 0



class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height, x=(self.window_width-paddle_width)/2,
                            y=self.window_height-paddle_offset-paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.paddle.color = 'black'
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.ball.color = 'black'
        self.window.add(self.ball, x=self.window_width/2-ball_radius, y=self.window_height/2-ball_radius)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # life
        self.initial_life = 0

        # heart

        # self.heart = GPolygon()
        # self.heart.add_vertex((0, 10))
        # self.heart.add_vertex((10, 0))
        # self.heart.add_vertex((20, 10))
        # self.heart.add_vertex((30, 0))
        # self.heart.add_vertex((40, 10))
        # self.heart.add_vertex((20, 30))


        # Initialize our mouse listeners
        onmouseclicked(self.ball_speed)
        onmousemoved(self.paddle_move)

        # Draw bricks
        for i in range(BRICK_COLS):
            for j in range(BRICK_ROWS):
                brick = GRect(width=brick_width, height=brick_height)
                brick.filled = True
                brick.color = 'black'
                if j <= 1:
                    brick.fill_color = 'red'
                elif j <= 3:
                    brick.fill_color = 'orange'
                elif j <= 5:
                    brick.fill_color = 'yellow'
                elif j <= 7:
                    brick.fill_color = 'green'
                elif j <= 9:
                    brick.fill_color = 'blue'
                else:
                    brick.fill_color = 'purple'
                self.window.add(brick, x=i*(brick_width + brick_spacing), y=j*(brick_height + brick_spacing))

        # score label
        global score
        self.score_label = GLabel('Score : ' + str(score))
        self.score_label.font = '-20'
        self.window.add(self.score_label, x=0, y=self.window_height - self.score_label.height/2)

    def paddle_move(self, mouse):
        if (mouse.x >= PADDLE_WIDTH/2) and (mouse.x <= self.window_width - PADDLE_WIDTH/2):
            self.paddle.x = mouse.x - PADDLE_WIDTH/2
        elif mouse.x < PADDLE_WIDTH/2:
            # while self.paddle.x > 0:
            #     self.paddle.x -= 1
            #     pause(5)
            self.paddle.x = 0
        elif mouse.x > self.window_width - PADDLE_WIDTH/2:
            # while self.paddle.x < self.window_width - PADDLE_WIDTH:
            #     self.paddle.x += 1
            #     pause(5)
            self.paddle.x = self.window_width - PADDLE_WIDTH

    def ball_speed(self, mouse):
        if self.__dx == 0 and self.__dy == 0:
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
        if self.ball.y >= self.window_height and self.initial_life > 1:
            self.ball.x = self.window_width / 2 - BALL_RADIUS
            self.ball.y = self.window_height/2 - BALL_RADIUS
            self.__dx = 0
            self.__dy = 0
            self.initial_life -= 1
            self.life_remain(self.initial_life)
        elif self.ball.y >= self.window_height and self.initial_life <= 1:
            self.over_label = GLabel('Game over')
            self.over_label.font = '-60'
            self.window.add(self.over_label, x=(self.window_width-self.over_label.width)/2,
                            y=(self.window_height - self.over_label.height) / 2)

    def life_remain(self, life):
        for i in range(life):
            re_round = self.window.get_object_at(
                (self.window_width - (i + 1) * self.round.width * 1.2 + self.round.width / 2),
                (self.window_height - self.round.height / 2 - 5))
            self.window.remove(re_round)
        for i in range(life):
            self.round = GOval(20, 20)
            self.round.filled = True
            self.round.fill_color = 'red'
            self.window.add(self.round, x=(self.window_width-(i+1)*self.round.width*1.2),
                            y=(self.window_height-self.round.height-5))


    def set_life(self, life_1):
        self.initial_life = life_1

    def set_dx(self, vx):
        self.__dx *= vx

    def set_dy(self, vy):
        self.__dy *= vy

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def bounce_x(self):
        maybe_obj = None
        global score
        if self.window.get_object_at(self.ball.x - 1, self.ball.y + BALL_RADIUS) is not None and \
                self.window.get_object_at(self.ball.x - 1, self.ball.y + BALL_RADIUS) is not self.score_label:
            maybe_obj = self.window.get_object_at(self.ball.x, self.ball.y + BALL_RADIUS)

        elif self.window.get_object_at(self.ball.x + 2*BALL_RADIUS + 1, self.ball.y + BALL_RADIUS) is not None and \
                self.window.get_object_at(self.ball.x + 2*BALL_RADIUS + 1, self.ball.y + BALL_RADIUS) \
                is not self.score_label:
            maybe_obj = self.window.get_object_at(self.ball.x + 2*BALL_RADIUS, self.ball.y + BALL_RADIUS)

        if maybe_obj is not self.paddle and maybe_obj is not None and maybe_obj is not self.score_label:
            self.window.remove(maybe_obj)
            score += 1
            self.score_label.text = 'Score : ' + str(score)
        return maybe_obj

    def bounce_y(self):
        maybe_obj = None
        global score
        if self.window.get_object_at(self.ball.x + 2*BALL_RADIUS/3, self.ball.y) is not None and \
                self.window.get_object_at(self.ball.x + 2*BALL_RADIUS/3, self.ball.y) is not self.score_label:
            maybe_obj = self.window.get_object_at(self.ball.x + 2*BALL_RADIUS/3, self.ball.y)

        elif self.window.get_object_at(self.ball.x + 4*BALL_RADIUS/3, self.ball.y) is not None and \
                self.window.get_object_at(self.ball.x + 4*BALL_RADIUS/3, self.ball.y) is not self.score_label:
            maybe_obj = self.window.get_object_at(self.ball.x + 4*BALL_RADIUS/3, self.ball.y)

        elif self.window.get_object_at(self.ball.x + 2*BALL_RADIUS/3, self.ball.y + 2*BALL_RADIUS) is not None and \
                self.window.get_object_at(self.ball.x + 2*BALL_RADIUS/3, self.ball.y + 2*BALL_RADIUS) \
                is not self.score_label:
            maybe_obj = self.window.get_object_at(self.ball.x + 2*BALL_RADIUS/3, self.ball.y + 2*BALL_RADIUS)

        elif self.window.get_object_at(self.ball.x + 4*BALL_RADIUS/3, self.ball.y + 2*BALL_RADIUS) is not None and \
                self.window.get_object_at(self.ball.x + 4*BALL_RADIUS/3, self.ball.y + 2*BALL_RADIUS) \
                is not self.score_label:
            maybe_obj = self.window.get_object_at(self.ball.x + 4*BALL_RADIUS/3, self.ball.y + 2*BALL_RADIUS)

        if maybe_obj is not self.paddle and maybe_obj is not None and maybe_obj is not self.score_label:
            self.window.remove(maybe_obj)
            score += 1
            self.score_label.text = 'Score : ' + str(score)
        return maybe_obj

