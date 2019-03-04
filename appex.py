import json
import MySQLdb
import MySQLdb.cursors
from functools import wraps
import flask
app = flask.Flask(__name__, static_folder='static', static_url_path='')


def support_jsonp(f):
    """Wraps JSONified output for JSONP"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        callback = flask.request.args.get('callback', False)
        if callback:
            content = str(callback) + '(' + str(f(*args,**kwargs)) + ')'
            return flask.current_app.response_class(content, mimetype='application/javascript')
        else:
            return f(*args, **kwargs)
    return decorated_function



@app.route('/')
@app.route('/index')
def index():
    return '''
<html>
    <head>
        <title>My New Skillz</title>
    </head>
    <body>
        <h1>Woohoo!</h1>
        This is the landing page...
    </body>
</html>'''


@app.route('/movie/<card_name>')
def movies(card_name):
    conn = MySQLdb.connect(host='localhost',
                           user='root',
                           passwd='password',
                           db='magic2',
                           cursorclass = MySQLdb.cursors.DictCursor)
    c = conn.cursor()
    c.execute('SELECT * FROM Card_name WHERE name=%s;', [card_name])
    if c.rowcount > 0:
        rs = c.fetchall()
        return flask.render_template('yesfound.html', title=card_name, data=[r for r in rs])
    else:
        return flask.render_template('notfound.html', title=card_name)



@app.route('/json/movie/<card_name>')
@support_jsonp
def json_movies(card_name):
    conn = MySQLdb.connect(host='localhost',
                           user='root',
                           passwd='password',
                           db='magic2',
                           cursorclass = MySQLdb.cursors.DictCursor)
    c = conn.cursor()
    c.execute('SELECT * FROM Card_name WHERE name LIKE %s;', [card_name])
    result_list = []
    if c.rowcount > 0:
        rs = c.fetchall()
        result_list = [r for r in rs]
    s = json.dumps({'Card_name': result_list})
    print(s)
    return s

@app.route('/json/card/<card>')
@support_jsonp
def card_finder(card):
    conn = MySQLdb.connect(host='localhost',
                           user='root',
                           passwd='password',
                           db='magic2',
                           cursorclass = MySQLdb.cursors.DictCursor)
    c = conn.cursor()
    c.execute('SELECT * FROM Card WHERE name LIKE %s;', [card])
    result_list = []
    if c.rowcount > 0:
        rs = c.fetchall()
        result_list = [r for r in rs]
    s = json.dumps({'Card_name': result_list})
    print(s)
    return s


# Add a route for star names that allows
# URLs that contain a star's last name and lists
# all stars with that last name.





# Add a route to retrieve a JSON version
# of the star names by last name as described above.








if __name__ == '__main__':
    app.run()