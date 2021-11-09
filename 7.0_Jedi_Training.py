# Sign your name: Gabe Van Haecke

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''

import arcade
SW = 500
SH = 400
arcade.open_window(SW, SH, "Ch.7 Jedi Training")
arcade.set_background_color(arcade.color.ALMOND)

arcade.start_render()
for x in range(0, SW + 1, 20):
    arcade.draw_rectangle_filled(x, SH/2, 2, SH+1, arcade.color.BLACK)
for y in range(0, SH + 1, 20):
    arcade.draw_rectangle_filled(SW/2, y, SW+1, 2, arcade.color.BLACK)
arcade.draw_lrtb_rectangle_filled(20, 80, 380, 360, arcade.color.PHLOX)
arcade.draw_line(80, 20, 120, 60, arcade.color.BLUE)
arcade.draw_rectangle_filled(200, 260, 20, 40, arcade.color.BLUSH, 45)
arcade.draw_circle_filled(250, 200, 40, arcade.color.WISTERIA)
arcade.draw_ellipse_filled(100, 100, 120, 40, arcade.color.AMBER)
arcade.draw_text("I love you. I know.", 20, 155, arcade.color.BRICK_RED, 20)
arcade.draw_arc_filled(400, 320, 120, 120, arcade.color.YELLOW, 30, 330)
arcade.draw_point(460, 10, arcade.color.RED, 5)
arcade.finish_render()
arcade.run()
