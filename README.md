# pico-w-plasma2040

>This assume you have already done the basic set ups and know how to upload code to the plasma stick. If you are not sure, you may want to start (here at https://github.com/pimoroni/pimoroni-pico)[https://github.com/pimoroni/pimoroni-pico]

The journey started with getting these (2 LED flexible matrix screens from aliexpress)[https://www.aliexpress.com/item/4000544584524.html] and then wanted to display a hanukia on it for my daughter's school.
So in order to figure out the coordinates of each pixel to draw and light up (and hoping to use in the web server capabilities in the future) it started by creating these codepen(s):
- Interface for 32 by 8: https://codepen.io/danuw/pen/VwdREpp
- Interface for 16 by 16: https://codepen.io/danuw/pen/MWXdQvz

After about an evening of CSS faffing and calibrating, I could get the coordinates to reach this outcome: https://twitter.com/i/status/1601020048042520576. 

So if you are interested in a quick way of drawing random patterns (or fonts), this may be of help to you too.

# How to use?

You have 2 options for now.

## Open 1 - manual setup

In this scenario, connect to the codepen above (according to your screen size), select the boxes to light up, and copy paste that list into the `onLeds` array [here](https://github.com/danuw/pico-w-plasma2040/blob/main/hanukia.py#L10).

## Option 2 - Wed admin interface

First you will need a file with your wifi credentials as shown here https://github.com/danuw/pico-w-plasma2040/blob/main/hanukia-webadmin.py#L51-L52
You 

# Bonus special FIFA World Cup?

... your very own score board :) (a bit of manual process still but will get to that next)

https://github.com/danuw/pico-w-plasma2040/blob/main/fifaworldcup22.py

# Todo next

- [X] inital web admin 
- [ ] use async to ensure the rainbow pattern is animated
- [ ] add images to the readme
