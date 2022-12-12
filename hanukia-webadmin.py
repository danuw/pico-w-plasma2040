import WIFI_CONFIG
import network
import socket
import time
import machine
import plasma
from plasma import plasma_stick

  
from machine import Pin
 
 
## on leds init 
onLeds = [170,171,172,173,162,154,155,156,157,146,138,139,140,141,130,128,122,123,124,125,127,114,112,105,106,107,108,109,110,111,98,96,90,91,92,93,95,82,80,74,75,76,77,66,58,59,60,61,50,42,43,44,45];

# Set how many LEDs you have
NUM_LEDS = len(onLeds)
NUM_LEDS2 = 32*8

# The SPEED that the LEDs cycle at (1 - 255)
SPEED = 20

# How many times the LEDs will be updated per second
UPDATES = 60

offset = 0.0

def lightUp(ledArray, color, offset):
    # function body 

    for i in range(len(ledArray)):
        hue = float(i) / len(ledArray)
        led_strip.set_hsv(ledArray[i], color, offset, 0.9)
        
    return

def clearLights():
    # function body 
    for i in range(NUM_LEDS2):
        led_strip.set_hsv(i, 0, 0, 0)
        
    return

### web server init

intled = machine.Pin("LED", machine.Pin.OUT)

led = Pin(15, Pin.OUT)
stateis = ""

ssid = WIFI_CONFIG.SSID
password = WIFI_CONFIG.PSK

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

html = """<!DOCTYPE html>
    <html>
        <head> <title>Pico W</title> </head>
        <body>
        <style>   
            body {
              margin: 40px;
            }

            .wrapper {
              -webkit-column-count: 32;  /* Chrome, Safari, Opera */
              -moz-column-count: 32;     /* Firefox */
              column-count: 32;
              column-gap:0;
              margin:1px;
              padding: 1px;
              /*display: grid;
              auto-flow: row;
              /*grid-template-rows: 100px 100px;
              grid-template-columns: 100px 100px 100px;
              grid-gap: 10px;*/
              background-color: #fff;
              color: #444;
            }

            .box {
              background-color: #444;
              color: #fff;
              border-radius: 5px;
            /*   padding: 20px; */
              font-size: 100%;
              cursor: pointer;
              padding :10px;
              
              display: flex;
              justify-content: center;
              align-items: center;
              gap: 12px;
              aspect-ratio: 1 / 1 ;
            }
            .lightUp{
              background : red;
            }
        </style>
        <h1>Pico W</h1>
            <p>Hello World</p>
            <p>
            <a href='/light/on'>Turn Light On</a>
            </p>
            <p>
            <a href='/light/off'>Turn Light Off</a>
            </p>
            <br>            
            <div class="wrapper">
            </div>
            <div class="result">
            </div>
            <script type="text/javascript">
              window.addEventListener("DOMContentLoaded", function() {
                  let rownb = 8;
                  let colnb = 32;
                  let total = rownb * colnb;
                  let wrapperDiv = document.querySelectorAll(".wrapper")[0];
                  
                  for (let i = 0; i < total; i++) {
                    let currentcolnb = Math.floor(i / rownb);
                    let currentrownb = i% rownb;
                    let index = i + 1;
                    if( currentcolnb % 2 == 0){
                      index = rownb*currentcolnb+ (rownb-currentrownb);
                    }
                    wrapperDiv.innerHTML += '<div class="box a" data-lednb="'+(total -index)+'">'+(total -index)+'</div>';
                    //wrapperDiv.innerHTML += '<div class="box a" data-lednb="'+i+'">'+index+"-"+(rownb-currentrownb)+"-"+currentrownb+"-"+currentcolnb % 2+'</div>';
                  }
                  
                  let boxes = document.querySelectorAll(".box");
                  Array.from(boxes, function(box) {
                    box.addEventListener("click", function() {
                      //alert(this.classList[1]);
                      this.classList.toggle("lightUp");
                      
                      let onLeds = document.querySelectorAll(".lightUp");
                      let ledlist=[]; 
                      for(let j=0; j < onLeds.length; j++){
                        ledlist.push(onLeds[j].getAttribute("data-lednb"));
                      }
                      let resultDiv = document.querySelectorAll(".result")[0];
                      resultDiv.innerHTML = "<a href='/light/on?points="+ledlist.join(",")+"'>Switch on:"+ledlist.join(",")+"</a>";
                    });
                  });
                });
            </script>
        </body>
    </html>
"""
 
# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )
 
# Open socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
 
s = socket.socket()
s.bind(addr)
s.listen(1)
 
print('listening on', addr)

stateis = ""

# WS2812 / NeoPixel™ LEDs
led_strip = plasma.WS2812(NUM_LEDS2, 0, 0, plasma_stick.DAT, color_order=plasma.COLOR_ORDER_RGB)

# Start updating the LED strip
led_strip.start()

start = time.time()

#default state
stateON = True

# Listen for connections
while True:
    try:
        cl, addr = s.accept()
        print('client connected from', addr)

        request = cl.recv(1024)
        print(request)

        request = str(request)
        led_on = request.find('/light/on')
        led_off = request.find('/light/off')
        print( 'led on = ' + str(led_on))
        print( 'led off = ' + str(led_off))

        if led_on == 6:
            print("led on")
            intled.value(1)
            stateON = True
            
            if "?" in request:
                print(request.split("?"))
                params = request.split("?")[1]
                if "&" in params:
                    paramsList = params.split("&")
                    print(paramsList)
                    for i in range(len(paramsList)):
                        if "points=" in paramsList[i] :
                            print(paramsList[i])
                            my_str = paramsList[i].split("=")[1]
                else :
                    my_str = params.split("=")[1]
                print(my_str)
                onLeds = [int(item) for item in my_str.split(",") if item.isdigit()]
                print(len(onLeds))


            stateis = "LED is ON"
            
        if led_off == 6:
            print("led off")
            intled.value(0)
            clearLights()
            stateON = False
            stateis = "LED is OFF"
        
#         todo : make asynchronous so we can have animated effects too
        if stateON:
            
            SPEED = min(255, max(1, SPEED))
            
            if time.time() > start + 0.1:
                start = time.time()
                offset += float(SPEED) / 2000.0
                print("Time elapsed: ", start, " - Offset: ", offset) # CPU seconds elapsed (floating point)
            
            offset += float(SPEED) / 2000.0
                
#             lightUp(frFlagWhite, yellow, 0.0)
#             lightUp(frFlagRed, red, 1.0)
#             lightUp(frFlagBlue, blue, 1.0)
            for i in range(len(onLeds)):
                hue = float(i) / len(onLeds)
                led_strip.set_hsv(onLeds[i], hue + offset, 1.0, 1.0)

            time.sleep(1.0 / UPDATES)## need to wait for elapsed time logic


     
        response = html + stateis
        
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
 
    except OSError as e:
        cl.close()
        print('connection closed')
