THINGS:

A specific process on the Pi allows for interfacing with the GPIO. It's called pigpiod and it must be running to use the gpio.

To check if it's running, run:

  $ ps -ef | grep pigpiod

Output should look like:

  root      1837     1  7 20:00 ?        00:00:52 pigpiod
  pi        1868  1861  0 20:12 pts/1    00:00:00 grep --color=auto pigpiod

If it doesn't then start it, using:

  $ sudo pigpiod

From there you can use the pigpio socket interfaces to control the GPIO.

Note that if you want to use more advanced features of the library, you can read the man page to learn what they are:

  $ man gpiod

CONSIDERATIONS:

There are python and c interfaces for the GPIO control. They may use different names when referring to the same GPIO, so make sure you're using the correct naming convension.
