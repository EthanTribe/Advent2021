# Advent2021
A python program that zooms into part of the Mandelbrot set each day, generating a beautiful image.

Advent_2021.py is adapted from [Mandelbrot.py]() and zooms in to the focal point -0.743643887037158704752191506114774 + 0.131825904205311970493132056385139i by a factor of 10 each day. An HD image is generated with a random predefined colourmap.
Advent_2021_precise.py is needed due to the low default precision of Python floats, otherwise past day __ the image's resolution will rapidly decrease.
In parenthesis after images are the maximum number of iterations (`imax`) before a pixel is counted as being in the Mandelbrot set, which effects the clarity, colour distribution, and runtime of the program.
