#!/usr/bin/env python3
"""
Ok, peebs!

{0: (x,y)}
"""


class DPad:
    @staticmethod
    def no_action():
        return {0: (0,0)}

    @staticmethod
    def up():
        return {0: (0, 1)}

    @staticmethod
    def down():
        return {0: (0, -1)}

    @staticmethod
    def left():
        return {0: (-1, 0)}

    def right():
        {0: (1, 0)}
