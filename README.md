# The Art Of Flour

## Introduction

The Art Of Flour is a recipes blog. It allows the users to replicate the recipes in their homes. Users can also submit their recipes, which are stored in the admin database and can be published in the blog. The Art Of Flour is also an interactive platform, that allows Users to like and comment the Posts. There is a contact form that allows Users to give their feedback and express their opinions about the Blog

![picture alt](/static/images/AmIresponsive.PNG "the-art-of-flour")

The live link for "The Art Of Flour" can be found [here](https://the-art-of-flour.herokuapp.com/ "The Art Of Flour")


# Table of Contents
1. [Table of Contents](#table-of-contents)
1. [Introduction](#introduction)
2. [UX](#ux)
2. [Agile Development](#agile-development)
3. [Design](#design) 
4. [Features](#features)
6. [Technologies Used](#technologies-used)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [Credits](#credits)


# UX

## Admin Stories

### As an Admin:
 - I have the superuser full access.
 - I can create, read, edit and delete all the posts and recipes.
 - I can approve, delete or edit the comments provided by the site Users in the backend.
 - I can collect and store in the database messages sent by the Site Users from the contact form.
 - I can approve/rejec/edit the users' posts(recipes) before publication in the backend.

## Visitor stories.

### As Site User:

 - I can leave/delete my comments on all posts.
 - I can leave likes on blog posts.
 - I can register an account.
 - I can submit my own recipes(posts) and, with the Admin approval, public them on the site.
 - I can update/delete my recipes(posts) if logged in the blog.
 - I can contact the Site Admin for asking question and/or to provide feedbacks.

# Agile Development
 Agile development practices have been used to manage and delivery this project.

 ## Agile Development Tools
 - I used the [MoSCoW method](https://en.wikipedia.org/wiki/MoSCoW_method) to prioritize the project's requirements.
 - I used the [Project Kanban Board](https://github.com/users/nicolascagna96/projects/3/views/1) to help visualize the work and create user stories.
 - I used [GitHub Issues](https://github.com/nicolascagna96/the-art-of-flour/issues) to track my work.


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

The user can creates an account through the Signup form

## Signin
![picture alt](/static/images/login.PNG "the-art-of-flour")
An user that already have an account, can signin to his/her account through this form.

## Signin message
![picture alt](/static/images/signin-message.PNG "the-art-of-flour")
When a user signs in, a success message is displayed on the screen.

## Logout
![picture alt](/static/images/logout.PNG "the-art-of-flour")
An user can logout from the account.

## Logout message
![picture alt](/static/images/signout-message.PNG "the-art-of-flour")
When a user signs out, a success message is displayed on the screen.

## Contact
![picture alt](/static/images/contact.PNG "the-art-of-flour")

## Contact message
![picture alt](/static/images/contact-message.PNG "the-art-of-flour")
An users can contact the Site Admin throught the Contact From.

## Submit Your Recipe
![picture alt](/static/images/submit-recipes-form.PNG "the-art-of-flour")

Once that the Site User creates his own recipe/post, the Site Admin will be able to review it and publish it from the Django Administration dashboard 

## Submit Your Recipe message
![picture alt](/static/images/submit-recipes-message.PNG "the-art-of-flour")
Once that the user submit his/her post recipe, a pending approval message is displayed on the screen.

## Update or Delete a Recipe Post(CRUD)
![picture alt](/static/images/crud-functionality.PNG "the-art-of-flour")

The author of the post can delete and/or edit his own post form the front-end.

## Deleting Recipe 
![picture alt](/static/images/delete-post-message.PNG "the-art-of-flour")

## Recipe deletion successfull message
![picture alt](/static/images/delete-recipe-message.PNG "the-art-of-flour")

## Post view
![picture alt](/static/images/post.PNG "the-art-of-flour")

## Comment
![picture alt](/static/images/comment.PNG "the-art-of-flour")

## Deleting Comment
![picture alt](/static/images/delete_comment.PNG "the-art-of-flour")

## Delete comment message
![picture alt](/static/images/delete_comment_confirmation.PNG "the-art-of-flour")

## Comment Pending Approval
![picture alt](/static/images/comment-approval.PNG "the-art-of-flour")

## Django Administration - Superuser Access
![picture alt](/static/images/site-administration.PNG "the-art-of-flour")
From this dashboard the site Admin can manage the site content.

## Footer & Social Links
![picture alt](/static/images/footer.PNG "the-art-of-flour")

# Future Features to Implement

- Host videos of the recipes.
- Social media sign-in option

# Technologies Used

## Languages Used

-  [HTML5](https://en.wikipedia.org/wiki/HTML5)
-  [CSS3](https://en.wikipedia.org/wiki/CSS)
-  [Python](https://en.wikipedia.org/wiki/Python"Python")
-  [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-  [SQL - Postegres](https://www.postgresql.org/)

## Framewors, Libraries & Tools used
- [Heroku](https://dashboard.heroku.com/apps"Heroku") was used to deploy this app.
- [Github](https://github.com"Github") was used to store the project's code.
- [Gitpod](https://www.gitpod.io/"Gitpod") was used as IDE linked to my GitHub repository.
- [Cloudinary](https://cloudinary.com/users/login?RelayState=%2Fconsole%2Fgetting-started%3Fconsole_customer_external_id%3Dc-617cfc490e076cec8cf7a8126eac86")  cloud service used to store and manage the images
- [Balsamiq](https://balsamiq.com/) used to create the wireframes.
- [Django](https://www.djangoproject.com/) is a Python-based web framework.
- [Google Lightouse](https://developer.chrome.com/docs/lighthouse/overview/) Used for measure the overall quality of web page.  
- [Font Awsome](https://fontawesome.com/) used for the icons of the social links in the footer
- [amiresponsive](https://ui.dev/amiresponsive) to check if the website is responsive on different devices.
- [Bootstrap](https://getbootstrap.com/) Powerful, extensible, and feature-packed frontend toolkit.

## Installed packages
- django-summernote
- django-crispy-forms
- django-allauth
- dj3-cloudinary-storage

# Testing

### W3C HTML Validator
No errors were found when passing all the html pages through the W3C validator.
![picture alt](/static/images/html-validator.PNG "the-art-of-flour")

### W3C CSS Validator
No error were found when passing the CSS code through the validator
![picture alt](/static/images/css-validator.PNG "the-art-of-flour")

### Accessibility
Good accessibility rating in Lighthouse

![picture alt](/static/images/lighthouse.PNG "the-art-of-flour")

### Python code check
Installed in GitPod pycodestyle, and use it to check the Python code. No issues found.(PEP8 website is still down). When running "python3 -m flake8" in the terminal some lines that were reccommended to be shortened, I have left longer for readability purposes.

![picture alt](/static/images/python-code.PNG "the-art-of-flour")

## Further Testings
- I tested the all the pages works in different browsers: Chrome, Safari and Safari.
- I confirmed that this project is responsive, looks good and works on all standard screens using the   devtools device toolbar.
- Social links open to external pages.

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

1. When running "python3 -m flake8" in the terminal some lines that were reccommended to be shortened, I have left longer for readability purposes.
No unfixed bugs found.

# Deployment
This project was deployed to Heroku. I followed these steps:

- Log in to Heroku and create a new app with an unique name.
- Add the Hreoku Postgres database to the Resources tab.
- In the Settings Tab, add the following key and value to the configvars:

1. SECRET_KEY | VALUE: ******
2. PORT | VALUE: 8000
3. CLOUDINARY_URL | API enviroment variable
4. DATABASE_URL | value supplied by heroku
5. DISABLE_COLLECTSTATIC | value = 1

- Add this key/value to the settings.py in Gitpod.
- create the Procfile
- Set Debug = False and add X_FRAME_OPTIONS = SAMEORIGIN in the settings.py
- git push the project to GitHub
- In Heroku settings delete the config vars for DISABLE_COLLECTSTATIC = 1
- click the 'deploy' button.

# Credits.

- Code Institute - "I think therefore I blog" - Walkthrough project
- Code Institute - "Hello Django"
- [mdbootstrap](https://mdbootstrap.com/docs/standard/extended/login/) I used this code for the Login Form
- [Codemy](https://www.youtube.com/watch?v=CVEKe39VFu8) - How To Add Database Forms To A Web Page. Used to understand the logic of databases forms.
- [mdbootstrap](https://mdbootstrap.com/snippets/standard/mdbootstrap/2885134?view=side) - I use it as an inspiration for my footer
- [medium](https://medium.com/jungletronics/a-django-blog-in-vs-code-3b6fc8eb19aa#b3ec) - I use it as an inspiration for the CRUD functionality.
-  [django](https://docs.djangoproject.com/en/4.1/ref/contrib/messages/) - I use it as an inspiration for the message.
- [sherryrich](https://github.com/sherryrich/heard-it) - I checked his Blog project as an inspiration for my project, especially for implementing the CRUD functionality. 

## Media
 - The recipes and the photos were taken by [bbcGoodFood](https://www.bbcgoodfood.com/)


## Acknowledgements
- I want to thank all the Code Institute's tutors for the great support
- Martina Terlevic for reviewing my project and for providing to me a lot of useful feedbacks.
- To create the blog I took inspiration from the Code Institute material especially the "I think therefore I blog" walkthrough project.






































