from flask import jsonify, render_template
from foodapp import app

"""This defined routes for UI pages"""

"""==================All user================"""

@app.route('/', methods=['GET'])
def index():
    """Render user login page"""
    return render_template('index.html')


@app.route('/user/login', methods=['GET'])
def admin_login():
    """Render user register page"""
    return render_template('register.html')

"""===============Admin pages================"""

@app.route('/admin/orders', methods=['GET'])
def admin_orders_page():
    """Render admin orders page."""
    return render_template('admin.html')

@app.route('/admin/menus/create', methods=['GET'])
def admin_add_menu_page():
    """Render admin add menu page."""
    return render_template('addItem.html')

@app.route('/admin/menus/createdlist', methods=['GET'])
def admin_added_menu_page():
    """Render admin added menu page."""
    return render_template('addedlist.html')

"""=================User pages============="""

@app.route('/user/orders/menu', methods=['GET'])
def user_get_menu_page():
    """Render user get menu."""
    return render_template('home.html')

@app.route('/user/orders/history', methods=['GET'])
def user_get_order_history_page():
    """Render user order history page."""
    return render_template('history.html')