# pin mapping from Pycom to NodeMCU-32S
# Using this mapping, add to 'from pin_map import *'
GPIO3 = 'P0'
GPIO1 = 'P1'
GPIO0 = 'P2'
GPIO4 = 'P3'
GPIO15 = 'P4'
GPIO5 = 'P5'
GPIO27 = 'P6'
GPIO19 = 'P7'
GPIO2 = 'P8'  #OnBoard LED in NodeMCU-32S
GPIO12 = 'P9'
GPIO13 = 'P10'
GPIO22 = 'P11'
GPIO21 = 'P12'
GPIO36 = 'P13' #Input Pin in WiPy
#GPI37 = 'P14' #Not assign in NodeMCU-32S
#GPI38 = 'P15' #Not assign in NodeMCU-32S
GPIO39 = 'P16' #Input Pin in WiPy
GPIO35 = 'P17' #Input Pin in WiPy
GPIO34 = 'P18' #Input Pin in WiPy
GPIO32 = 'P19'
GPIO33 = 'P20'
GPIO26 = 'P21'
GPIO25 = 'P22'
GPIO14 = 'P23'

if __name__ == "__main__":
    print("Initialize done pin mapping from WiPy of Pycom to NodeMCU-32S")
