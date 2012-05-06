import bottle
from bottle import request, route
import os
import igo.tagger


tagger = igo.tagger.Tagger('ipadic')


@route('/parse')
def parse():
    for m in tagger.parse(request.query.q):
        yield "%s %s %s\r\n" % (m.surface, m.feature, m.start)


@route('/')
def index():
    return "Hello World"

if __name__ == '__main__':
    bottle.run(server='gevent',
               host='0.0.0.0', port=os.environ.get('PORT', 5000))
