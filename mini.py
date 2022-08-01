import random
def q1():
    if 1==1:
        
            
            
            
        t=1
        test=[]
        for i in range(30):
            question_number=random.randint(1,15)
            test.append(question_number)
            i=i+t
    
        print(test)
        print ("The original list is : ", test)  
# using naive method
# to remove duplicated 
# from list 
        res = []
        for i in test:
                if i not in res:
                    res.append(i)
        print(res)
        for i in range(1,15):
            #Question :- 1 
            if res[0]==1:
                q1=print("1.world first computer ? \n A.ENIAC \n B.Tata Institute of Fundamental Research Automatic Calculator (TIFRAC) f\nC.Common Operating Machine ")
                ans=input('::')
                if ans=='A':print('right')
                elif ans=='a':print('right')
                else:print('False')
            #Question :- 2
            if res[1]==2:
                q2=print("2.how many generations of computers we have ?\nA.one\nB.ten\nC.five")
                ans=input('::')
                if ans=='C':print('right')
                elif ans=='c':print('right')
                else:print('False')
            #Question :- 3
            if res[2]==3:
                q3=print("3.Who is the father of Computer science ?\nA.stephen hawking\nB.Charles Babbage\nC.abdul kalam")
                ans=input('::')
                if ans=='B':print('right')
                elif ans=='b':print('right')
                else:print('False')
            #Question :- 4
            if res[3]==4:
                q4=print("4.In a computer, most processing takes place in _______?\nA.mouse\nB.keyboard\nC.CPU")
                ans=input('::')
                if ans=='C':print('right')
                elif ans=='c':print('right')
                else:print('False')   
            #Question :- 5
            if res[4]==5:
                q5=print("5.Who is the father of personal computer?\nA.Edward Robert\nb.Charles Babbage\nc.kevin mitnik")
                ans=input('::')
                if ans=='A':print('right')
                elif ans=='a':print('right')
                else:print('False')
            #Question :- 6
            if res[5]==6:
                q6=print('6.IBM stands for _______?\nA.International Business Machines\nB.Interpreted business machines\nC.international barrier machines')
                ans=input('::')
                if ans=='A':print('right')
                elif ans=='a':print('right')
                else:print('False')
            #Question :- 7
            if res[6]==7:
                q7=print('7.DOS stands for _______?\nA. denial operating system\nB. Disk Operating System\nC. deniled operating system')
                ans=input('::')
                if ans=='B':print('right')
                elif ans=='b':print('right')
                else:print('False')
            #Question :- 8
            if res[7]==8:
                q8=print('8.Refresh Rate of monitor is measured in ?\nA.Hertz\nB. pixels\nC. mm')
                ans=input('::')
                if ans=='A':print('right')
                elif ans=='a':print('right')
                else:print('False')
            #Question :- 9
            if res[8]==9:
                q9=print('9.Where are the CPU and memory located?\nA.mouse\nB.motherboard\nC.processor')
                ans=input('::')
                if ans=='B':print('right')
                elif ans=='b':print('right')
                else:print('False')
            #Question :- 10
            if res[9]==10:
                q10=print('10.Full form of MAN?\nA.motrologic area network\nB.Metropolitan Area Network\nC.Monition area network')
                ans=input('::')
                if ans=='B':print('right')
                elif ans=='b':print('right')
                else:print('False')
            #Question :- 11
            if res[10]==11:
                q11=print('11.In which year, the Microsoft company was founded?\nA.1975\nB.1972\nC.1965')
                ans=input('::')
                if ans=='A':print('right')
                elif ans=='a':print('right')
                else:print('False')
            #Question :- 12
            if res[11]==12:
                q12=print('12.What are mouse and joystick?\nA.input devices\nB.prcessing devices\nC.output devices')
                ans=input('::')
                if ans=='A':print('right')
                elif ans=='a':print('right')
                else:print('False')
            #Question :- 13
            if res[12]==13:
                q13=print('13.What kind of memory is both static and non-volatile?\nA.RAM\nB.VRAM\nC.ROM')
                ans=input('::')
                if ans=='C':print('right')
                elif ans=='c':print('right')
                else:print('False')
            #Question :- 14
            if res[13]==14:
                q14=print('14.Where does most data go first with in a computer memory hierarchy?\nA.RAM\nB.ROM\nC.VRAM')
                ans=input('::')
                if ans=='A':print('right')
                elif ans=='a':print('right')
                else:print('False')
                
            #Question :- 15
            if res[14]==15:
                q15=print('15.When did arch rivals IBM and Apple Computers Inc. decide to join hands?\nA.1991\nB.1975\nC.1968')
                ans=input('::')
                if ans=='A':print('right')
                elif ans=='a':print('right')
                else:print('False')
    else:print('error')

def q2():
    if 2==2:
        for i in range(1,15):
            q1=1
            q2=2
            q3=3
            q4=4
            q5=5
            q6=6
            q7=7
            q8=8
            q9=9
            q10=10
            q11=11
            q12=12
            q13=13
            q14=14
            q15=15

            question_number=random.randint(1,15)
            #Question :- 1 
            if question_number==1:
                q1=print("The members of the Rajya Sabha are elected by elected\n(A) members of the Legislative Assembly\n(B) members of Lok Sabha\n(C) members of Rajya Sabha\n(D) members of Supreme court")
                ans=input('::')
                if ans=='A':print('right')
                elif ans=='a':print('right')
                else:print('False')
            #Question :- 2
            if question_number==2:
                q2=print("2.Total number of High Courts in India is?\n(A) 24\n(B) 25\n(C) 26\n(D) 27")
                ans=input('::')
                if ans=='A':print('right')
                elif ans=='a':print('right')
                else:print('False')
            #Question :- 3
            if question_number==3:
                q3=print("3.Who was the first Indian Women President of the United Nations General Assembly.\n(A) Vijay Lakshmi Pandit\n(B) Lata Devi\n(C) Indira Gandhi\n(D) Sarojini Devi")
                ans=input('::')
                if ans=='A':print('right')
                elif ans=='a':print('right')
                else:print('False')
            #Question :- 4
            if question_number==4:
                q4=print("4.Which one of the following article deals with the appointment of the Prime Minister and other ministers?\n(A) Article 76\n(B) Article 74\n(C) Article 75\n(D) Article 72")
                ans=input('::')
                if ans=='C':print('right')
                elif ans=='c':print('right')
                else:print('False')   
            #Question :- 5
            if question_number==5:
                q5=print("5.The Prime Minister is appointed by which one of the following?\n(A) Attorney general of India\n(B) President\n(C) Vice-president\n(D) Chief justice of India")
                ans=input('::')
                if ans=='B':print('right')
                elif ans=='b':print('right')
                else:print('False')
            #Question :- 6
            if question_number==6:
                q6=print('6.The Supreme Court of India at present contains the following number of Judges?\n(A) 25 judges\n(B) 31 judges\n(C) 20 judges\n(D) 30 judges')
                ans=input('::')
                if ans=='B':print('right')
                elif ans=='b':print('right')
                else:print('False')
            #Question :- 7
            if question_number==7:
                q7=print('7.Who among the following appoints the Chief Justice and other Judges of the Supreme Court?\n(A) Prime minister\n(b) Vice-president\n(c) Home minister\n(d) President')
                ans=input('::')
                if ans=='D':print('right')
                elif ans=='d':print('right')
                else:print('False')
            #Question :- 8
            if question_number==8:
                q8=print('8.Which of the following are the powers of the Supreme Court?\n(a) Original and Appellate Jurisdiction\n(b) Appointment of ad-hoc judges\n(c) Judicial review\n(d) All the above')
                ans=input('::')
                if ans=='D':print('right')
                elif ans=='d':print('right')
                else:print('False')
            #Question :- 9
            if question_number==9:
                q9=print('9.Mr. T.S. Thakur is the ...................Chief Justice of India.\n(a) 41st\n(b) 42nd\n(c) 43rd\n(d) 44th')
                ans=input('::')
                if ans=='C':print('right')
                elif ans=='c':print('right')
                else:print('False')
            #Question :- 10
            if question_number==10:
                q10=print('10.The executive power of the Union is vested in which one of the below?\nA. Prime minister\nB. Home minister\nC. Vice-president\nD. President')
                ans=input('::')
                if ans=='D':print('right')
                elif ans=='d':print('right')
                else:print('False')
            #Question :- 11
            if question_number==11:
                q11=print('11.IWhen was the first Parliamentary Forum on Water Conservation and Management constituted?\na. 1950\nb. 2005\nc. 1970\nd. 1985')
                ans=input('::')
                if ans=='B':print('right')
                elif ans=='b':print('right')
                else:print('False')
            #Question :- 12
            if question_number==12:
                q12=print('12.When was the first Parliamentary Forum on Youth constituted?\na) 2010\nb) 2008\nc) 2006\nd) 1985')
                ans=input('::')
                if ans=='C':print('right')
                elif ans=='c':print('right')
                else:print('False')
            #Question :- 13
            if question_number==13:
                q13=print('13.The independence of Judiciary”  in Indian constitution is taken from.\n(a) Britain\n(b) USA\n(c) South Africa\n(d) Australia')
                ans=input('::')
                if ans=='A':print('right')
                elif ans=='a':print('right')
                else:print('False')
            #Question :- 14
            if question_number==14:
                q14=print('14.Which of the following article of the Indian Constitution deals with the constitution of the Parliament of India?\nA. Article 73\nB. Article 78\nC. Article 79\nD. Article 72')
                ans=input('::')
                if ans=='C':print('right')
                elif ans=='c':print('right')
                else:print('False')
                
            #Question :- 15
            if question_number==15:
                q15=print('15.How many number of members are nominated by the President to the Rajya sabha?\nA. 20\nB. 18\nC. 12\nD. 15')
                ans=input('::')
                if ans=='C':print('right')
                elif ans=='c':print('right')
                else:print('False')
    else:print('error')
def q3():
    if 3==3:
        for i in range(1,15):
            q1=1
            q2=2
            q3=3
            q4=4
            q5=5
            q6=6
            q7=7
            q8=8
            q9=9
            q10=10
            q11=11
            q12=12
            q13=13
            q14=14
            q15=15

            question_number=random.randint(1,15)
            #Question :- 1 
            if question_number==1:
                q1=print("A man presses more weight on earth at :\nA.Sitting position \nB.Standing  Position \nC.Lying Position \nD.None of These")
                ans=input('::')
                if ans=='b':print('right')
                elif ans=='B':print('right')
                else:print('False')

            #Question :- 2 
            if question_number==2:
                q2=print("A piece of ice is dropped in a vesel containing kerosene. When ice melts, the level of kerosene will \nA.Rise \nB.Fall \nC.Remain Same \nD.None of These ")
                ans=input('::')
                if ans=='b':print('right')
                elif ans=='B':print('right')
                else:print('False')

            #Question :- 3 
            if question_number==3:
                q1=print("Young's modulus is the property of \nA.Gas only \nB.Both Solid and Liquid \nC.Liquid only \nD.Solid only")
                ans=input('::')
                if ans=='d':print('right')
                elif ans=='D':print('right')
                else:print('False')

            #Question :- 4 
            if question_number==4:
                q1=print("	If electrical conductivity increases with the increase of temperature of a substance, then it is a: \nA.Conductor \nB.Semiconductor \nC.Insulator  \nD.Carborator ")
                ans=input('::')
                if ans=='b':print('right')
                elif ans=='B':print('right')
                else:print('False')

            #Question :- 5 
            if question_number==5:
                q1=print("An artificial Satellite revolves round the Earth in circular orbit, which quantity remains constant? \nA.Angular Momentum \nB.Linear Velocity \nC.Angular Displacement \nD.None of These ")
                ans=input('::')
                if ans=='a':print('right')
                elif ans=='A':print('right')
                else:print('False')

            #Question :- 6 
            if question_number==6:
                q1=print("Minimum distance between and object and real image of a convex lense is: \nA.4<i>f</i> \nB.3<i>f</i> \nC.2<i>f</i> \nD.<i>f</i> ")
                ans=input('::')
                if ans=='A':print('right')
                elif ans=='a':print('right')
                else:print('False')

            #Question :- 7 
            if question_number==7:
                q1=print("Bolometer is used to measure \nA.Frequency \nB.Temperature \nC.Velocity \nD.Wavelength ")
                ans=input('::')
                if ans=='C':print('right')
                elif ans=='c':print('right')
                else:print('False')

            #Question :- 8 
            if question_number==8:
                q1=print("	Product of Force and Velocity is called:\nA.Work \nB.Power \nC.Energy \nD.Momentum ")
                ans=input('::')
                if ans=='B':print('right')
                elif ans=='b':print('right')
                else:print('False')

            #Question :- 9 
            if question_number==9:
                q1=print("Which one of the following has the highest value of specific heat ? \nA.Alcohol \nB.Methane \nC.Kerosene \nD.Water ")
                ans=input('::')
                if ans=='D':print('right')
                elif ans=='d':print('right')
                else:print('False')

            #Question :- 10 
            if question_number==10:
                q1=print("With the increase of pressure, the boiling point of any substance \nA.Increases \nB.Decreases \nC.Remains Same \nD.Becomes zero ")
                ans=input('::')
                if ans=='A':print('right')
                elif ans=='a':print('right')
                else:print('False')

            #Question :- 11 
            if question_number==11:
                q1=print("Elecronegativity is the measure of\nA.Metallic character \nB.Non-metallic character \nC.Basic Character \nD.None of these ")
                ans=input('::')
                if ans=='B':print('right')
                elif ans=='b':print('right')
                else:print('False')

            #Question :- 12 
            if question_number==12:
                q1=print("The rotational effect of a force on a body about an axis of rotation is described in terms of the\nA.Centre of gravity \nB.Centripetal force \nC.Centrifugal force \nD.Moment of force ")
                ans=input('::')
                if ans=='D':print('right')
                elif ans=='d':print('right')
                else:print('False')

            #Question :- 13 
            if question_number==13:
                q1=print("If no external force acts on a system of bodies, the total linear momentum of the system of bodies remains constant. Which law states that ?\nA.Newton's first law \nB.Newton's Second Law \nC.Newton's Third Law \nD.Principle of conservation of linear momentum ")
                ans=input('::')
                if ans=='D':print('right')
                elif ans=='d':print('right')
                else:print('False')

            #Question :- 14 
            if question_number==14:
                q1=print("Which law is also called the law of inertia ?\nA.Newton's first law \nB.Newton's Second Law \nC.Newton's Third Law \nD.All of these ")
                ans=input('::')
                if ans=='A':print('right')
                elif ans=='a':print('right')
                else:print('False')

            #Question :- 15 
            if question_number==15:
                q1=print("What is the unit of Astronomical Distance ?\nA.Light year \nB.Angstrom \nC.Weber \nD.Lux ")
                ans=input('::')
                if ans=='A':print('right')
                elif ans=='a':print('right')
                else:print('False')

def q4():
    if 4==4:
        for i in range(1,15):
            q1=1
            q2=2
            q3=3
            q4=4
            q5=5
            q6=6
            q7=7
            q8=8
            q9=9
            q10=10
            q11=11
            q12=12
            q13=13
            q14=14
            q15=15

            question_number=random.randint(1,15)
            #Question :- 1 
            if question_number==1:
                q1=print("What is the maximum possible length of an identifier? \nA.16 \nB.32 \nC.64 \nD.None of these above ")
                ans=input('::')
                if ans=='D':print('right')
                elif ans=='d':print('right')
                else:print('False')

            #Question :- 2 
            if question_number==2:
                q2=print("Who developed the Python language? \nA.Zim Den \nB.Guido van Rossum \nC.Niene Stom \nD.Wick van Rossum ")
                ans=input('::')
                if ans=='':print('right')
                elif ans=='':print('right')
                else:print('False')

            #Question :- 3 
            if question_number==3:
                q1=print("In which language is Python written? \nA.English \nB.PHP \nC.C \nD.All of the above ")
                ans=input('::')
                if ans=='c':print('right')
                elif ans=='C':print('right')
                else:print('False')

            #Question :- 4 
            if question_number==4:
                q1=print("Which one of the following is the correct extension of the Python file? \nA..py \nB..python \nC..p \nD.None of these ")
                ans=input('::')
                if ans=='':print('right')
                elif ans=='':print('right')
                else:print('False')

            #Question :- 5 
            if question_number==5:
                q1=print("In which year was the Python 3.0 version developed? \nA.2008 \nB.2000 \nC.2010 \nD.2005 ")
                ans=input('::')
                if ans=='a':print('right')
                elif ans=='A':print('right')
                else:print('False')

            #Question :- 6 
            if question_number==6:
                q1=print("What do we use to define a block of code in Python language? \nA.Key \nB.Brackets \nC.Indentation \nD.None of these ")
                ans=input('::')
                if ans=='c':print('right')
                elif ans=='C':print('right')
                else:print('False')

            #Question :- 7 
            if question_number==7:
                q1=print("Which character is used in Python to make a single line comment? \nA./ \nB.// \nC.# \nD.! ")
                ans=input('::')
                if ans=='c':print('right')
                elif ans=='C':print('right')
                else:print('False')

            #Question :- 8 
            if question_number==8:
                q1=print("Which of the following statements is correct regarding the object-oriented programming concept in Python? \nA.Classes are real-world entities while objects are not real \nB.Classes are real-world entities while objects are not real \nC.Both objects and classes are real-world entities \nD.All of the above ")
                ans=input('::')
                if ans=='b':print('right')
                elif ans=='B':print('right')
                else:print('False')

            #Question :- 9 
            if question_number==9:
                q1=print("What is the method inside the class in python language? \nA.Object \nB.Function \nC.Attribute \nD.Argument ")
                ans=input('::')
                if ans=='b':print('right')
                elif ans=='B':print('right')
                else:print('False')

            #Question :- 10 
            if question_number==10:
                q1=print("Which of the following declarations is incorrect? \nA._x = 2 \nB.__x = 3 \nC.__xyz__ = 5 \nD.None of these ")
                ans=input('::')
                if ans=='d':print('right')
                elif ans=='D':print('right')
                else:print('False')

            #Question :- 11 
            if question_number==11:
                q1=print("Why does the name of local variables start with an underscore discouraged? \nA.To identify the variable \nB.It confuses the interpreter \nC.It indicates a private variable of a class \nD.None of these ")
                ans=input('::')
                if ans=='c':print('right')
                elif ans=='C':print('right')
                else:print('False')

            #Question :- 12 
            if question_number==12:
                q1=print(" Which of the following is not a keyword in Python language? \nA.val \nB.raise \nC.try \nD.with ")
                ans=input('::')
                if ans=='a':print('right')
                elif ans=='A':print('right')
                else:print('False')

            #Question :- 13 
            if question_number==13:
                q1=print("Which of the following statements is correct for variable names in Python language? \nA.All variable names must begin with an underscore. \nB.Unlimited length \nC.The variable name length is a maximum of 2. \nD.All of the above ")
                ans=input('::')
                if ans=='b':print('right')
                elif ans=='B':print('right')
                else:print('False')

            #Question :- 14 
            if question_number==14:
                q1=print("Which of the following declarations is incorrect in python language? \nA.xyzp = 5,000,000 \nB.x y z p = 5000 6000 7000 8000 \nC.x,y,z,p = 5000, 6000, 7000, 8000 \nD.x_y_z_p = 5,000,000 ")
                ans=input('::')
                if ans=='b':print('right')
                elif ans=='B':print('right')
                else:print('False')

            #Question :- 15 
            if question_number==15:
                q1=print("Which of the following words cannot be a variable in python language? \nA._val \nB.val \nC.try \nD._try_ ")
                ans=input('::')
                if ans=='c':print('right')
                elif ans=='C':print('right')
                else:print('False')

            




choise=int(input('enter your choise::'))
if choise==1:print(q1())
elif choise==2:print(q2())
elif choise==3:print(q3())
else:print(q4())





































                
