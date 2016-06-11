from flask import Flask

app = Flask(__name__)

@app.route("/<int:number>",methods=["GET","POST"])
def index(number):
    return funct(number)

def funct(number):
    return "This is the number, {}".format(number)

if __name__ == '__main__':
    app.run()
