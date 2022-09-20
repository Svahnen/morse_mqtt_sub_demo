f = open("/sys/class/leds/led0/brightness", "w")
f.write("1")
f.close()
