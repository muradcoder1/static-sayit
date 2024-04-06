from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/elements")
def elements():
    return render_template("elements.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/single_blog")
def single_blog():
    return render_template("single-blog.html")

@app.route("/about")
def about():
    return render_template("about-us.html")
if __name__=="__main__":
    app.run(debug=True)

