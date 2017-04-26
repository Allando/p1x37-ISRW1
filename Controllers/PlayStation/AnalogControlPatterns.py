#!/usr/bin/env python3
"""
Well, lads, this is a big one!
0: Left Stick  :: -1 = Left | +1 = Right 
1: Left Stick  :: -1 = Up   | +1 = Down
2: UNKNOWN COMMAND
3: Right Stick :: -1 = Left | +1 = Right 
4: Right Stick :: -1 = Up   | +1 = Down
"""


class analog:
    def no_action(self):
        {
            0: (0.0),
            1: (0.0),
            2: (0.0),
            3: (0.0),
            4: (0.0)
        }

    def left_stick_up(self):
        {
            0: (0.0),
            1: (-1.0),
            2: (0.0),
            3: (0.0),
            4: (0.0)
        }

    def left_stick_down(self):
        {
            0: (0.0),
            1: (1.0),
            2: (0.0),
            3: (0.0),
            4: (0.0)
        }

    def left_stick_left(self):
        {
            0: (-1.0),
            1: (0.0),
            2: (0.0),
            3: (0.0),
            4: (0.0)
        }

    def left_stick_right(self):
        {
            0: (1.0),
            1: (0.0),
            2: (0.0),
            3: (0.0),
            4: (0.0)
        }

    def unknown_action_1(self):
        {
            0: (0.0),
            1: (0.0),
            2: (-1.0),
            3: (0.0),
            4: (0.0)
        }

    def unknown_action_2(self):
        {
            0: (0.0),
            1: (0.0),
            2: (1.0),
            3: (0.0),
            4: (0.0)
        }

    def right_stick_up(self):
        {
            0: (0.0),
            1: (0.0),
            2: (0.0),
            3: (0.0),
            4: (-1.0)
        }

    def right_stick_down(self):
        {
            0: (0.0),
            1: (1.0),
            2: (0.0),
            3: (0.0),
            4: (1.0)
        }

    def right_stick_left(self):
        {
            0: (0.0),
            1: (0.0),
            2: (0.0),
            3: (-1.0),
            4: (0.0)
        }

    def right_stick_right(self):
        {
            0: (1.0),
            1: (0.0),
            2: (0.0),
            3: (1.0),
            4: (0.0)
        }

