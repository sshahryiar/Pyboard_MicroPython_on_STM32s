from pyb import LED, Pin, SPI
from machine import I2C
from micropython import const
from SSD1306_I2C import OLED1306
from AHT15 import AHT15
from SPL06_007 import SPL06
from utime import sleep_ms
import framebuf


background = framebuf.FrameBuffer(bytearray(
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x04\x00\x02\x22\xa0\xa4\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x40\x20\x18\x20\x40\x00'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x40\x20\x90\x48\x28\x60\x14\x14\x14\x14\x14\x14\x14\x14\x60\x28\x48\x90\x20\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\xff\x00\x50\x50\x50\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x60\x10\x08\x06\x01\x00\x00\x00\x00\x00\x01'
    b'\x06\x88\x10\x60\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x06\x61'
    b'\x06\x41\x40\x44\x80\x80\x81\x80\xe0\x80\x80\xe0\x10\x11\x08\x00\x44\x40\x41\x06\x61\x06\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x30\xcc\x32\x08\x05\x02\x03\x00\x00\x03\x02\x05\x08\x32\x08\xf0\x00\x00\x00\x00\x00'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x70\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x00\x02\xfc\x00\x06\x70\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x10'
    b'\x66\x48\xb0\x40\x40\x83\x82\x01\x00\x00\x00\x00\x00\x80\x80\x40\x40\xb0\x48\x66\x10\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x08\x16\x28\x50\x40\x00\x20\x20\x40\x50\x50\x28\x16\x08\x07\x00\x00\x00\x00\x00'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x0c\x08\x10\x20\x00\x40\x40\x40\x50\x50\x40\x48'
    b'\x08\x24\x12\x00\x0c\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x00\x00\x01\x00\x1e\x12\xf0\x15\x15\x15\x15\xf0\x12\x1e\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
    128, 40, framebuf.MONO_VLSB)


led = LED(1)

cs_pin = Pin('PB0', Pin.OUT_PP)

TWI = I2C(scl = 'PB9', sda = 'PB8', freq = 400000)

spi = SPI(1, mode = SPI.MASTER, baudrate = 2000000, polarity = 1, phase = 1, bits = 8, firstbit = SPI.MSB)

baro = SPL06(spi, cs_pin)
rht = AHT15(TWI)

oled = OLED1306(TWI)
oled.fill(oled.BLACK)
oled.show()
#sleep_ms(1000)


while(True):
    AHT15_RH, AHT15_T, AHT15_status, AHT15_CRC = rht.read_sensor()
    SPL06_T = baro.get_tmp()
    SPL06_P = baro.get_prs()
    
    T_avg = ((AHT15_T + SPL06_T) / 2.0)
    
    oled.fill(oled.BLACK)
    oled.blit(background, 0, 15)
    oled.text("Weather Station", 2, 2)
    oled.text(str("%2.1f" %T_avg), 1, 56)
    oled.text(str("%2.1f" %AHT15_RH), 40, 56)
    oled.text(str("%2.1f" %SPL06_P), 80, 56)
    oled.show()
    
    print("T.A/'C: " + str("%2.2f" %AHT15_T))
    print("T.S/'C: " + str("%2.2f" %SPL06_T))
    print("R.H./%: " + str("%2.2f" %AHT15_RH))
    print("P/mBar: " + str("%2.2f" %SPL06_P))
    print(" ")
    led.toggle()
    
    sleep_ms(1000)
    