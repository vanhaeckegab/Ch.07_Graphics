'''
PYCASSO PROJECT
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''

import arcade
import math

SH = 500
SW = 500
arcade.open_window(int(SW), SH, "Gabe Van Haecke")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

arcade.draw_circle_filled(250, 250, 150, arcade.color.BLACK)
arcade.draw_lrtb_rectangle_filled(0, SW, 162.5, 0, arcade.color.WHITE)


def drawstar(sx, sy, r):
    arcade.draw_polygon_filled([[4 * math.cos(math.radians(54+r)) + sx, 4 * math.sin(math.radians(54+r)) + sy],
                            [12 * math.cos(math.radians(90+r)) + sx, 12 * math.sin(math.radians(90+r)) + sy],
                            [4 * math.cos(math.radians(126+r)) + sx, 4 * math.sin(math.radians(126+r)) + sy],
                            [12 * math.cos(math.radians(162+r)) + sx, 12 * math.sin(math.radians(162+r)) + sy],
                            [4 * math.cos(math.radians(198+r)) + sx, 4 * math.sin(math.radians(198+r)) + sy],
                            [12 * math.cos(math.radians(234+r)) + sx, 12 * math.sin(math.radians(234+r)) + sy],
                            [4 * math.cos(math.radians(270+r)) + sx, 4 * math.sin(math.radians(270+r)) + sy],
                            [12 * math.cos(math.radians(306+r)) + sx, 12 * math.sin(math.radians(306+r)) + sy],
                            [4 * math.cos(math.radians(342+r)) + sx, 4 * math.sin(math.radians(342+r)) + sy],
                            [12 * math.cos(math.radians(18+r)) + sx, 12 * math.sin(math.radians(18+r)) + sy]
                            ], arcade.color.BLACK)


for i in range(22):
    drawstar(250 + 175 * math.cos(math.radians(-28.125 + 11.25 * i)),
             250 + 175 * math.sin(math.radians(-28.125 + 11.25 * i)), 28.125 + 11.25 * i)

arcade.draw_text("AMOGUS", 250, 280, arcade.color.WHITE_SMOKE, 50, 0, "center", "Impact", False, False, "center",)

arcade.draw_circle_filled(170, 200, 25, arcade.color.ORANGE_RED)
arcade.draw_circle_filled(170, 160, 25, arcade.color.ORANGE_RED)
arcade.draw_lrtb_rectangle_filled(145, 180, 200, 160, arcade.color.ORANGE_RED)
arcade.draw_circle_filled(225, 225, 60, arcade.color.RED)
arcade.draw_circle_filled(225, 160, 60, arcade.color.RED)
arcade.draw_lrtb_rectangle_filled(165, 285, 225, 160, arcade.color.RED)
arcade.draw_circle_filled(250, 225, 35, arcade.color.COOL_GREY)
arcade.draw_circle_filled(275, 225, 35, arcade.color.COOL_GREY)
arcade.draw_lrtb_rectangle_filled(250, 275, 260, 190, arcade.color.COOL_GREY)
arcade.draw_circle_filled(270, 230, 10, arcade.color.ASH_GREY)
arcade.draw_circle_filled(280, 230, 10, arcade.color.ASH_GREY)
arcade.draw_lrtb_rectangle_filled(270, 280, 240, 220, arcade.color.ASH_GREY)
arcade.draw_circle_filled(190, 85, 25, arcade.color.RED)
arcade.draw_lrtb_rectangle_filled(165, 215, 220, 85, arcade.color.RED)
arcade.draw_circle_filled(260, 85, 25, arcade.color.RED)
arcade.draw_lrtb_rectangle_filled(235, 285, 160, 85, arcade.color.RED)

arcade.draw_text("It's a problem", 250, 0,
                 arcade.color.BLACK, 85, 0, "center", "Brush Script", False, True, "center")


arcade.finish_render()
arcade.run()
