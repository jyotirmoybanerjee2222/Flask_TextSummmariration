import requests
from flask import Flask,render_template,url_for,request



app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def Index():
    return render_template("index.html")

@app.route("/Summarize",methods=["GET","POST"])
def Summarize():
        if request.method == "POST":
            API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
            headers = {"Authorization": "Bearer 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"}

            data = request.form["data"]

            minL = 100
            maxL = 400
            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.json()

            output = query({
                    "inputs":data,
                    "parameters":{"min_length":minL,"max_length":maxL},
                })
            
            return render_template("index.html",result=output)

        else:
            return render_template("index.html")

if __name__ == "__main__":
    app.debug=True
    app.run()