# Usage

.. code-block:: python

    from time import sleep

    from rpi_displays.sainsmart.displays import LCD2004

    lcd = LCD2004()

    lcd.display_string('********************', 1)
    lcd.display_string('*   Have a nice    *', 2)
    lcd.display_string('*        Day!      *', 3)
    lcd.display_string('********************', 4)

    sleep(5)
    lcd.clear()
    sleep(1)

    lcd.switch_backlight(0)


``rpi-displays`` can handle multiline messages::

    from rpi_displays.sainsmart.displays import LCD2004

    lcd = LCD2004()
    lcd.text('This is a very long text that has more than 20 chars and look what happens', 1)
