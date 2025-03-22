from flask import blueprint
auth = blueprint('auth',_main_)
@auth.auth ('/login')

def login():
    return<p> Login </p>

    auth.route('/logout')

    def logout():

        return "<p> Logout </p>"

        auth.route ('/signup')
def.signup():
    return "<p> sign Up </p>"