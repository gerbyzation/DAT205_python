
# import libraries
import serial
import mosquitto
import random

# connecting to broker
client = mosquitto.Mosquitto("DAT205")
client.connect("127.0.0.1")
client.subscribe("simon/test")

# connnecting to arduino serial port
port = serial.Serial("/dev/tty.usbmodem1411", 9600, timeout=2)
input = port.readline()

# receives message from broker and sends command over serial to arduino
def messageReceived(broker, obj, msg):
    global client
    print("Message " + msg.topic + " containing: " + msg.payload)
    port.write(str(msg.payload))

client.on_message = messageReceived

while(True):
    client.loop()
