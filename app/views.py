from app import app
from flask import render_template
from flask import url_for
from datetime import datetime
from app.models import User


@app.route('/')
def home():
	return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('home'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', title='Admin Dashboard')

@app.route('/chart')
def chart():
    return render_template('charts.html', title='Charts')

@app.errorhandler(Exception)
def page_not_found(e):
    ttl_error = str(e)
    ttl_error = ttl_error[:3]
    return render_template('404.html', error=ttl_error)

@app.route('/himel')
def fun_himel():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <center>
    <h1>হ্যালো লুবনা ম্যামের জামাই!!! :D</h1>

    <img src="https://i.imgur.com/FGGtKuJ.jpg">
    <p>সবাই আমিন না বলে যাবেন না।</p>
    </center>
    """