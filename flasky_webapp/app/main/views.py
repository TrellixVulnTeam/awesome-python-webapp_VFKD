from datetime import datetime
from flask import render_template, session, redirect, url_for, abort

from . import main
from .forms import NameForm
from ..models import User


@main.route('/', methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        return redirect(url_for('.index'))
    
    return render_template('main/index.html',
                           form=form,
                           name=session.get('name'),
                           known=session.get('konwn', False),
                           current_time=datetime.utcnow())

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('user.html',user=user)