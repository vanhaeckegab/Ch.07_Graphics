'''
FLAG PROJECT
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red:#BF0A30 and blue:#002868
Title the window, "The Stars and Stripes"
I used a draw_text command and used 20 pt. asterisks for the stars.
We will have a competition to see who can make this flag in the least lines of code.
The record is 16! You will have to use some loops to achieve this.
'''
import arcade
import math

SH = 390
SW = SH * 1.9
arcade.open_window(int(SW), SH, "Flag")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

# Red lines
for y in range(int(SH/26), SH+1, int(SH / 13 * 2)):
    arcade.draw_rectangle_filled(SW/2, y, SW+1, SH/13, (191, 10, 48))

# Blue Square
arcade.draw_lrtb_rectangle_filled(0, SH * .76, SH, SH - .5385 * SH, (0, 40, 104))

# Star code
for i in range(50):
    if i <= 5:
        SY = SH - SH * .054
        SX = SH * .063 + i * (2 * SH * .063)
    elif i > 5 and i <= 10:
        SY = SH - 2 * SH * .054
        SX = 2 * SH * .063 + (i - 6) * (2 * SH * .063)
    elif i > 10 and i <= 16:
        SY = SH - 3 * SH * .054
        SX = SH * .063 + (i - 11) * (2 * SH * .063)
    elif i > 16 and i <= 21:
        SY = SH - 4 * SH * .054
        SX = 2 * SH * .063 + (i - 17) * (2 * SH * .063)
    elif i > 21 and i <= 27:
        SY = SH - 5 * SH * .054
        SX = SH * .063 + (i - 22) * (2 * SH * .063)
    elif i > 27 and i <= 32:
        SY = SH - 6 * SH * .054
        SX = 2 * SH * .063 + (i - 28) * (2 * SH * .063)
    elif i > 32 and i <= 38:
        SY = SH - 7 * SH * .054
        SX = SH * .063 + (i - 33) * (2 * SH * .063)
    elif i > 38 and i <= 43:
        SY = SH - 8 * SH * .054
        SX = 2 * SH * .063 + (i - 39) * (2 * SH * .063)
    else:
        SY = SH - 9 * SH * .054
        SX = SH * .063 + (i - 44) * (2 * SH * .063)
    arcade.draw_polygon_filled([
                [(SH*.0616)/6 * math.cos(math.radians(54)) + SX, (SH*.0616)/6 * math.sin(math.radians(54))+SY],
                [SH*.0616/2 * math.cos(math.radians(90)) + SX, SH*.0616/2 * math.sin(math.radians(90)) + SY],
                [(SH*.0616)/6 * math.cos(math.radians(126)) + SX, (SH*.0616)/6 * math.sin(math.radians(126))+SY],
                [SH*.0616/2 * math.cos(math.radians(162)) + SX, SH*.0616/2 * math.sin(math.radians(162)) + SY],
                [(SH*.0616)/6 * math.cos(math.radians(198)) + SX, (SH*.0616)/6 * math.sin(math.radians(198))+SY],
                [SH*.0616/2 * math.cos(math.radians(234)) + SX, SH*.0616/2 * math.sin(math.radians(234)) + SY],
                [(SH*.0616)/6 * math.cos(math.radians(270)) + SX, (SH*.0616)/6 * math.sin(math.radians(270)) + SY],
                [SH*.0616/2 * math.cos(math.radians(306)) + SX, SH*.0616/2 * math.sin(math.radians(306)) + SY],
                [(SH*.0616)/6 * math.cos(math.radians(342)) + SX, (SH*.0616)/6 * math.sin(math.radians(342))+SY],
                [SH*.0616/2 * math.cos(math.radians(18)) + SX, SH*.0616/2 * math.sin(math.radians(18)) + SY]
                ], arcade.color.WHITE)

arcade.finish_render()
arcade.run()







