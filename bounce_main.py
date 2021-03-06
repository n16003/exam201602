from tkinter import *
import random
import time

#色とサイズ
WIDTH = 500
HEIGHT= 600
COLOR  = ('red', 'blue', 'green', 'yellow')
BLOCK_W = 8
BLOCK_H = 5
U_BLOCK_W = 4

#衝突判定
def point_collision(a , b):
    cx = ( b[2] - b[0]) / 2
    cy = ( b[3] - b[1]) /2
    r = cx
    #left-top
    dx = cx - a[0]
    dy = cy - a[1]
    p1 = dx**2 + dy**2 < r**2
    #right-top
    dx = cx - a[2]
    dy = cy - a[1]
    p2 = dx**2 + dy**2 < r**2
    #right-bottom
    dx = cx - a[2]
    dy = cy - a[3]
    p3 = dx**2 + dy**2 < r**2
    #left-bottom
    dx = cx - a[0]
    dy = cy - a[3]
    p4 = dx**2 + dy**2 < r**2

    return p1 or p2 or p3 or p4


class Ball:
    def __init__(self, canvas, paddle, blocks,u_blocks, color):
        self.canvas = canvas
        self.paddle = paddle
        self.blocks  = blocks
        self.u_blocks = u_blocks
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 200)
        self.x =  0
        self.y =  0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        self.canvas.bind_all('<KeyPress-Return>',self.start)
#キースタート（ENTERを押すと初期位置に戻るチート機能付き）
    def start(self,event):
        self.x = random.choice((-3,-2,-1,1,2,3))
        self.y = -3
        c.itemconfig(game_start_text, state = 'hidden')
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True

        return False

#paddleの下に当たっても跳ね返るように
    def hit_paddle2(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[1] <= paddle_pos[3] and pos[3] >= paddle_pos[3]:
                return True

#ブロックの当たり判定
    def hit_block(self, pos):
        target_block = 0
        collision_type = 0
        for block in self.blocks:
            block_pos = self.canvas.coords(block.id)

            # circle_collision check
            if point_collision(block_pos, pos):
                collision_type |= 3

            # top check
            if pos[2] >= block_pos[0] and pos[0] <= block_pos[2] \
                and pos[3] >= block_pos[1] and pos[3] < block_pos[3]:

                collision_type |= 1

            # bottom check
            if pos[2] >= block_pos[0] and pos[0] <= block_pos[2] \
                and pos[1] > block_pos[1] and pos[1] <= block_pos[3]:

                collision_type |= 1

            # left check
            if pos[3] >= block_pos[1] and pos[1] <= block_pos[3] \
                and pos[2] >= block_pos[0] and pos[2] < block_pos[2]:

                collision_type |= 2

            # right check
            if pos[3] >= block_pos[1] and pos[1] <= block_pos[3] \
                  and pos[0] > block_pos[0] and pos[0] <= block_pos[2]:

                collision_type |= 2

            if collision_type != 0:
                return(block, collision_type)

        return (None, 0)

    def hit_u_block(self, pos):
        target_block = 0
        collision_type = 0
        for block in self.u_blocks:
            block_pos = self.canvas.coords(block.id)

            # circle_collision check
            if point_collision(block_pos, pos):
                collision_type |= 3

            # top check
            if pos[2] >= block_pos[0] and pos[0] <= block_pos[2] \
                    and pos[3] >= block_pos[1] and pos[3] < block_pos[3]:

                collision_type |= 1

            # bottom check
            if pos[2] >= block_pos[0] and pos[0] <= block_pos[2] \
                    and pos[1] > block_pos[1] and pos[1] <= block_pos[3]:

                collision_type |= 1

            # left check
            if pos[3] >= block_pos[1] and pos[1] <= block_pos[3] \
                    and pos[2] >= block_pos[0] and pos[2] < block_pos[2]:

                collision_type |= 2

            # right check
            if pos[3] >= block_pos[1] and pos[1] <= block_pos[3] \
                    and pos[0] > block_pos[0] and pos[0] <= block_pos[2]:

                collision_type |= 2

            if collision_type != 0:
                return (block, collision_type)

        return (None, 0)

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = abs(self.y)

        if pos[3] >= self.canvas_height:
            # self.y = abs(self.y) * -1
            self.hit_bottom = True

        if pos[0] <= 0:
            self.x = abs(self.x)

        if pos[2] >= self.canvas_width:
            self.x = abs(self.x) * -1

        if self.hit_paddle(pos):
            self.y = abs(self.x) * -1

        if self.hit_paddle2(pos):
            self.y = abs(self.x)

        (target, collision_type) = self.hit_block(pos)
        if target != None:
            target.delete()
            del self.blocks[self.blocks.index(target)]

            if (collision_type & 1) != 0:
                self.y *= -1

        (target, collision_type) = self.hit_u_block(pos)
        if target != None:
            target.delete()
            del self.u_blocks[self.u_blocks.index(target)]

            if (collision_type & 1) != 0:
                self.y *= -1


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 220, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, event):
        self.x = -2

    def turn_right(self, event):
        self.x = 2

class Block:
    def __init__(self, canvas, x, y, color):
        self.canvas = canvas
        self.pos_x = x
        self.pos_y = y
        self.id = canvas.create_rectangle(0, 0, 50, 20, fill = color)
        self.canvas.move(self.id,self.pos_x * 50 + 60, self.pos_y * 20 + 25)

    def delete(self):
        self.canvas.delete(self.id)

class Under_Block:
    def __init__(self, canvas, x, y, color):
        self.canvas = canvas
        self.pos_x = x
        self.pos_y = y
        self.id = canvas.create_rectangle(0, 0, 50, 20, fill=color)
        self.canvas.move(self.id, self.pos_x * 50 + 150, self.pos_y * 20 + 450)

    def delete(self):
        self.canvas.delete(self.id)


tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
c = Canvas(tk,width = WIDTH,height = HEIGHT, bd=0, highlightthickness=0)
c.pack()
tk.update()

image1 = PhotoImage(file = 'new_hikakin.gif')

hoge = c.create_image(0, 0, image = image1)
c.move(hoge, 170, 200)

#ブロック生成
blocks=[]
for y in range(BLOCK_H):
    for x in range(BLOCK_W):
        blocks.append(Block(c, x, y, random.choice(COLOR)))

u_blocks = []
for y in range(BLOCK_H):
    for x in range(U_BLOCK_W):
        u_blocks.append(Under_Block(c, x, y, random.choice(COLOR)))

p = Paddle(c, 'green')
ball = Ball(c, p, blocks, u_blocks, 'black')

game_over_text = c.create_text(250,200,  text ='GAME OVER', state = 'hidden',font =('Courier', 40))
game_start_text = c.create_text(250, 200, text ='Please push enter', state = 'hidden', font =('Courier', 20))
c.itemconfig(game_start_text, state='normal')


def update():
    if not ball.hit_bottom:
        ball.draw()
        p.draw()

    if ball.hit_bottom == True:
        time.sleep(1)
        c.itemconfig(game_start_text, state = 'hidden')
        c.itemconfig(game_over_text, state = 'normal')




    tk.update_idletasks()
    tk.update()
    tk.after(10, update)


tk.after(10, update)
tk.mainloop()
