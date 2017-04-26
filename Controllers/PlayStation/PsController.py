#! /usr/bin/env python
# Source: https://gist.github.com/claymcleod/028386b860b75e4f5472
# -*- coding: utf-8 -*-
#
# This file presents an interface for interacting with the Playstation 4 Controller
# in Python. Simply plug your PS4 controller into your computer using USB and run this
# script!
#
# NOTE: I assume in this script that the only joystick plugged in is the PS4 controller.
#       if this is not the case, you will need to change the class accordingly.
#
# Copyright © 2015 Clay L. McLeod <clay.l.mcleod@gmail.com>
#
# Distributed under terms of the MIT license.


import os
import platform
import pprint
import pygame
import socket

"""
Loading from other files in directory
"""
from .AnalogControlPatterns import Analog as ACP
from .ButtonControlPatterns import Button as BCP
from .DPadControlPatterns import DPad as DCP

class PS4Controller(object):
    """Class representing the PS4 controller. Pretty straightforward functionality."""

    controller = None
    axis_data = None
    button_data = None
    hat_data = None

    command = ""

    def init(self):
        """Initialize the joystick components"""

        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

    def listen(self, command=None):
        """Listen for events to happen"""

        if not self.axis_data:
            self.axis_data = {}

        if not self.button_data:
            self.button_data = {}
            for i in range(self.controller.get_numbuttons()):
                self.button_data[i] = False

        if not self.hat_data:
            self.hat_data = {}
            for i in range(self.controller.get_numhats()):
                self.hat_data[i] = (0, 0)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    self.axis_data[event.axis] = round(event.value, 2)
                elif event.type == pygame.JOYBUTTONDOWN:
                    self.button_data[event.button] = True
                elif event.type == pygame.JOYBUTTONUP:
                    self.button_data[event.button] = False
                elif event.type == pygame.JOYHATMOTION:
                    self.hat_data[event.hat] = event.value

                # Insert your code on what you would like to happen for each event here!
                # In the current setup, I have the state simply printing out to the screen.

                """
                command	        action	                    eye color
                #M0	            Stop	                    Blue
                #M1	            Move Forward	            Blue
                #M2	            Move Back	                Blue
                #M3	            Turn right	                Blue
                #M4	            Turn left	                Blue
                #M5	            Wave both hands	            Green
                #M6	            Wave right hands	        Yellow
                #M7	            Grip both hands	            Blue
                #M8	            Wave left hand	            Red
                #M9	            Stretch out right hand	    Blue
                """

                """
                BUTTONS
                """
                if self.button_data == BCP.no_action():
                    return
                elif self.button_data == BCP.cross():
                    command = "!M6"
                    return command
                elif self.button_data == BCP.circle():
                    command = "!M5"
                    return command
                elif self.button_data == BCP.triangle():
                    command = "!M7"
                    return command
                elif self.button_data == BCP.square():
                    command = "!M8"
                    return command
                elif self.button_data == BCP.l1:
                    command = "!M9"
                    return command
                elif self.button_data == BCP.r1:
                    return
                elif self.button_data == BCP.l2:
                    return
                elif self.button_data == BCP.r2:
                    return
                elif self.button_data == BCP.unknown_command_1():
                    return
                elif self.button_data == BCP.unknown_command_2():
                    return
                elif self.button_data == BCP.ps_and_touch_button():
                    command = "!M0"
                    return command
                elif self.button_data == BCP.l3:
                    return
                elif self.button_data == BCP.r3:
                    return

                """
                ANALOG
                """
                if self.axis_data == ACP.no_action():
                    return
                elif self.axis_data == ACP.left_stick_up():
                    command = "!M1"
                    return command
                elif self.axis_data == ACP.left_stick_down():
                    command = "!M2"
                    return command
                elif self.axis_data == ACP.left_stick_left():
                    command = "!M4"
                    return command
                elif self.axis_data == ACP.left_stick_right():
                    command = "!M3"
                    return command
                elif self.axis_data == ACP.unknown_action_1():
                    return
                elif self.axis_data == ACP.unknown_action_2():
                    return
                elif self.axis_data == ACP.right_stick_up():
                    return
                elif self.axis_data == ACP.right_stick_down():
                    return
                elif self.axis_data == ACP.right_stick_left():
                    return
                elif self.axis_data == ACP.right_stick_right():
                    return

                """
                D-PAD
                """
                if self.hat_data == DCP.no_action():
                    return
                elif self.hat_data == DCP.up():
                    return
                elif self.hat_data == DCP.down():
                    return
                elif self.hat_data == DCP.left():
                    return
                elif self.hat_data == DCP.right():
                    return

                if platform.system() == "Linux":
                    os.system('clear')
                else:
                    os.system('cls')

                pprint.pprint(self.button_data)    # Buttons
                pprint.pprint(self.axis_data)      # Analog sticks
                pprint.pprint(self.hat_data)       # D-Pad



if __name__ == "__main__":
    ps4 = PS4Controller()
    ps4.init()
    ps4.listen()


