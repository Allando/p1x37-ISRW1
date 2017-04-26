#! /usr/bin/env python3
"""
Okay, here is the deal!!
    {0: False,    CROSS
     1: False,    CIRCLE
     2: False,    TRIANGLE
     3: False,    SQUARE
     4: False,    L1
     5: False,    R1
     6: False,    L2
     7: False,    R2
     8: False,    UNKNOWN COMMAND
     9: False,    UNKNOWN COMMAND
     10: False,   PS Button / Touch Pad button
     11: False,   L3
     12: False}   R3
"""


class button:
    def no_action(self):
        {0: False,
         1: False,
         2: False,
         3: False,
         4: False,
         5: False,
         6: False,
         7: False,
         8: False,
         9: False,
         10: False,
         11: False,
         12: False}

    def cross(self):
        {0: True,
         1: False,
         2: False,
         3: False,
         4: False,
         5: False,
         6: False,
         7: False,
         8: False,
         9: False,
         10: False,
         11: False,
         12: False}

    def circle(self):
        {0: False,
         1: True,
         2: False,
         3: False,
         4: False,
         5: False,
         6: False,
         7: False,
         8: False,
         9: False,
         10: False,
         11: False,
         12: False}

    def triangle(self):
        {0: False,
         1: False,
         2: True,
         3: False,
         4: False,
         5: False,
         6: False,
         7: False,
         8: False,
         9: False,
         10: False,
         11: False,
         12: False}

    def square(self):
        {0: False,
         1: False,
         2: False,
         3: True,
         4: False,
         5: False,
         6: False,
         7: False,
         8: False,
         9: False,
         10: False,
         11: False,
         12: False}

    def l1(self):
        {0: False,
         1: False,
         2: False,
         3: False,
         4: True,
         5: False,
         6: False,
         7: False,
         8: False,
         9: False,
         10: False,
         11: False,
         12: False}

    def r1(self):
        {0: False,
         1: False,
         2: False,
         3: False,
         4: False,
         5: True,
         6: False,
         7: False,
         8: False,
         9: False,
         10: False,
         11: False,
         12: False}

    def l2(self):
        {0: False,
         1: False,
         2: False,
         3: False,
         4: False,
         5: False,
         6: True,
         7: False,
         8: False,
         9: False,
         10: False,
         11: False,
         12: False}

    def r2(self):
        {0: False,
         1: False,
         2: False,
         3: False,
         4: False,
         5: False,
         6: False,
         7: True,
         8: False,
         9: False,
         10: False,
         11: False,
         12: False}

    def unknown_command_1(self):
        {0: False,
         1: False,
         2: False,
         3: False,
         4: False,
         5: False,
         6: False,
         7: False,
         8: True,
         9: False,
         10: False,
         11: False,
         12: False}

    def unknown_command_2(self):
        {0: False,
         1: False,
         2: False,
         3: False,
         4: False,
         5: False,
         6: False,
         7: False,
         8: False,
         9: True,
         10: False,
         11: False,
         12: False}

    def ps_and_touch_button(self):
        {0: False,
         1: False,
         2: False,
         3: False,
         4: False,
         5: False,
         6: False,
         7: False,
         8: False,
         9: False,
         10: True,
         11: False,
         12: False}

    def l3(self):
        {0: False,
         1: False,
         2: False,
         3: False,
         4: False,
         5: False,
         6: False,
         7: False,
         8: False,
         9: False,
         10: False,
         11: True,
         12: False}

    def r3(self):
        {0: False,
         1: False,
         2: False,
         3: False,
         4: False,
         5: False,
         6: False,
         7: False,
         8: False,
         9: False,
         10: False,
         11: False,
         12: True}
