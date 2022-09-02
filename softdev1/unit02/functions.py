def age_calc():
    yr = int(input("enter the current year "))
    month = int(input("enter current month "))
    yr2 = int(input("enter your birth year "))
    age = (yr2 -yr)*12 + month
    print("You are",end=" ")
    print(age , end="")
    print(" months old")

def main():
    age_calc()
    age_calc()
    age_calc()
main()