import simplejson

from flask import Module, render_template, request, redirect, url_for, session, flash
from jsonifier import queries


# define this module
fluff = Module(__name__)


@fluff.route('/', methods=['GET', 'POST'])
def create():
    
    if request.method == 'POST' and 'json' in request.form:
        
        try:
            # turn the pasted json into python
            the_json = request.form.get('json')
            the_json = simplejson.loads(the_json)
            
            # handle a temporary paste if necessary
            temporary = False
            if 'temporary' in request.form:
                temporary = bool(request.form.get('temporary'))
            
            # save it
            paste_id = queries.paste_create(the_json, temporary)
            
            # redirect to it
            if paste_id:
                return redirect(url_for('paste.view', id=paste_id))
            
        except:
            flash('That was not valid JSON. For a JSON reference, please refer to <a href="http://json.org/" target="_blank">json.org</a>.')
            return redirect(url_for('fluff.create'))
        
    return render_template('fluff/create.html')


@fluff.route('/developers')
def developers():
    return render_template('fluff/developers.html')