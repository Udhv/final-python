
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/sub",methods=['POST','GET'])
def hoise():
    cho="hrllp"
    hoise=request.form["ch"]
    ho=int(hoise)
    if ho==1:
        return cho
    return hoise

if __name__ == "__main__":
    app.run(debug=True)
