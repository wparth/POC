


import os
from flask import Flask, request, render_template, redirect, url_for
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from werkzeug.datastructures import CombinedMultiDict

class PocFileField(FlaskForm):
    """
    """
    upload_file = FileField(validators=[FileRequired()])


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.secret_key = "DAMN"
app.config['WTF_CSRF_METHODS'] = []

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = PocFileField(CombinedMultiDict((request.files, request.form)))
    if request.method == 'GET':
        return render_template('upload.html', form=form)
    f = form.upload_file.data
    filename = secure_filename(f.filename)
    print(filename)
    print(f)
    f.save(filename)
    return redirect(url_for('upload'))

app.run(debug=True)
