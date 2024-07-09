
from flask import *
app=Flask("__name__")

@app.route('/login',methods=['post'])
def runn():
    tp=request.form['type']
    name=request.form["n1"]
    Lastname=request.form["n2"]
    Username=request.form["n3"]
    Email=request.form["n4"]
    password=request.form["n5"]
    conpass=request.form["n6"]
    address=request.form["n7"]
    city=request.form["n8"]
    state=request.form["n9"]
    pincode=request.form["n10"]
    if password==conpass:
        
        return f"Type of user:{tp}->Name:{name}{Lastname}->Username:{Username}->Email:{Email}->address:{address}->city:{city}->state:{state}->pincode:{pincode}"
    else:
        return "invalid"


if __name__=="__main__":
    app.run(debug=True)