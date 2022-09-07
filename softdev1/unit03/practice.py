def convert_height():
   height = int(input("Enter height in inches: "))
   height_2 = height//12
   height_3 = height%12

   print("You are ", height_2,  height_3, "", "tall")  
convert_height()

