from flask import Flask, make_response, render_template
app = Flask(__name__)

@app.route('/')
def make_session():
    resp = make_response(render_template('new.html'))
    resp.set_cookie("INSERTED", "INSERTED")
    return resp

app.run(debug=True)
