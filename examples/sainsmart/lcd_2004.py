from time import sleep

from rpi_displays.sainsmart.displays import LCD2004


# a custom icon, consisting of 6 individual characters
# 3 chars in the first row and 3 chars in the second row
fontdata1 = [
    [0x00, 0x00, 0x03, 0x04, 0x08, 0x19, 0x11, 0x10],
    [0x00, 0x1F, 0x00, 0x00, 0x00, 0x11, 0x11, 0x00],
    [0x00, 0x00, 0x18, 0x04, 0x02, 0x13, 0x11, 0x01],
    [0x12, 0x13, 0x1b, 0x09, 0x04, 0x03, 0x00, 0x00],
    [0x00, 0x11, 0x1f, 0x1f, 0x0e, 0x00, 0x1F, 0x00],
    [0x09, 0x19, 0x1b, 0x12, 0x04, 0x18, 0x00, 0x00],
    [0x1f, 0x0, 0x4, 0xe, 0x0, 0x1f, 0x1f, 0x1f],
]

fontdata2 = [
    [0x1, 0x3, 0x7, 0xf, 0xf, 0x7, 0x3, 0x1],
    [0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10],
    [0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18],
    [0x1c, 0x1c, 0x1c, 0x1c, 0x1c, 0x1c, 0x1c, 0x1c],
    [0x1e, 0x1e, 0x1e, 0x1e, 0x1e, 0x1e, 0x1e, 0x1e],
    [0x0, 0x1, 0x3, 0x7, 0xf, 0x1f, 0x1f, 0x1f],
]

lcd = LCD2004()
lcd.display_string('RPi I2C test', 1)
lcd.display_string(' Custom chars', 2)

sleep(2)

lcd.clear()

# Set logo chars (fontdata1)
lcd.set_custom_chars(fontdata1)

# Write first three chars to row 1 directly
lcd.set(0x80)
lcd.set_char(0)
lcd.set_char(1)
lcd.set_char(2)

# Write next three chars to row 2 directly
lcd.set(0xC0)
lcd.set_char(3)
lcd.set_char(4)
lcd.set_char(5)
sleep(2)

lcd.clear()

lcd.display_string_position('Testing', 1, 1)
sleep(1)

lcd.display_string_position('Testing', 2, 3)
sleep(1)
lcd.clear()

# Set logo chars from the second set
lcd.set_custom_chars(fontdata2)

block = chr(255)  # block character, built-in

# display two blocks in columns 5 and 6 (i.e. AFTER pos. 4) in row 1
# first draw two blocks on 5th column (cols 5 and 6), starts from 0
lcd.display_string_position(block * 2, 1, 4)

# chars starting from col. 7 (pos. 6)
pos = 6
lcd.display_string_position(chr(1), 1, 6)
sleep(0.2)

lcd.display_string_position(chr(2), 1, pos)
sleep(0.2)

lcd.display_string_position(chr(3), 1, pos)
sleep(0.2)

lcd.display_string_position(chr(4), 1, pos)
sleep(0.2)

lcd.display_string_position(block, 1, pos)
sleep(0.2)


# another one, same as above, 1 char-space to the right
pos = pos + 1  # increase column by one

lcd.display_string_position(chr(1), 1, pos)
sleep(0.2)

lcd.display_string_position(chr(2), 1, pos)
sleep(0.2)

lcd.display_string_position(chr(3), 1, pos)
sleep(0.2)

lcd.display_string_position(chr(4), 1, pos)
sleep(0.2)

lcd.display_string_position(block, 1, pos)
sleep(0.2)


# set first set of custom chars - smiley
lcd.set_custom_chars(fontdata1)

lcd.display_string_position(chr(0), 1, 9)
lcd.display_string_position(chr(1), 1, 10)
lcd.display_string_position(chr(2), 1, 11)
lcd.display_string_position(chr(3), 2, 9)
lcd.display_string_position(chr(4), 2, 10)
lcd.display_string_position(chr(5), 2, 11)
sleep(2)

lcd.clear()
sleep(1)

lcd.switch_backlight(0)
