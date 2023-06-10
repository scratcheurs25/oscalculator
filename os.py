import kandinsky
import ion
from math import *
from kandinsky import *
from ion import *

mousex = 50
mousey = 50
mouses = 2
windows_cont = True
draw_init = 0
draw_initt = False
gamel = False
typee = "base"
pro = False

def draw_app(idenk,x,y):
    global gamel
    global pro
    w = 50
    h = 50
    kandinsky.fill_rect(x,y,w,h,(0,255,0))
    kandinsky.draw_string(idenk,x,y+h)
    if x < mousex - 5 + 15 and mousex - 5 < x + w and y < mousey - 5 + 15 and mousey - 5 < y + h:
        if idenk == "game" and ion.keydown(KEY_EXE):
            gamel = True
        if idenk == "pro" and ion.keydown(KEY_EXE):
            pro = True 

def draw_backgond():
    global draw_initt
    global draw_init
    global gamel
    global typee
    global pro
    kandinsky.fill_rect(0,0,320,222,(255,255,255))
    if not draw_initt:
        kandinsky.draw_string("welcome to works os",0,0)
    if draw_init > 0:
        kandinsky.draw_string("init",0,0)
        draw_init -= 1
        draw_initt = True
    if draw_init == 0 and draw_initt:
        if typee == "base":
            draw_app("game",0,0)
        else:
            draw_app("pro",0,0)
    if gamel:
        draw_window("game",50,50,200,100,"exegame")
    if pro:
        draw_window("you programe",50,50,200,100,"progame")




def draw_button(text,x,y,w,h,idenk):
    global windows_cont
    global draw_init
    global gamel
    global pro
    kandinsky.fill_rect(x,y,w,h,(255,255,255))
    kandinsky.draw_string(text,x,y)
    if x < mousex - 5 + 15 and mousex - 5 < x + w and y < mousey - 5 + 15 and mousey - 5 < y + h and ion.keydown(KEY_EXE):
        if idenk == "setup":
            draw_init = 50
            windows_cont = False
        if idenk == "gamequit":
            gamel = False
            pro = False

def draw_window(titel,x,y,w,h,idenk):
    kandinsky.fill_rect(x,y,w,h,(44,48,52))
    kandinsky.draw_string(titel,x,y)
    if idenk == "start":
        draw_button("setup",x + 80,y + 50,50,10,"setup")
    if idenk != "start":
        draw_button("x",x + w - 10,y,10,10,"gamequit")
    if idenk == "exegame":
        draw_button("cliks",x + 80,y + 50,50,10,"null")
    if idenk == "progame":
        pass
def draw_mouse():
    kandinsky.fill_rect(mousex + 5,mousey +5,5,5,(0,0,0))
    kandinsky.fill_rect(mousex - 5,mousey,10,5,(0,0,0))
    kandinsky.fill_rect(mousex - 5,mousey - 5,10,5,(0,0,0))

def mouse_move():
    global mousex
    global mousey
    global mouses
    if ion.keydown(KEY_RIGHT):
        mousex += mouses
    if ion.keydown(KEY_LEFT):
        mousex -= mouses
    if ion.keydown(KEY_UP):
        mousey -= mouses
    if ion.keydown(KEY_DOWN):
        mousey += mouses
def run(os):
    global typee
    while True:
        if os == "":
            typee = "base"
            draw_backgond()
            if windows_cont:
                draw_window("os",50,50,200,100,"start")
            draw_mouse()
            mouse_move()
        elif os == "pro":
            typee = "pro"
            draw_backgond()
            if windows_cont:
                draw_window("os",50,50,200,100,"start")
            draw_mouse()
            mouse_move()

