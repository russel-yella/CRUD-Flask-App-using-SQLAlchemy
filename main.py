from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

DATABASE_URL = 'sqlite:///books.db'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

db.init_app(app)

class Books(db.Model):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    title: Mapped[str] = mapped_column(String(100),unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(100),unique=True, nullable=False)
    rating: Mapped[float] = mapped_column(Float, default=0)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    all_books = db.session.execute(db.select(Books).order_by(Books.title)).scalars().all()
    return render_template('index.html',books=all_books)


@app.route("/add", methods=['POST','GET'])
def add():
    if request.method == 'POST':
        new_book = Books(
            title=request.form['title'],
            author=request.form['author'],
            rating=request.form['rating']
        )
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('add.html')

@app.route("/delete/<int:book_id>")
def delete(book_id):

    book_to_delete = db.get_or_404(
        Books,
        book_id
    )

    db.session.delete(book_to_delete)

    db.session.commit()

    return redirect(url_for("home"))

@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):

    book = db.get_or_404(
        Books,
        book_id
    )

    if request.method == "POST":

        book.title = request.form['title']
        book.author = request.form['author']

        book.rating = float(request.form["rating"])

        db.session.commit()

        return redirect(url_for("home"))

    return render_template(
        "edit.html",
        book=book
    )

if __name__ == "__main__":
    app.run(debug=True)

