from flask import Flask, render_template, redirect, make_response
from ..logic.shorten import Shortener
import os 

app = Flask(__name__, template_folder='../templates')
app.config.from_mapping(
    DATABASE=os.path.join(app.instance_path, 'shorten.sqlite')
)

# Should return a home page where the users can input their URL or shortened URL
# HTTP Method -> GET
@app.route('/')
def hello():
    return render_template('home.html')

# POST to logic that shortens the given URL
@app.route('/shorten', methods=['POST'])
def shorten(url):
    pass

# POST to logic that returns a customized shortened URL
@app.route('/shorten/custom', methods=['POST'])

# POST to logic that un-shrotens the given short URL
@app.route('/unshorten')
def unshorten(short_url, methods=['POST']):
    pass

# Test that the shortened URL route works
@app.route('/test_url')
def test_url():
    pass

# POST to loging and verify login credentials
@app.route('/login', methods=['POST'])
def login():
    pass

# POST to register and sign up as a new user
@app.route('/register', methods=['POST'])
def register():
    pass

# Returns a page that displays the user's name and dashboard of shortened URLs
@app.route('/member/<member_id>')
def return_member_landing(member_id):
    pass

# Returns a 404 error if the route is not recognized
@app.errorhandler(404)
def not_found():
    return make_response(render_template('404.html'), 404)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')