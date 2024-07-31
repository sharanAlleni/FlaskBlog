from flask import Flask,render_template
app= Flask(__name__)

posts=[
    {
        'author':"Sai",
        "title":"Blog Post 1",
        "content":"content 1",
        "date_posted":"date 1"
    },

    {
        'author':"Sharan",
        "title":"Blog Post 2",
        "content":"content 2",
        "date_posted":"date 2"
    }

]

@app.route("/home")
def home():
    return render_template("home.html",title='title_xyz',posts_dict=posts)

@app.route("/about")
def about():
    return render_template("about.html")


if __name__=="__main__":
    app.run(debug=True)
