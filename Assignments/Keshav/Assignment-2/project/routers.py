from flask import render_template, redirect, flash, request
from flask_login import login_user, logout_user, current_user
from project.form_ import SignupForm, SignInForm
from project import db, bcrypt, apps
from project.models import User


@apps.route('/')
def root():
    print("jjj")
    form = SignInForm()
    if current_user.is_authenticated:
        return redirect("/dashboard")
    return render_template("signin.html", form=form)


@apps.route("/dashboard")
def blogs():
    if current_user.is_authenticated:
        return render_template("dashboard.html", user_detail=current_user)


@apps.route("/signup/", methods=["GET", "POST"])
def signUp():
    if current_user.is_authenticated:
        return redirect("/dashboard")
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode("utf-8")
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been created, you can login now", "success")
        return redirect("/")
    return render_template("signup.html", form=form)


@apps.route("/signin/", methods=["GET", "POST"])
def signIn():
    if current_user.is_authenticated:
        return redirect("/dashboard")
    form = SignInForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=True)
                flash(f"You have successfully logged in!!", "success")
                return redirect("/dashboard")
            else:
                flash(
                    f"Please check your email and password", "danger")
                return redirect("/")
    return render_template("signin.html", form=form)


@apps.route("/logout")
def logout():
    logout_user()
    flash(f"You have successfully logged out!!", "success")
    return redirect("/")
