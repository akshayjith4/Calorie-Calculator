from flask.views import MethodView
from flask import Flask, render_template, request

app = Flask(__name__)

class Home(MethodView):
    def dispatch_request(self):
        return render_template('home.html')

class ResultPage(MethodView):
    def post(self):
        # Retrieve form data
        age = int(request.form.get('age'))
        height = int(request.form.get('height'))
        weight = int(request.form.get('weight'))
        gender = request.form.get('gender')  # Expect 'male' or 'female'
        activity_level = float(request.form.get('activity_level'))

        # Calculate BMR
        if gender == 'male':
            bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
        elif gender == 'female':
            bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
        else:
            return "Invalid gender"

        # Calculate TDEE
        tdee = bmr * activity_level

        return render_template('result.html', total_calories=tdee)


class Foods(MethodView):
    def dispatch_request(self):
        return render_template('foods.html')

class Exercises(MethodView):
    def dispatch_request(self):
        return render_template('exercises.html')



# Adding URL rules with view functions
app.add_url_rule('/', view_func=Home.as_view('home'))
app.add_url_rule('/result', view_func=ResultPage.as_view('result'), methods=['POST'])
app.add_url_rule('/foods', view_func=Foods.as_view('foods'))
app.add_url_rule('/exercises', view_func=Exercises.as_view('exercises'))

if __name__ == '__main__':
    app.run(debug=True)
