import simplejson

from flask import Module, request, jsonify, abort
from jsonifier import queries


# define this module
api = Module(__name__)


@api.route('/create', methods=['POST'])
def create():
    if request.method == 'POST' and request.form.get('json'):
        
        try:
            # turn the pasted json into python
            the_json = request.form.get('json')
            the_json = simplejson.loads(the_json)
            
            # save it
            paste_id = queries.paste_create(the_json)
            
            # return the paste id
            if paste_id:
                return jsonify({ 'id': str(paste_id) })
            
        except:
            raise abort(501)
    
    # nothing to paste
    raise abort(403)