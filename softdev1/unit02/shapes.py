def circle_area():
    rad = int(input("enter a radius"))
    ans1 = 3.1415*rad**2
    print(ans1)
circle_area()
def sph():
    rad1 = int(input("enter a radius"))
    ans2 = 4/3*3.1415*rad1**3
    print(ans2)
sph()
def area_rec():
   ht = int(input("enter a height")) 
   width = int(input("enter a width"))
   ans3 = ht *width
   print(ans3)
area_rec()
def area_sq():
    side = int(input("enter a side length"))
    ans4 = side**2
    print(ans4)
area_sq()
def isos():
    height = int(input("enter a height"))
    leg = int(input("enter a leg"))
    ans5 = (leg*height)/2
    print(ans5)
isos()
def eq():
    length = int(input("enter a length"))
    ans6 = (sqrt(3)/4)*length**2
    print(ans6)