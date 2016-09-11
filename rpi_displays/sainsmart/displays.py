# -*- coding: utf-8 -*-
from time import sleep

from ..channels import I2C
from .constants import (
    LCD_2LINE, LCD_4BITMODE, LCD_BACKLIGHT, LCD_CLEARDISPLAY, LCD_DISPLAYCONTROL, LCD_DISPLAYON,
    LCD_ENTRYLEFT, LCD_ENTRYMODESET, LCD_FUNCTIONSET, LCD_NOBACKLIGHT, LCD_RETURNHOME, En,
    LCD_5x8DOTS, Rs)


class LCD2004:
    """
    This is the driver for the SainSmart LCD 2004 models.
    It can be used for the 16x2 and 20x4
    """

    def __init__(
            self, address=0x27, lines=LCD_2LINE, dots=LCD_5x8DOTS, bitmode=LCD_4BITMODE,
            backlight=LCD_BACKLIGHT):
        self.device = I2C(address)
        self.backlight = backlight

        self.set(0x03)
        self.set(0x03)
        self.set(0x03)
        self.set(0x02)

        self.set(LCD_FUNCTIONSET | lines | dots | bitmode)
        self.set(LCD_DISPLAYCONTROL | LCD_DISPLAYON)
        self.set(LCD_ENTRYMODESET | LCD_ENTRYLEFT)
        sleep(0.2)

    # clocks EN to latch command
    def strobe(self, data):
        self.device.write_cmd(data | En | LCD_BACKLIGHT)
        sleep(.0005)
        self.device.write_cmd(((data & ~En) | LCD_BACKLIGHT))
        sleep(.0001)

    def set_four_bits(self, data):
        self.device.write_cmd(data | LCD_BACKLIGHT)
        self.strobe(data)

    def set(self, cmd, mode=0):
        self.set_four_bits(mode | (cmd & 0xF0))
        self.set_four_bits(mode | ((cmd << 4) & 0xF0))

    def set_char(self, charvalue, mode=1):
        self.set_four_bits(mode | (charvalue & 0xF0))
        self.set_four_bits(mode | ((charvalue << 4) & 0xF0))

    # custom chars (0 - 7)
    def set_custom_chars(self, fontdata):
        self.set(0x40)
        for char in fontdata:
            for line in char:
                self.set_char(line)

    def display_string(self, string, line):
        if line == 1:
            self.set(0x80)
        if line == 2:
            self.set(0xC0)
        if line == 3:
            self.set(0x94)
        if line == 4:
            self.set(0xD4)

        for char in string:
            self.set(ord(char), Rs)

    def display_string_position(self, string, line, pos):
        if line == 1:
            pos_new = pos
        elif line == 2:
            pos_new = 0x40 + pos
        elif line == 3:
            pos_new = 0x14 + pos
        elif line == 4:
            pos_new = 0x54 + pos

        self.set(0x80 + pos_new)

        for char in string:
            self.set(ord(char), Rs)

    def switch_backlight(self, state):
        if state == 1:
            self.device.write_cmd(LCD_BACKLIGHT)
        elif state == 0:
            self.device.write_cmd(LCD_NOBACKLIGHT)

    def clear(self):
        self.set(LCD_CLEARDISPLAY)
        self.set(LCD_RETURNHOME)
