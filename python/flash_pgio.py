import time
import pigpio

gpio = pigpio.pi()
for i in range(0,50):
	gpio.write(4,i%2)
	time.sleep(1)

gpio.write(4,0)
