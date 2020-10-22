from flask import Flask, render_template, request, redirect, url_for, session, flash
from flaskstuff.form import RegistrationForm, LoginForm
from flaskstuff import app, db, bcrypt
from flaskstuff.model import users

app.secret_key = 'hello'

@app.route('/view')
def view():
    return render_template('view.html', values=users.query.all())

@app.route('/home', methods=['POST','GET'])
def home(): 
    render_template('layout.html')
    # the action in the X button moves to the same place that you are currently in and apparently it brings what you see with it too.
    return render_template('home.html') 

@app.route('/about')
def about():
    render_template('layout.html')
    return 'about'
    #if request.method == "POST":
    #    return redirect(url_for('home'))
    #if 'user' in session:
    #    user = session['user']
    #    return render_template('about.html', title='About', user=user)
    #else:
    #    return render_template('about.html', title='About')

@app.route('/login', methods=["POST","GET"])
def login(): 
    render_template('layout.html')
    form = LoginForm()
    if form.validate_on_submit():
        user = users.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['logged'] = True
            session['user'] = form.username.data
            render_template('layout.html', user=form.username.data, form=form)
            render_template('home.html')
            flash('You have been logged in!','good')
            return redirect(url_for('home'))
        else: 
            flash('Incorrect username or password','bad')
    return render_template('login.html',form=form)

@app.route('/register', methods=["POST","GET"])
def register(): 
    render_template('layout.html')
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        usr = users(form.username.data, form.email.data, hashed_password)
        db.session.add(usr)
        db.session.commit()
        session['logged'] = True
        session['user'] = form.username.data
        render_template('home.html')
        flash(f'Account created for {form.username.data}!','good')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
def logout():
    render_template('layout.html')
    session.pop('logged',None)
    session.pop('user',None)
    render_template('layout.html')
    flash('You have successfully logged out','good')
    return redirect(url_for('home'))


# functions can have multiple routs
# debugger allows the page to be changed automatically after you save file instead of having to run the code again
# html in main file goes insie quotes "<h1>Hello World!</h1>"
# the variable that is passed in here will be able to be accessed in html code.. you use the post paremeter in the html code