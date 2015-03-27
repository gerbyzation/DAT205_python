
# import libraries
import serial
import mosquitto
import random

# connecting to broker
client = mosquitto.Mosquitto("Gerrit")
client.connect("141.163.83.22")
client.subscribe("lights")

# connnecting to arduino serial port
port = serial.Serial("/dev/tty.usbmodem1411", 9600, timeout=2)
input = port.readline()

# receives message from broker and sends command over serial to arduino
def messageReceived(broker, obj, msg):
    global client
    print("Message " + msg.topic + " containing: " + msg.payload)
    if msg.payload == "ON":
        port.write(str(1))
    elif msg.payload == "OFF":
        port.write(str(0))

client.on_message = messageReceived

while(True):
    client.loop()
