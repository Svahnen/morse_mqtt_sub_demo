import paho.mqtt.client as mqtt  # Import the MQTT library
import time  # Import the time library so we can use sleep


def on_connect(client, userdata, flags, rc):
    # This will be called once the client connects
    print(f"Connected with result code {rc}")
    # Subscribe
    client.subscribe("morse")


def on_message(client, userdata, msg):
    # This will be called when a message is received

    # Depending on message we write to a file
    # to set the brightness of the internal LED
    # The file first have to be given write access
    if msg.payload[0] == 46:  # 46 is the ASCII code for "."
        print("inside 46")
        f = open("/sys/class/leds/led0/brightness", "w")
        f.write("1")
        f.close()
        time.sleep(0.1)
        f = open("/sys/class/leds/led0/brightness", "w")
        f.write("0")
        f.close()
    elif msg.payload[0] == 95:  # 95 is the ASCII code for "_"
        print("inside 95")
        f = open("/sys/class/leds/led0/brightness", "w")
        f.write("1")
        f.close()
        time.sleep(0.5)
        f = open("/sys/class/leds/led0/brightness", "w")
        f.write("0")
        f.close()


client = mqtt.Client("jonny_pi_sub")  # client ID
client.on_connect = on_connect  # Set the on_connect callback
client.on_message = on_message  # Set the on_message callback
client.connect('35.228.72.67', 1883)
client.loop_forever()  # Start the main loop
