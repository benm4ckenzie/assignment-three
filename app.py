import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'book_review'
app.config["MONGO_URI"] = 'mongodb+srv://benm4ckenzie:Istanbul5x@myfirstcluster-beoum.mongodb.net/book_review?retryWrites=true&w=majority'


mongo = PyMongo(app)


@app.route('/')
@app.route('/get_library')
def get_library():
    return render_template('library.html', book=mongo.db.book.find())


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/add_book')
def add_book():
    return render_template('addbook.html',
    book=mongo.db.book.find())


@app.route('/submit_book', methods=['POST'])
def submit_book():
    book = mongo.db.book
    book.insert_one(request.form.to_dict())
    return redirect(url_for('get_library'))


@app.route('/update_book/<book_id>')
def update_book(book_id):
    the_book = mongo.db.book.find_one({"_id": ObjectId(book_id)})
    all_author = mongo.db.author.find()
    return render_template('editbook.html', book=the_book, author=all_author)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)