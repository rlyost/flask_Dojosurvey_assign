from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")

# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/survey', methods=['POST'])
def survey_info():
  name = request.form['name']
  location = request.form['location']
  language = request.form['language']
  comment = request.form['comment']
  if len(name) < 1:
    # display validation errors
    flash("Name can not be empty!")
    return redirect('/')
  if len(comment) < 1:
    flash("Comment can not be empty!")
    return redirect('/')
  elif len(comment) > 120:
    flash("Comment is too long. No more then 120 characters.")
    return redirect('/')

  return render_template("process.html", name2=name, location2=location, language2=language, comment2=comment)

app.run(debug=True) # run our server
