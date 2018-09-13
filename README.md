# BookStore
BookStore Application using MySQL and Python Tkinter

The purpose of this project is to implement an applicaton for buying books based on reviews and ratings given by other buyers. 

## Table of Contents

1. [Project overview](#project-overview)
2. [Requirements](#requirements)
3. [Architecture](#architecture)




## Project Overview

The idea behind this project is to implement an application that allows you to buy books and give them reviews and ratings so that
other customers will have an idea of how good that book is. The application's administrator can add new books, while users can buy 
those books, and then write reviews for them. In order to buy or review books, you must be registerd in the system. Every user 
registered in the system has a personal page where she can see the books she buyed and access all the information regarging those
books.
For GUI I used the Tkinter Python binding to Tk GUI Toolkit, while for the bookstore DB I used MySQL.


## Requirements
  Please see the requirments.txt file for a list of all necessary packages.
  Also the application need MySQL installed and Python2.7
  
  In order to start the application run: python WelcomePage.py



## Architecture

The MySQL database schema is described in the image below:
The database contains tables with information about the books, users, reviews, the books one user buyed and the reviewed books.

![structurabd](https://user-images.githubusercontent.com/12434214/45482256-30499800-b756-11e8-888f-dc9b661885f7.JPG)

Here I present an overview of how the application should look like:

![screenshot from 2018-01-09 23-38-09](https://user-images.githubusercontent.com/12434214/45482205-10b26f80-b756-11e8-8ec8-1e81c8d60f8a.png)

![screenshot from 2018-01-09 23-38-46](https://user-images.githubusercontent.com/12434214/45482220-1c059b00-b756-11e8-8ca8-cf2b2a3650b9.png)

![screenshot from 2018-01-09 23-42-27](https://user-images.githubusercontent.com/12434214/45482242-2758c680-b756-11e8-825f-5fcf53ff84e4.png)

![screenshot from 2018-01-09 23-42-18](https://user-images.githubusercontent.com/12434214/45482226-1f992200-b756-11e8-995c-aedd23a7c0be.png)

![screenshot from 2018-01-09 23-44-45](https://user-images.githubusercontent.com/12434214/45482235-23c53f80-b756-11e8-957e-ec302c434431.png)

![screenshot from 2018-01-09 23-45-16](https://user-images.githubusercontent.com/12434214/45482238-258f0300-b756-11e8-96ae-3fbc7649186a.png)



## Copyright and License


This application is provided under the [MIT-license](https://github.com/DanIulian/BookStore/blob/master/LICENSE).



