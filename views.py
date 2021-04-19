from app import app

@app.route('/')
def Home():
    return "this is home page"