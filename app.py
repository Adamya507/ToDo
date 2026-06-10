from flask import Flask,render_template,redirect,url_for,request
from datetime import date
import os
app=Flask(__name__)
datetoday=date.today().strftime("%d-%B-%Y")
if "task.txt" not in os.listdir("."):
    with open("task.txt","w") as f: #using with we do this together like opening the file and write
        f.write("")
        
def gettasklist():
    with open("task.txt","r") as f:
        tasklist=f.readlines()
        f.close()    
    return tasklist

def createnewtasklist():
    os.remove("task.txt")
    with open("task.txt","w") as f:
        f.write("")
        f.close()
        
def updatetasklist(tasklist):
    os.remove("task.txt")
    with open("task.txt","w") as f:
        f.writelines(tasklist)
               
            
@app.route("/")
def main():
    return render_template("index.html",datetoday=datetoday,tasklist=gettasklist(),l=len(gettasklist()))

@app.route("/addtask",methods=['POST','GET'])
def addtask():
    if request.method=='POST':
        task=request.form["newtask"]
        with open("task.txt","a") as f:
            f.writelines(task+"\n")
            f.close()
            return render_template("index.html",datetoday=datetoday,tasklist=gettasklist(),l=len(gettasklist())) 
  
@app.route("/deltask",methods=['GET'])
def deltask():
    id=int(request.args["deltaskid"])
    tasklist=gettasklist()
    if id<0 or id>len(tasklist):
        return render_template("index.html",datetoday=datetoday,tasklist=gettasklist(),l=len(gettasklist()),mess="invalid index....")  
    else:
        tasklist.pop(id)
    updatetasklist(tasklist)
    return render_template("index.html",datetoday=datetoday,tasklist=gettasklist(),l=len(gettasklist()),mess="task deleted sucessfully....")             

@app.route("/clear")
def clear():
    createnewtasklist()
    return render_template("index.html",datetoday=datetoday,tasklist=gettasklist(),l=len(gettasklist()))


if __name__=="__main__":
    app.run(debug=True)