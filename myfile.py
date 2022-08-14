# print("Hello World")


# if 2 > 1:
#     print("true")


# Type casting
# a = 10
# b = "Value: "

# print(b+str(a))


# Text
# text = """Lorem Ipsum is simply dummy text of the
#  printing and typesetting industry.
#   Lorem Ipsum has been the industry's
#    standard dummy text ever since the 1500s, """

# print(text[0:8])
# print(len(text))


# MARKSHEET
# name = input("Enter your name: ")
# english = int(input("Enter english marks: "))
# urdu = int(input("Enter urdu marks: "))
# maths = int(input("Enter maths marks: "))
# totalMarks = int(input("Enter total marks: "))


# obtMarks = english+urdu+maths
# percetage = (obtMarks / totalMarks)*100

# print(name + ", You got " + str(format(percetage, ".2f"))+"%")

# Markhseet Ends here


# Objects
myProfile = {
    "name": "Ghulam Qadir",
    "email": "ghulamqadirsakaria25@gmail.com",
    "skills": ["Web Developer", "Flutter Developer"]
}
print(myProfile)
print(myProfile.get("skills")[1])


# Functions
def pythonFunct(myName):
    print(myName)


pythonFunct("Ghulam Qadir")
