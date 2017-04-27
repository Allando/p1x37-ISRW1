#!/usr/bin/env python3
"""
Well, lads, this is a big one!
0: Left Stick  :: -1 = Left | +1 = Right 
1: Left Stick  :: -1 = Up   | +1 = Down
2: UNKNOWN COMMAND
3: Right Stick :: -1 = Left | +1 = Right 
4: Right Stick :: -1 = Up   | +1 = Down
"""


class Analog:
    @staticmethod
    def no_action():
        return {
            0: (0.0),
            1: (0.0),
            2: (0.0),
            3: (0.0),
            4: (0.0)
        }

    @staticmethod
    def left_stick_up():
        return {
            0: (0.0),
            1: (-1.0),
            2: (0.0),
            3: (0.0),
            4: (0.0)
        }

    @staticmethod
    def left_stick_down():
        return {
            0: (0.0),
            1: (1.0),
            2: (0.0),
            3: (0.0),
            4: (0.0)
        }

    @staticmethod
    def left_stick_left():
        return {
            0: (-1.0),
            1: (0.0),
            2: (0.0),
            3: (0.0),
            4: (0.0)
        }

    @staticmethod
    def left_stick_right():
        return {
            0: (1.0),
            1: (0.0),
            2: (0.0),
            3: (0.0),
            4: (0.0)
        }

    @staticmethod
    def unknown_action_1():
        return {
            0: (0.0),
            1: (0.0),
            2: (-1.0),
            3: (0.0),
            4: (0.0)
        }

    @staticmethod
    def unknown_action_2():
        return {
            0: (0.0),
            1: (0.0),
            2: (1.0),
            3: (0.0),
            4: (0.0)
        }

    @staticmethod
    def right_stick_up():
        return {
            0: (0.0),
            1: (0.0),
            2: (0.0),
            3: (0.0),
            4: (-1.0)
        }

    @staticmethod
    def right_stick_down():
        return {
            0: (0.0),
            1: (1.0),
            2: (0.0),
            3: (0.0),
            4: (1.0)
        }

    @staticmethod
    def right_stick_left():
        return {
            0: (0.0),
            1: (0.0),
            2: (0.0),
            3: (-1.0),
            4: (0.0)
        }

    @staticmethod
    def right_stick_right():
        return {
            0: (1.0),
            1: (0.0),
            2: (0.0),
            3: (1.0),
            4: (0.0)
        }


