import importlib
import pkgutil
import re

from flask import Blueprint


def register_blueprints(app, package_name, package_path):
    """Register all Blueprint instances on the specified Flask application
    found in all modules for the specified package.

    :param app: the Flask application
    :param package_name: the package name
    :param package_path: the package path
    """
    rv = []
    for _, name, _ in pkgutil.iter_modules(package_path):
        if name.startswith('views_'):
            m = importlib.import_module('%s.%s' % (package_name, name))
            for item in dir(m):
                item = getattr(m, item)
                if isinstance(item, Blueprint):
                    app.register_blueprint(item)
                rv.append(item)
    return rv


def _make_choices(qs, placeholder=None):
    """Helper method for generating choices for :class:`SelectField`
    instances.
    """
    if placeholder:
        return [['', placeholder]] + [[unicode(i[0]), i[1]] for i in list(qs)]
    else:
        return [['', '']] + [[unicode(i[0]), i[1]] for i in list(qs)]


def stash_file(fileobj, user, event=None):
    from apollo.services import user_uploads
    upload = user_uploads.create(user=user, event=event)
    upload.data.put(fileobj)
    upload.save()
    upload.reload()

    return upload


def is_objectid(str):
    return bool(re.match('^[0-9a-fA-F]{24}$', str))


def compute_location_path(location):
    '''Given a :class:`apollo.locations.models.Location` instance,
    generates a dictionary with location type names as keys and
    location names as values. Due to lack of joins in MongoDB,
    this dictionary is useful for queries that retrieve submission
    and participant information within a location hierarchy.'''
    from apollo.locations.models import Location

    # we don't really expect the latter case, but for the former,
    # it's possible to have a participant with no location set
    if not location or not isinstance(location, Location):
        return None

    return {
        ancestor.location_type: ancestor.name
        for ancestor in location.ancestors_ref
    }
