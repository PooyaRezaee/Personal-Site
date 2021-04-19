from . import admin

@admin.route('/')
def Dashboard():
    return "this is panel admin"