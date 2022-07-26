from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/category/animal/')
def animals():
    return render_template("category-animal.html")

@app.route('/category/potion/')
def potions():
    return render_template("category-potion.html")

@app.route('/category/material/')
def materials():
    return render_template("category-material.html")

@app.route('/cart/')
def cart():
    return render_template("cart.html")

@app.route('/category/animal/dragon/')
def purchase():
    return render_template("purchase.html")

if __name__ == '__main__':
    app.run()
