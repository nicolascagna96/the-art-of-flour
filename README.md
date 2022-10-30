# The Art Of Flour

## Introduction

The Art Of Flour is a recipes blog. It allows the users to replicate the recipes in their homes. Users can also submit their recipes, which are stored in the admin database and can be published in the blog. The Art Of Flour is also an interactive platform, that allows Users to like and comment the Posts. There is a contact form that allows Users to give their feedback and express their opinions about the Blog

![picture alt](/static/images/AmIresponsive.PNG "the-art-of-flour")

The live link for "The Art Of Flour" can be found [here](https://the-art-of-flour.herokuapp.com/ "The Art Of Flour")

## QR Code
Sacn the QR Code to open the live website!

![picture alt](/static/images/frame.png "the-art-of-flour")


# Table of Content

1. [Introduction](#introduction)
2. [UX](#ux)
3. [Design](#design) 
4. [Features](#features)
6. [Technologies Used](#technologies-used)
7. [Testing](#testing)
8. [ Deployment](#deployment)
9. [Credits](#credits)


# UX User Stories

## Admin Stories

### As an Admin:
 - As Site Admin I can create and submit new blog posts.
 - As Site Admin I can approve or delete the comments provided by the site Users.
 - As Site Admin I can collect and store in the database the recipes and the messages sent by the Site Users.

 ### As Site User:

 - I can leave comments on blog posts to leave my feedabacks.
 - I can leave likes on blog posts.
 - I can register an account.
 - I can submit my own recipes to the Admin thank to the Submit Recipe form.
 - I can contact the Site Admin/Creator for asking question or to provide feedbacks.


 # Design

 ## Wireframe

### Homepage:
![picture alt](/static/images/home-frame.png "the-art-of-flour")
### Blog Post Frame:
![picture alt](/static/images/post-frame.png "the-art-of-flour")
### Contact Form Frame:
![picture alt](/static/images/contact-frame.png "the-art-of-flour")
### Signup Frame
![picture alt](/static/images/signup-frame.png "the-art-of-flour")
### SignIn Frame:
![picture alt](/static/images/login-frame.png "the-art-of-flour")
### Logout frame:
![picture alt](/static/images/logout-frame.png "the-art-of-flour")

## Site Navigation

![picture alt](/static/images/SiteNavigation.drawio.png "the-art-of-flour")

## Database Schema

![picture alt](/static/images/databaseschema.png "the-art-of-flour")

# Features

## Existing Features 

## Home Page
![picture alt](/static/images/homepage.PNG "the-art-of-flour")

## Navigation bar 1
This is teh navigation bar when the User is not logged into the Blog.
![picture alt](/static/images/navbar.PNG "the-art-of-flour")

## Navigation bar 2
This is the navigation bar that the Users see after the Login.
![picture alt](/static/images/navbar-login.PNG "the-art-of-flour")

## Signup
![picture alt](/static/images/signup.PNG "the-art-of-flour")

## Signin
![picture alt](/static/images/login.PNG "the-art-of-flour")

## Signin message
![picture alt](/static/images/signin-message.PNG "the-art-of-flour")

## Logout
![picture alt](/static/images/logout.PNG "the-art-of-flour")

## Logout message
![picture alt](/static/images/signout-message.PNG "the-art-of-flour")

## Contact
![picture alt](/static/images/contact.PNG "the-art-of-flour")

## Contact message
![picture alt](/static/images/contact-message.PNG "the-art-of-flour")

## Submit Your Recipe
![picture alt](/static/images/submit-recipe.PNG "the-art-of-flour")

## Submit Your Recipe message
![picture alt](/static/images/submit-recipe-message.PNG "the-art-of-flour")

## Post view
![picture alt](/static/images/post.PNG "the-art-of-flour")

## Comment
![picture alt](/static/images/comment.PNG "the-art-of-flour")

## Comment Pending Approval
![picture alt](/static/images/comment-approval.PNG "the-art-of-flour")

## Django Administration - Superuser Access
![picture alt](/static/images/superuser.PNG "the-art-of-flour")

## Footer & Social Links
![picture alt](/static/images/footer.PNG "the-art-of-flour")

# Future Features to Implement

- Host videos of the recipes.
- Social media sign-in option

# Bugs encountered during development
 1. I could not storage the imgaes provided by the Users in the Admin database for the contact and submit recipes forms.

- I asked for help to the tutor and he suggested to me to add the "enctype" attribute in the form element.

2. Error message after adding a form:
- CSRF token had been added as CSRF and the error was fixed.

3. App wasn't deploying to heroku correctly. 
- Typo error. DEBUG = Flse instead of writing DEBUG = FALSE.

4. CSS wasn't loading correctly.
- The tutor explained to me that the error was caused by a space in the token provided.

## Unfixed Bugs

No unfixed bugs present so far.

# Technologies Used

## Languages Used

-  [HTML5](https://en.wikipedia.org/wiki/HTML5)
-  [CSS3](https://en.wikipedia.org/wiki/CSS)
-  [Python](https://en.wikipedia.org/wiki/Python"Python")
-  [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

## Framewors, Libraries & Tools used
- [Heroku](https://dashboard.heroku.com/apps"Heroku")
- [PEP8](https://pep8.org/"PEP8")
- [Github](https://github.com"Github")
- [Gitpod](https://www.gitpod.io/"Gitpod")
- [Cloudinary](https://cloudinary.com/users/login?RelayState=%2Fconsole%2Fgetting-started%3Fconsole_customer_external_id%3Dc-617cfc490e076cec8cf7a8126eac86")
- [Balsamiq](https://balsamiq.com/)
- [Django](https://www.djangoproject.com/)
- [Balsamiq](https://balsamiq.com/)
- [Google Lightouse](https://developer.chrome.com/docs/lighthouse/overview/)
- [Font Awsome](https://fontawesome.com/)


































