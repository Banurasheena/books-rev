from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError




class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")
    


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField("Login")


class SearchForm(FlaskForm):
    isbn = StringField('isbn_number', validators=[DataRequired()])
    title = StringField('title', validators=[DataRequired()])
    author = StringField('author', validators=[DataRequired()])
    submit = SubmitField('Search')
    


class Book:
    def __init__(self, b_id, g_id, isbn, isbn13, authors, year, title, rating, ratings_count, url, small_url):
        self.id = b_id
        self.g_id = g_id
        self.isbn = isbn
        self.isbn13 = int(float(isbn13))
        self.authors = authors
        self.year = year
        self.title = title
        self.rating = rating
        self.ratings_count = ratings_count
        self.url = url
        self.small_url = small_url

    def trim_authors(self):
        authors_len = len(self.authors)
        if authors_len > 2:
            del self.authors[2:]
        self.authors = ", ".join(self.authors)
        if authors_len > 2:
            self.authors = self.authors + " and more"


class Review:

    def __init__(self, r_id, b_id, u_id, date, time, review, rating):
        self.id = r_id
        self.b_id = b_id
        self.u_id = u_id
        self.date = date
        self.time = time
        self.review = review
        self.rating = rating

