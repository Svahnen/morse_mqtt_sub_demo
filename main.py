import paho.mqtt.client as mqtt
import time
def on_connect(client, userdata, flags, rc):
	# This will be called once the client connects
	print(f"Connected with result code {rc}")
	# Subscribe here!
	client.subscribe("morse")
def on_message(client, userdata, msg):
	#print(f"Message received [{msg.topic}]: {msg.payload}")
	#print(msg.payload.decode("utf-8"))
	#print(msg.payload[0])

	if msg.payload[0] == 46:
		print("inside 46")
		f = open("/sys/class/leds/led0/brightness", "w")
		f.write("1")
		f.close()
		time.sleep(0.1)
		f = open("/sys/class/leds/led0/brightness", "w")
		f.write("0")
		f.close()
	elif msg.payload[0] == 95:
		print("inside 95")
		f = open("/sys/class/leds/led0/brightness", "w")
		f.write("1")
		f.close()
		time.sleep(0.5)
		f = open("/sys/class/leds/led0/brightness", "w")
		f.write("0")
		f.close()

client = mqtt.Client("jonny_pi_sub") # client ID "mqtt-test"
client.on_connect = on_connect
client.on_message = on_message
client.connect('35.228.72.67', 1883)
client.loop_forever()  # Start networking daemon


