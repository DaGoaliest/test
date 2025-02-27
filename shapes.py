import math

l = input("length: ")
w = input("width: ")

area = int(l) * int(w)
print(f"The area of this rectangle is {area}")

r = input("radius: ")

cArea = float(r) ** 2 * math.pi
print(f"The area of the circle is {cArea}")


tb = input("triangle base: ")
th = input("triangle height: ")

tArea =  (int(tb) * int(th)) / 2
print(f"the area of the triangle is {tArea}")