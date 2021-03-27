from flask import Flask, render_template,request
import pickle;

app = Flask(__name__)

file=open('predictor.pkl','rb');
classifier=pickle.load(file);
file.close()

@app.route("/",methods=["GET","POST"])
def hello():
    print("request.method",request.method)
    if request.method=="POST":
        #print(request.form)
        mydict=request.form
        age=int(mydict['age']);
        sex=int(mydict['sex']);
        cp=int(mydict['cp']);
        trestbps=int(mydict['trestbps']);
        chol=int(mydict['chol']);
        fbs=int(mydict['fbs']);
        restecg=int(mydict['restecg']);
        thalach=int(mydict['thalach']);
        exang=int(mydict['exang']);
        oldpeak=float(mydict['oldpeak']);
        slope=int(mydict['slope']);
        ca=int(mydict['ca']);
        thal=int(mydict['thal']);
        user_input=[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        prob=classifier.predict_proba([user_input])[0][1]
        print("prob=",prob)
        return render_template('show1.html',p=prob*100)
    return render_template('index1.html')
    
@app.route("/contact",methods=["GET","POST"])
def contact():
    if request.method=="GET":
        return render_template('contact.html')
    return render_template('index1.html')



@app.route("/about",methods=["GET","POST"])
def about():
    if request.method=="GET":
        return render_template('about.html')
    
    
    return render_template('index1.html')


@app.route("/home",methods=["GET","POST"])
def home():
    return render_template('index1.html')


if "__name__"=="__main__":
    pass
app.run(debug=True)