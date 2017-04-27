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


class Button:
    @staticmethod
    def no_action():
        return {0: False,
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

    @staticmethod
    def cross():
        return {0: True,
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

    @staticmethod
    def circle():
        return {0: False,
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

    @staticmethod
    def triangle():
        return {0: False,
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

    @staticmethod
    def square():
        return {0: False,
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

    @staticmethod
    def l1():
        return {0: False,
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

    @staticmethod
    def r1():
        return {0: False,
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

    @staticmethod
    def l2():
        return {0: False,
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

    @staticmethod
    def r2():
        return {0: False,
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

    @staticmethod
    def unknown_command_1():
        return {0: False,
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

    @staticmethod
    def unknown_command_2():
        return {0: False,
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

    @staticmethod
    def ps_and_touch_button():
        return {0: False,
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

    @staticmethod
    def l3():
        return {0: False,
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

    @staticmethod
    def r3():
        return {0: False,
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
