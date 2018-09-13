-- MySQL stored procedures for database manipulation
DELIMITER //

DROP PROCEDURE IF EXISTS add_new_user//	

CREATE PROCEDURE add_new_user(
	IN uname VARCHAR(30),
	IN sname VARCHAR(30),
	IN bname VARCHAR(30),
	IN addr VARCHAR(50),
	IN bkg_card_nr VARCHAR(19),
	IN pass VARCHAR(10) )

BEGIN
	INSERT INTO Users(userName, firstName, familyName, email, bankingCardNumber, password) 
		VALUES (uname, sname, bname, addr, bkg_card_nr, pass) ;
END//

DELIMITER ;

DELIMITER $$

DROP PROCEDURE IF EXISTS log_in$$

CREATE PROCEDURE log_in(
	IN uName VARCHAR(30),
	OUT fName VARCHAR(30),
	OUT sName VARCHAR(30),
	OUT emal VARCHAR(30),
	OUT pass VARCHAR(30)
	)

BEGIN

	SELECT firstName, familyName, email, password 
		INTO fName, sName, emal, pass 
		FROM Users 
		WHERE userName = uName;
END$$



DROP PROCEDURE IF EXISTS getAllBooks$$

CREATE PROCEDURE getAllBooks()

BEGIN

	SELECT title, author, genre, price, stock  FROM Books;
END$$



DROP PROCEDURE IF EXISTS isBook$$

CREATE PROCEDURE isBook(IN bName VARCHAR(30), OUT bExist INT)

BEGIN
	SELECT count(*) INTO bExist 
		FROM Books
		WHERE title = bName;

END$$



DROP PROCEDURE IF EXISTS insertBook$$

CREATE PROCEDURE insertBook(
	IN bName VARCHAR(30),
	IN bGenre VARCHAR(30),
	IN bAuthor VARCHAR(30),
	IN bYear VARCHAR(20),
	IN bSock INT,
	IN bPrice DOUBLE
)

BEGIN
	INSERT INTO Books(title, genre, author, published_year, stock, price)
		VALUES (bName, bGenre, bAuthor, bYear, bSock, bPrice);
END$$



DROP FUNCTION IF EXISTS bookScore$$

CREATE FUNCTION bookScore(idBook INT) 
	RETURNS DOUBLE
BEGIN
	DECLARE sumScore INT;
	DECLARE nrReviews INT;
	DECLARE bookGrade DOUBLE DEFAULT 0.0;

	SELECT COUNT(*) INTO nrReviews 
		FROM ReviewedBooks
		WHERE bookId = idBook;

	SELECT IFNULL(SUM(score), 0) INTO sumScore
		FROM ReviewedBooks
		WHERE bookId = idBook;


	IF nrReviews = 0 
	THEN
		SET bookGrade = 0;
	ELSE
		SET bookGrade = sumScore / nrReviews;

	END IF;

	RETURN bookGrade;

END$$



DROP PROCEDURE IF EXISTS getBooksUser$$

CREATE PROCEDURE getBooksUser()

BEGIN

	SELECT title, author, genre,  price, stock, bookScore(bookId) FROM Books;
END$$




DROP PROCEDURE IF EXISTS getUsersBooks$$

CREATE PROCEDURE getUsersBooks(IN uName VARCHAR(30))

BEGIN
	DECLARE idUser INT;
	SELECT userId INTO idUser FROM Users WHERE userName=uName;

	SELECT b.title, b.author, b.genre, bb.quantity, bookScore(b.bookId)
		FROM Books b, BuyedBooks bb
		WHERE b.bookId = bb.bookId
			AND bb.userId = idUser ;
END$$


DROP PROCEDURE IF EXISTS buyBook$$

CREATE PROCEDURE buyBook(
	IN bookName VARCHAR(30),
	IN userNm VARCHAR(30)
)

BEGIN

	DECLARE nrBooks INT;
	DECLARE idBook INT;
	DECLARE idUser INT;

	SELECT userId INTO idUser FROM Users WHERE userName = userNm;
	SELECT bookId INTO idBook FROM Books WHERE title = bookName;


	SELECT IFNULL(count(*), 0) INTO nrBooks 
		FROM BuyedBooks 
		WHERE userId = idUser
			AND bookId = idBook;
		
	IF nrBooks = 0
	THEN
		INSERT INTO BuyedBooks(userId, bookId, quantity)
			VALUES (idUser, idBook, 1);
	ELSE
		UPDATE BuyedBooks SET quantity = quantity + 1
			WHERE userId = idUser
				AND bookId = idBook;
	END IF;

END$$



DROP PROCEDURE IF EXISTS getBookInfo$$

CREATE PROCEDURE getBookInfo(IN bookName VARCHAR(30))

BEGIN
	SELECT title, author, genre, published_year, price, bookScore(bookId)
		FROM Books 
		WHERE title = bookName;
END$$



DROP PROCEDURE IF EXISTS getBookReviews$$

CREATE PROCEDURE getBookReviews(IN bookName VARCHAR(30))
BEGIN
	DECLARE idBook INT;

	SELECT bookId INTO idBook FROM Books WHERE title=bookName;

	SELECT u.userName, bb.score 
		FROM ReviewedBooks bb, Users u
		WHERE bb.bookId = idBook
			AND bb.userId = u.userId;

END$$



DROP PROCEDURE IF EXISTS insertReview$$

CREATE PROCEDURE insertReview(
	IN uName VARCHAR(30),
	IN bookName VARCHAR(30),
	IN uScore DOUBLE,
	IN uReview VARCHAR(100) )

BEGIN
	DECLARE idBook INT;
	DECLARE idUser INT;
	DECLARE idReview INT;

	SELECT bookId INTO idBook FROM Books WHERE title=bookName;
	SELECT userId INTO idUser FROM Users WHERE userName=uName;

	INSERT INTO Reviews(reviewText)
		VALUES (uReview);

	SELECT reviewId INTO idReview FROM Reviews WHERE  reviewText=uReview;


	INSERT INTO ReviewedBooks(reviewId, bookId, userId, score)
		VALUES(idReview, idBook, idUser, uScore);


END$$



DROP TRIGGER IF EXISTS updateStock1$$


CREATE TRIGGER updateStock1
	AFTER UPDATE ON BuyedBooks FOR EACH ROW
BEGIN
	
	UPDATE Books SET stock = stock - 1
		WHERE bookId = NEW.bookId;

END$$


DROP TRIGGER IF EXISTS updateStock2$$


CREATE TRIGGER updateStock2
	AFTER INSERT ON BuyedBooks FOR EACH ROW
BEGIN
	
	UPDATE Books SET stock = stock - 1
		WHERE bookId = NEW.bookId;

END$$



DELIMITER ;

