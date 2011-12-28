import pymongo, bson


db = pymongo.Connection()['jsonifier']


def paste_create(json, temporary):
    if temporary == True:
        return db.pastes.insert({ 'json': json, 'temp': 1 })
    return db.pastes.insert({ 'json': json })


def paste_get(id):
    try:
        id = bson.objectid.ObjectId(id)
        return db.pastes.find_one({ '_id': id })
    except:
        return None


def paste_list():
    return list(db.pastes.find(fields={'json': 0}, limit=15, sort=[('_id', pymongo.DESCENDING)]))


def paste_remove(id):
    try:
        id = bson.objectid.ObjectId(id)
        return db.pastes.remove({ '_id': id })
    except:
        return False