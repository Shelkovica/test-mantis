

def test_login(app):
    app.session.login("administrator", "root")
    print("dgdfgdf")
    assert app.session.is_logged_in_as("administrator")