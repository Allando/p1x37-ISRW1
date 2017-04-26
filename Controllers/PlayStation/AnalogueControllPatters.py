#!/usr/bin/env python3
"""
Well, lads, this is a big one!
0: Left Stick  :: -1 = Left | +1 = Right 
1: Left Stick  :: -1 = Up   | +1 = Down
2: UNKNOWN COMMAND
3: Right Stick :: -1 = Left | +1 = Right 
4: Right Stick :: -1 = Up   | +1 = Down
"""


def no_action():
    {
        0: (0.0),
        1: (0.0),
        2: (0.0),
        3: (0.0),
        4: (0.0)
    }


def left_stick_up():
    {
        0: (0.0),
        1: (-1.0),
        2: (0.0),
        3: (0.0),
        4: (0.0)
    }


def left_stick_down():
    {
        0: (0.0),
        1: (1.0),
        2: (0.0),
        3: (0.0),
        4: (0.0)
    }


def left_stick_left():
    {
        0: (-1.0),
        1: (0.0),
        2: (0.0),
        3: (0.0),
        4: (0.0)
    }


def left_stick_right():
    {
        0: (1.0),
        1: (0.0),
        2: (0.0),
        3: (0.0),
        4: (0.0)
    }


def unknown_action_1():
    {
        0: (0.0),
        1: (0.0),
        2: (-1.0),
        3: (0.0),
        4: (0.0)
    }


def unknown_action_2():
    {
        0: (0.0),
        1: (0.0),
        2: (1.0),
        3: (0.0),
        4: (0.0)
    }


def right_stick_up():
    {
        0: (0.0),
        1: (0.0),
        2: (0.0),
        3: (0.0),
        4: (-1.0)
    }


def right_stick_down():
    {
        0: (0.0),
        1: (1.0),
        2: (0.0),
        3: (0.0),
        4: (1.0)
    }


def left_stick_left():
    {
        0: (0.0),
        1: (0.0),
        2: (0.0),
        3: (-1.0),
        4: (0.0)
    }


def left_stick_right():
    {
        0: (1.0),
        1: (0.0),
        2: (0.0),
        3: (1.0),
        4: (0.0)
    }

