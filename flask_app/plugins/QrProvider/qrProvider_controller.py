
import urllib
import pyotp
from flask import Blueprint, render_template, Markup

qrprovider_app = Blueprint(
    name='QrProvider',
    import_name=__name__,
    template_folder='templates',
    static_folder='static'
)


@qrprovider_app.route('/qrProvider')
def qr_provider():
    message = pyotp.random_base32(96)
    dimension = 500
    base = "https://chart.googleapis.com/chart?"
    dimension = "chs=" + str(dimension) + "x" + str(dimension)
    qr = "cht=qr&chl=" + urllib.quote_plus(message)
    error = "chld=" + 'M'
    full_url = base + dimension + "&" + qr + "&" + error
    qr_code = Markup("<img src=" + full_url + " height=" + str(dimension) + " width=" + str(dimension) + ">")
    return render_template('qrcode.html', qrCode=qr_code)
