from flask import Flask

app = Flask(_name_)

@app.route("/")
def home():
    return "<h1>Welcome to Our Cloud Project!</h1>"

if _name_ == "_main_":
    app.run(debug=True)
