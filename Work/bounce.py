# bounce.py
#
# Exercise 1.5
height = 100.0
bounce = 1

while bounce <= 10:
    height = height - 2 / 5 * height
    height = round(height, 2)
    print(bounce, " ", height)
    bounce += 1
