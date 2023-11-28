
# bounce.py
#
# Exercise 1.5

height = 100
bounce = 100.0
counter = 1

while bounce > 1.00:
    bounce = bounce * (3/5)
    print(f'{counter} {round(bounce, 4)}')
    counter = counter + 1
