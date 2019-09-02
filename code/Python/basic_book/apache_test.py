import bottle
app = bottle.default_app()


@bottle.route('/')
def home():
    return 'wsgi test'
