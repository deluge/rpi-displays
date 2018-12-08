rpi-displays
============

.. image:: https://badge.fury.io/py/rpi-displays.svg
    :target: https://badge.fury.io/py/rpi-displays

.. image:: https://travis-ci.org/deluge/rpi-displays.svg?branch=master
    :target: https://travis-ci.org/deluge/rpi-displays

.. image:: https://codecov.io/gh/deluge/rpi-displays/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/deluge/rpi-displays

.. image:: https://readthedocs.org/projects/rpi-displays/badge/?version=latest
    :target: https://readthedocs.org/projects/rpi-displays/?badge=latest

A Python 3 library to put text to several displays which are connected with a raspberry-pi.


Installation
------------

.. note::

    It requires the ``Adafruit-CharLCD`` package installed on your Raspberry Pi. A more detailed instruction is on `Adafruit_Python_CharLCD <https://github.com/adafruit/Adafruit_Python_CharLCD>`_

.. hint::

    Before you go on, try to use the Adafruit_Python_CharLCD library with a normal user **not root**.
    It could be possible, that you get a ``IOError: [Errno 13] Permission denied``.
    In that case, you have to add your user additional to the group **i2c** with:

    ``sudo usermod -a -G i2c UserName``

    Now your user got the permission for i2c, but last not least we have to activate
    the module.

    ``sudo modprobe i2c-bcm2708``

    I recommend to put the ``i2c-bcm2708`` in the ``/etc/modules`` files. After
    every reboot, the module will be automatically loaded.


If you got the adafruit library up and running, you can simply install the latest stable package using the command

``pip install rpi-displays``


Usage
-----

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


ToDos
-----

It would be nice to get this package more functionality and not only for one thing.
Have a look at the `TODO.rst <https://github.com/deluge/rpi-displays/blob/master/TODO.rst/>`_
So feel free to fork this repo and let it grow!


Prepare for development
-----------------------

A Python 3.6 interpreter is required in addition to pipenv.

.. code-block:: shell

    $ pipenv install --python 3.6 --dev
    $ pipenv shell
    $ pip install -e .


Now you're ready to run the tests:

.. code-block:: shell

    $ pipenv run py.test


Resources
---------

* `Documentation <https://rpi-displays.readthedocs.org/>`_
* `Bug Tracker <https://github.com/deluge/rpi-displays/issues>`_
* `Code <https://github.com/deluge/rpi-displays/>`_
