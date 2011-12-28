import simplejson

from pygments import highlight
from pygments.lexers import JavascriptLexer
from pygments.formatters import HtmlFormatter

from flask import Module, render_template, request, redirect, url_for, session, jsonify, flash
from jsonifier import queries


# define this module
paste = Module(__name__)


@paste.route('/')
def list():
    
    # query for the most recent pastes
    pastes = queries.paste_list()
    
    if pastes:
        return render_template('paste/list.html', pastes=pastes)


@paste.route('/<id>')
def view(id):
    
    # query for a single paste
    paste_data = queries.paste_get(id)
    
    if paste_data:
        
        # pretty print the json
        pretty = simplejson.dumps(paste_data['json'], sort_keys=True, indent=4)
        pretty = highlight(pretty, JavascriptLexer(), HtmlFormatter())
        
        paste_data['json'] = pretty
        
        # if this is temporary then delete it
        if 'temp' in paste_data:
            queries.paste_remove(paste_data['_id'])
        
        return render_template('paste/view.html', paste=paste_data)
    
    flash('That paste does not exist.')
    return redirect(url_for('fluff.create'))


@paste.route('/<id>/raw')
def view_raw(id):
    
    # query for a single paste
    paste_data = queries.paste_get(id)
    
    if paste_data:
        return jsonify({ 'paste_%s' % str(paste_data['_id']): paste_data['json'] })
    
    return redirect(url_for('fluff.create'))