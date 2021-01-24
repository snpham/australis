from flask import render_template, request, Blueprint
from astro.main.functions import *
import sys
sys.path.insert(0, '..')
from astralib.math_helpers.time_systems import *


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')


@main.route("/about")
def about():
    return render_template('about.html', title='About')


@main.route("/transforms", methods=["GET", "POST"])
def transforms():
    errors = []
    result = None
    if request.method == "POST":
        number1 = None
        number2 = None
        try:
            number1 = float(request.form["number1"])
        except:
            errors.append(request.form["number1"])
        try:
            number2 = float(request.form["number2"])
        except:
            errors.append(request.form["number2"])
        if number1 is not None and number2 is not None:
            if request.form["action"] == "Add":
                result = addition(number1, number2)
            if request.form["action"] == "Multiply":
                result = multiplication(number1, number2)
    return render_template('transforms.html', errors=errors, result=result)
    

@main.route("/time", methods=["GET", "POST"])
def time():
    errors = []
    result = None
    if request.method == "POST":
        if request.form["action"] == "CAL to Mod Julian":
            year = int(request.form["year"])
            month = int(request.form["month"])
            day = int(request.form["day"])
            hour = int(request.form["hour"])
            minute = int(request.form["minute"])
            second = float(request.form["second"])
            caldate = (year, month, day, hour, minute, second)
            jd, mjd = get_JD(year, month, day, hour, minute, second)
            result = jd
            return render_template('time.html', errors=errors, result=result, inputdate=caldate, calc='CAL2JD')
        elif request.form["action"] == "Julian to CAL":
            jd = float(request.form["JD"])
            date = cal_from_jd(jd)
            result = date
            return render_template('time.html', errors=errors, result=result, inputdate=jd, calc='JD2CAL')
    return render_template('time.html')

# @main.route("/resume")
# def resume():
#     return render_template('resume.html', title='My Resume')