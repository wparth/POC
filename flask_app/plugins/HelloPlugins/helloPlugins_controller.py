
import os
from flask import Blueprint, render_template


hello_app = Blueprint(
    name='HelloPlugins',
    import_name=__name__,
    template_folder='templates',
    static_folder='static'
)


@hello_app.route("/")
def hello():
    msg = os.environ['USER']
    return render_template('hello.html', msg=msg)