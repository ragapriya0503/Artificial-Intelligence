class Classlist():
    def Subfields():
        print("Sub-Fields in AI are:")
        print("Machine Learning")
        print("Neutral Network")
        print("Vision")
        print("RObotics")
        print("Speech Processing")
        print("Natural Language Processing")
    @staticmethod   
    def OddEven():
        number=int(input("Enter a number:"))
        if((number%2)==0):
            message=str(number) + " Is Even"
        else:
            message=str(number) + " Is Odd"
        return message

    def Eligible():
        age=int(input("Enter Your age:"))
        gender=input("Enter Your Gender:")
        if(gender.lower()=="female"):
            if(age>=18):
              eligible="You are eligible"
            else:
                eligible="You are not eligible"
        elif(gender.lower()=="male"):
            if(age>=21):
                eligible="You are eligible"
            else:
                eligible="You are not eligible"
        return eligible
        
    def Percentage():
        tamil=float(input("Tamil:"))
        english=float(input("English:"))
        maths=float(input("Maths:"))
        science=float(input("Science:"))
        socialScience=float(input("SocialScience:"))
        total=tamil+english+maths+science+socialScience
        percentage=float(total/5)
        print("Total:",total)
        print("Percentage:",percentage)
        
    def TriangleCal():
        height=float(input("Height:"))
        breath=float(input("Breath:"))
        area=float(height*breath)/2
        print("Area of Triangle:",area)
        height1=float(input("Height1:"))
        height2=float(input("Height2:"))
        breadth2=float(input("Breadth:"))
        perimetr=float(height1+height2+breadth2)
        print("Area of Triangle:",perimetr)