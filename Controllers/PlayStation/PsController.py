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
from PlayStation.AnalogControlPatterns import Analog as ACP
from PlayStation.ButtonControlPatterns import Button as BCP
from PlayStation.DPadControlPatterns import DPad as DCP


class PS4Controller(object):
    """Class representing the PS4 controller. Pretty straightforward functionality."""

    controller = None
    axis_data = None
    button_data = None
    hat_data = None

    command = "!M0"

    def init(self):
        """Initialize the joystick components"""

        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

    def listen(self):
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
                -----------------------------------------------------
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
                CONTROL DEFAULT MODE
                """
                # conditions = self.axis_data ==  and self.hat_data == (0, 0)
                # if conditions:
                #     command = "!M0"
                #     print(command)

                """
                BUTTONS
                """
                # if self.button_data[0]:  # Square
                #     command = "!M6"
                #     print(command)
                # elif self.button_data[1]:  # Cross
                #     command = "!M5"
                #     print(command)
                # elif self.button_data[2]:  # Circle
                #     command = "!M7"
                #     print(command)
                # elif self.button_data[3]:  # Triangle
                #     command = "!M8"
                #     print(command)
                # elif self.button_data[4]:  #
                #     command = "!M9"
                #     print(command)
                # elif self.button_data[5]:
                #     return
                # elif self.button_data[6]:
                #     return
                # elif self.button_data[7]:
                #     return
                # elif self.button_data[8]:
                #     return
                # elif self.button_data[9]:
                #     return
                # elif self.button_data[10]:
                #     command = "!M0"
                #     print(command)
                # elif self.button_data[11]:
                #     return
                # elif self.button_data[12]:
                #     return

                """
                ANALOG
                """
                # if self.axis_data[0] == -1.0:  # walk left
                #     command = "!M4"
                #     print(command)
                # elif self.axis_data[0] == 1.0:  # walk right
                #     command = "!M3"
                #     print(command)
                # if self.axis_data[1] == -1.0:  # walk forwards
                #     command = "!M1"
                #     print(command)
                # elif self.axis_data[1] == 1.0:  # walk backwards
                #     command = "!M2"
                #     print(command)
                # elif self.axis_data[4]:
                #     command = "!M3"
                #     print(command)
                # elif self.axis_data[5]:
                #     return
                # elif self.axis_data[6]:
                #     return
                # elif self.axis_data[7]:
                #     return
                # elif self.axis_data[8]:
                #     return
                # elif self.axis_data[9]:
                #     return
                # elif self.axis_data[10]:
                #     return

                """
                D-PAD
                """
                # if self.hat_data[0] == (1, 1):
                #     command = "D 0"
                #     print(command)
                # elif self.hat_data[0] == (1, 0):
                #     command = "D 1"
                #     print(command)
                # elif self.hat_data[0] == (1, -1):
                #     command = "D 2"
                #     print(command)
                # elif self.hat_data[0] == (0, 1):
                #     command = "D 3"
                #     print(command)
                # elif self.hat_data[0] == (0, -1):
                #     command = "D 5"
                #     print(command)
                # elif self.hat_data[0] == (-1, 1):
                #     command = "D 6"
                #     print(command)
                # elif self.hat_data[0] == (-1, 0):
                #     command = "D 7"
                #     print(command)
                # elif self.hat_data[0] == (-1, -1):
                #     command = "D 8"
                #     print(command)

                if platform.system() == "Linux":
                    os.system('clear')
                else:
                    os.system('cls')

                # print(self.button_data)

                # pprint.pprint(self.button_data)    # Buttons
                pprint.pprint(self.axis_data)      # Analog sticks
                # pprint.pprint(self.hat_data)       # D-Pad


if __name__ == "__main__":
    ps4 = PS4Controller()
    ps4.init()
    ps4.listen()

