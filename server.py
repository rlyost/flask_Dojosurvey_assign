from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")

# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/survey', methods=['POST'])
def survey_info():
  print "Got it"

  name = request.form['name']
  location = request.form['location']
  language = request.form['language']
  comment = request.form['comment']

  return render_template("process.html", name2=name, location2=location, language2=language, comment2=comment)

app.run(debug=True) # run our server
