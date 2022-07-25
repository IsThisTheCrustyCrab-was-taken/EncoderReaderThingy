from machine import Pin, UART, sleep

# setup p12 and p14 as input
p12 = Pin(12, Pin.IN, Pin.PULL_UP)
p14 = Pin(14, Pin.IN, Pin.PULL_UP)
# setup serial
serial = UART(1, 9600)
serial.init(9600, 8, None, 1)

def test():
    while True:
        print(p12.value(), " ", p14.value())
        sleep(0.1)