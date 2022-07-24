from curses import wrapper
import curses
import datetime
import canvas
import traceback
import random
import time

_canvas = canvas.Canvas()

# square
lines = [     # x1    y1   x2    y2        color
    canvas.Line(10,   10,   50,  10,       255),
    canvas.Line(50,   10,   50,  50,       135),
    canvas.Line(50,   50,   10,  50,        55),
    canvas.Line(10,   50,   10,  10,        95),
]

def randomise(scr):
    quad_verts = [
        random.randint(0, scr.getmaxyx()[1]-1),
        random.randint(0, scr.getmaxyx()[0]-1),
        random.randint(0, scr.getmaxyx()[1]-1),
        random.randint(0, scr.getmaxyx()[0]-1),

        random.randint(0, scr.getmaxyx()[1]-1),
        random.randint(0, scr.getmaxyx()[0]-1),
        random.randint(0, scr.getmaxyx()[1]-1),
        random.randint(0, scr.getmaxyx()[0]-1),
    ]

    lines[0].x1 = quad_verts[0]
    lines[0].y1 = quad_verts[1]
    lines[0].x2 = quad_verts[2]
    lines[0].y2 = quad_verts[3]

    lines[1].x1 = quad_verts[2]
    lines[1].y1 = quad_verts[3]
    lines[1].x2 = quad_verts[4]
    lines[1].y2 = quad_verts[5]

    lines[2].x1 = quad_verts[4]
    lines[2].y1 = quad_verts[5]
    lines[2].x2 = quad_verts[6]
    lines[2].y2 = quad_verts[7]

    lines[3].x1 = quad_verts[6]
    lines[3].y1 = quad_verts[7]
    lines[3].x2 = quad_verts[0]
    lines[3].y2 = quad_verts[1]

    for line in lines:
        line.color = random.randint(0, 255)

for i in lines:
    _canvas.add_line(i)

def schermo(scr, *args):
    try:
        ch = ''
        stdscr = curses.initscr()
        curses.cbreak()
        stdscr.timeout(100)
        while ch != ord('q'):
            randomise(stdscr)
            stdscr.addstr(0, 0, f"{datetime.datetime.now()}")
            stdscr.addstr(0, 0, _canvas.ret(scr.getmaxyx()[1]-1, scr.getmaxyx()[0]-1))
            stdscr.clrtobot()
            ch = stdscr.getch()
            time.sleep(1)

    except:
        traceback.print_exc()
    finally:
        curses.endwin()


curses.wrapper(schermo)
