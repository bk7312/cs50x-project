# The Login2Win Challenge
#### Video Demo:  https://www.youtube.com/watch?v=0hEYvDsl7ZU
#### Description: A game that introduces the casual user to their browser's developer tools.

The Login2Win Challenge is a simple game where the goal is to login into the website. To login, the user will first need to create an account, which will be challenging as the website is actively trying to prevent it from happening. 

The game starts by disabling the registration link and preventing the user from conveniently reaching the registration page. Once the user overcomes that hurdle, the website uses client-side input validation to prevent the user from entering the required details to register. As the game progresses, the user will slowly learn more about their browser's developer tools and some of the basics on html form inputs. 

Developers may also benefit from playing this game as it might prime them to think more about web security. This game also shows how easy it is to bypass client-side input validation and stresses the importance of server-side input validation. 

#### Implementation details: The website was created in html/bootstrap on the frontend, python/flask on the backend, and hosted on login2win.onrender.com

A total of four routes were used, "/" to show the home page, "/login" for the login page, "/register" for the registration page, and "/about" to describe a bit on what the project is about. 

All the forms in "/login" and "/register" uses html form attribute tags to prevent the user from entering the required data, data validation is done in python/flask to confirm that the user has bypassed the client-side validation and entered the required data. Hints were also given along the way to help users who might be stuck.

The original plan was to also include an SQL injection vulnerability on the login page where the user can add an additional SQL query after the closing tag (i.e. similar to xkcd.com/327/ but instead of DROP TABLE, the user will use INSERT INTO) to add themselves into the database, thus being able to login without the hassle of registering. Unfortunately, db.execute() from the cs50 module did not have the capability to handle multiple queries, which is a ultimately a good thing, but it also means I couldn't add this feature.