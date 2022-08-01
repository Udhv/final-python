
from flask import Flask, render_template, request
import free


app = Flask(__name__)



class Question:
    q_id=-1
    question=""
    option1=""
    option2=""
    option3=""
    correctOption=-1

    def __init__(self,q_id,question,option1,option2,option3,correctOption):
        self.q_id= q_id
        self.question=question
        self.option1=option1
        self.option2=option2
        self.option3=option3
        self.correctOption=correctOption

    def get_correct_option(self):
        
        if self.correctOption==1:
            return self.option1
        elif self.correctOption==2:
            return self.option2
        elif self.correctOption==3:
            return self.option3
        

q2=Question(2,"2.how many generations of computers we have ?","one","ten","five",3)
q3=Question(3,'Who is the father of Computer science ?','stephen hawking','Charles Babbage','abdul kalam',2)
q4=Question(4,'In a computer, most processing takes place in _______?','mouse','.keyboard','CPU',3)
question_list=[q2,q3,q4]

@app.route("/")
def quiz():
    return render_template("quiz.html",question_list=question_list)

@app.route("/submitquiz",methods=['POST','GET'])

def submit():
    correct_count=0
    for question in question_list:
        question_id=str(question.q_id)
        selected_option=request.form[question_id]
        correct_option=question.get_correct_option()
        if selected_option==correct_option:
            correct_count=correct_count+1
    correct_count=str(correct_count)
    return correct_count    

if __name__ == "__main__":
    app.run(debug=True)
