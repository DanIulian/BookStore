--Create the BookStore DataBase
DROP DATABASE IF EXISTS bookStoreDB;
CREATE DATABASE bookStoreDB;
USE bookStoreDB;

DROP TABLE IF EXISTS Books;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Reviews;
DROP TABLE IF EXISTS BuyedBooks;
DROP TABLE IF EXISTS ReviewedBooks;


CREATE TABLE Books(
	bookId  INT NOT NULL AUTO_INCREMENT,
	title VARCHAR(30) NOT NULL,
	genre VARCHAR(30),
	author VARCHAR(30),
	published_year VARCHAR(20),
	stock INT UNSIGNED,
	price DOUBLE,
	PRIMARY KEY (bookId),
	UNIQUE (title)
);


CREATE TABLE Users(
	userId INT NOT NULL AUTO_INCREMENT,
	userName VARCHAR(30),
	firstName VARCHAR(30),
	familyName VARCHAR(30),
	email VARCHAR(30),
	bankingCardNumber VARCHAR(19) NOT NULL,
	password VARCHAR(10) NOT NULL,
	PRIMARY KEY (userID),
	UNIQUE (userName)
);


CREATE TABLE Reviews(
	reviewId INT NOT NULL AUTO_INCREMENT,
	reviewText VARCHAR(250),
	PRIMARY KEY (reviewId)
);


CREATE TABLE BuyedBooks(
	userId INT NOT NULL,
	bookId INT NOT NULL,
	quantity INT NOT NULL,
	PRIMARY KEY (userId, bookId),

	FOREIGN KEY (userId)
		REFERENCES Users(userId)
		ON DELETE CASCADE,

	FOREIGN KEY (bookId)
		REFERENCES Books(bookId)
		ON DELETE CASCADE
);

CREATE TABLE ReviewedBooks(
	reviewId INT NOT NULL,
	bookId INT NOT NULL,
	userId INT NOT NULL,
	score DOUBLE NOT NULL,
	PRIMARY KEY (reviewId),


	FOREIGN KEY (reviewId)
		REFERENCES Reviews(reviewId)
		ON DELETE CASCADE,

	FOREIGN KEY (bookId)
		REFERENCES Books(bookId)
		ON DELETE CASCADE,

	FOREIGN KEY (userId)
		REFERENCES Users(userId)
		ON DELETE CASCADE

);

-- dummy examples
INSERT INTO Books (title, genre, author, published_year, stock, price) VALUES ('Harry Potter', 'Fiction', 'J. K. Rowling' , '2001', 5, 11.95);
INSERT INTO Books (title, genre, author, published_year, stock, price) VALUES ('Great Gatsby', 'Romance', 'F Scott Fitzgerald', '1920', 3, 10.95);
INSERT INTO Books (title, genre, author, published_year, stock, price) VALUES ('100km to Death', 'Science Fiction', 'Issac Asimov', '2013', 5, 14.95);
INSERT INTO Books (title, genre, author, published_year, stock, price) VALUES ('Love in time of cholera', 'Drama', 'G. Garcia Marquez', '1960', 5, 13.95);
INSERT INTO Books (title, genre, author, published_year, stock, price) VALUES ('Dark Matters', 'Children Fiction', 'P. Pullman', '2015', 5, 12.95);