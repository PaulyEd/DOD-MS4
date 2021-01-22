

[![alt text](https://res.cloudinary.com/dm2vu1yzr/image/upload/v1611064945/DOD_n69qw3.png)](https://DOD-pe.herokuapp.com/)

  

# RecipeMe

  
<Dev_on_Demand> is a e-commerce Django web app with a CRUD based SQL backend. Its purpose is to allow consumers to buy time with varying developers across numerous code based disaplines/practices, the purpose of the time bought is entirely at the consumers discreation, this could range from consultation for a business enterprise application to assisting a computer science student in a mentor/technical guidance role.

To test Stripe payment functionality in this project please use below details:
- Card number: 4242 4242 4242 4242 (4000 0025 0000 3155 - for extra auth step)
- CVC: any 3 digit number
- Exparation Date: any future date
- Address: any address details


## Table of Contents
  
- [RecipeMe](#recipeme)
  * [Table of Contents](#table-of-contents)
  * [UX & FEATURES](#ux---features)
    + [User](#user)
    + [Design](#design)
      - [Wireframes](#wireframes)
        * [Home](#home)
        * [Dashboard](#dashboard)
        * [Recipe](#recipe)
      - [Database](#database)
    + [Features](#features)
      - [Navbar](#navbar)
      - [Spotlight](#spotlight)
      - [Featured](#featured)
      - [Search](#search)
      - [Full Account Management](#full-account-management)
      - [Dashboard Data](#dashboard-data)
      - [Add Recipe](#add-recipe)
      - [Edit Recipe / Copy & Edit Recipe / Delete Recipe](#edit-recipe---copy---edit-recipe---delete-recipe)
  * [TECHNOLOGIES USED](#technologies-used)
    + [Languages](#languages)
    + [APIs](#apis)
    + [Frameworks](#frameworks)
    + [Libraries](#libraries)
    + [Tools](#tools)
  * [TESTING / ISSUE RESOLUTION](#testing---issue-resolution)
  * [DEPLOYMENT](#deployment)
    + [Hosting](#hosting)
    + [Environment Variables - TO BE UPDATED](#environment-variables---to-be-updated)
    + [Requirements](#requirements)
    + [Cloning a Repository](#cloning-a-repository)
    + [Installing Dependencies](#installing-dependencies)
  * [CREDITS](#credits)
    + [Media](#media)
    + [Acknowledgements](#acknowledgements)
    + [Code Snippets / References](#code-snippets---references)
      - [Javascript / JQuery:](#javascript---jquery-)
      - [Python / Django:](#python---django-)
      - [Bootstrap:](#bootstrap-)
      - [Misc:](#misc-)
  * [FAIR USE DISCLAIMER](#fair-use-disclaimer)


## UX & FEATURES

  

### User Stories

| User Story ID                  | As a/an     | I want to be able to…                                             | So that I can…                                                                |
|--------------------------------|-------------|-------------------------------------------------------------------|-------------------------------------------------------------------------------|
| Viewing and Navigation         |             |                                                                   |                                                                               |
| 1                              | Shopper     | View a list of Developers                                         | To see options available to me                                                |
| 2                              | Shopper     | View Developer details                                            | Identify price, developer skills & experiences                                |
| 3                              | Shopper     | Quick view and detail view of cart/bag                            | To manage/control my potential purchase                                       |
| 4                              | Shopper     | Adjust cart/bag anytime to control my potenial outlay             | To manage/control my potential purchase                                       |
| Registration and User Accounts |             |                                                                   |                                                                               |
| 5                              | Site User   | Register for an account                                           | Have a personal account to view my profile                                    |
| 6                              | Site User   | Login and Logout                                                  | Easily access my personal information                                         |
| 7                              | Site User   | Recover my password                                               | Recover access to my account                                                  |
| 8                              | Site User   | Receive an email conformation                                     | Verify my registration was successful                                         |
| 9                              | Site User   | Have a personalized user profile                                  | To view my personal information such as payment information and order history |
| 10                             | Customer    | Leave a review                                                    | Leave my testimonial and support this small business                          |
| 11                             | Customer    | Edit my review                                                    | Edit my previously created review with new details                            |
| 12                             | Customer    | Delete my review                                                  | Delete my previously created review as I may feel its no longer valid or reivewed in error |
| 13                             | Developer   | Dispute a review                                                  | I may feel I have been harshly reviewed and want a site owner to remove / let me respond   |
| Sorting and searching          |             |                                                                   |                                                                               |
| 10                             | Shopper     | Sort the list of developer by rating or price                     | View the available developers by the rating and price                         |
| 10                             | Shopper     | Search for a developer by language/framework                      | Quickly find the developer with the skills I need                             |
| Purchasing and Checkout        |             |                                                                   |                                                                               |
| 10                             | Customer    | View items in my bag to be purchased                              | see the developers and total cost before I purchase                           |
| 10                             | Customer    | Adjust the quantity or remove items in my bag                     | Easily make changes before checkout                                           |
| 10                             | Customer    | Enter my payment information                                      | Check out easily with no problems                                             |
| 10                             | Customer    | View an order confirmation after checkout                         | Verify there are no mistakes with my address, order, or payment information   |
| Admin and store management     |             |                                                                   |                                                                               |
| 10                             | Store Owner | Add a developer                                                   | Add a new item to my store                                                    |
| 10                             | Store Owner | Edit a developer                                                  | Change any details in the price or description                                |
| 20                             | Store Owner | Delete a developer                                                | Remove items that are no longer available                                     |
| 20                             | Store Owner | Moderate reviews                                                  | To prevent inappropriate comments on site and allow devs to dispute 'unfair' reviews |


### Design

This Project is designed to allow users to conduct basic CRUD (Create, Read, Update, Delete) actions on a database. The database utilised for this app is [MongoDB](https://www.mongodb.com/what-is-mongodb), more on this [below](#database) . The Frontend of the project is mainly [Bootstrap](https://getbootstrap.com/) as it is modern, responsive and a template style a lot of web users would be familiar with.

#### Wireframes

For this project I used [Balsamiq](https://balsamiq.com/) to create my initial frontend design using wireframes, very basic setup was done initially and the wireframes were updated as the project progressed along with my vision for how I wanted the app to look.

##### Home

| Desktop / Tablet      | Mobile                 | 
| --------------------- | ------------------------ | 
|<img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1599469893/Desktop_-_Home_pxnxue.png"  style="center"  width="100%"> | <img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1599469893/Mobile_-_Home_xr5z6a.png"  style="center"  width="100%"> |
 
##### Dashboard
| Desktop / Tablet      | Mobile                 | 
| --------------------- | ------------------------ | 
|x<img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1599469893/Desktop_-_Dashboard_j0jgtp.png"  style="center"  width="100%">| <img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1599469893/Mobile_-_Dashboard_j68gyr.png"  style="center"  width="100%">|
 
##### Recipe

| Desktop / Tablet         | Mobile                 | 
| --------------------- | ------------------------ | 
| <img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1599469893/Desktop_-_Recipe_bcwdio.png"  style="center"  width="100%"> | <img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1599469893/Mobile_-_Recipe_b6lbaa.png"  width="100%"> | 

#### Database

For this project I used [MongoDB Atlas](https://account.mongodb.com/account/login) to host my database, see schema below:

 <img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1599475537/Schema_-_Full_adwzjb.png"  style="center"  width="100%">

### Features

#### Navbar

Stored on the base.html file to create consistency across all of the pages, provides quick access to home, spotlight, featured, and all recipes.

Also provides entry point for [account management](#full-account-management) and [search](#search) functionality outlined below.

 <img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1599476966/Nav_bi150b.png"  style="center"  width="100%">

#### Spotlight

Shows which user is currently the highest-rated and that users highest rated recipe.

 <img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1599476970/Spotlight_awkwmw.png"  style="center"  width="70%">
 
#### Featured

Shows the top 3 rated recipes on the app.

 <img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1599476969/Featured_iicnpw.png"  style="center"  width="70%">

#### Search

Allows users to enter a term(s) and return results based off of the entered data, the search creates an index to check against recipe name, description & ingredients 

<img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1599477745/search_il0m5y.png"  style="center"  width="70%">

#### Full Account Management

Full CRUD actions available for a user account, and [Flask](https://flask.palletsprojects.com/en/1.1.x/) utilized to facilitate user log n / log out via sessions.

 <img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1599476608/Account_Managment_ia0xlu.png"  style="center"  width="100%">

#### Dashboard Data

Upon logging in if a user has created recipes they will be presented with graphical data regarding how users have interacted with their recipes in terms of ratings. These graphs show the rating distribution (number of each rating given to users recipes) and most rated recipes (users recipes that have had the highest number of votes registered)

 <img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1599477850/Charts_pl7i73.png"  style="center"  width="100%">

#### Add Recipe

For users to add a recipe they first need to be logged in, this could be seen as a potential barrier for frivolous users, but it encourages users to be more active and engaged with the app by creating an account.

To add a new recipe the user can simply click the dropdown under their name and select "Add recipe" from anywhere on the site, this will then prompt a tabbed modal to appear where the recipe can be added in three sections, images can be added after the recipe is added.

 <img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1599478300/recipemodal_l2gb5e.png"  style="center"  width="100%">

#### Edit Recipe / Copy & Edit Recipe / Delete Recipe

When on a recipe page:
1.  The owner of the recipe is presented with an option to edit a recipe that will bring the user to a new page similar to the add recipe modal, where whatever is already in the recipe, will be populated and available for editing. They also here have the option to upload an image for their recipe here. This works through [Cloudinary](https://cloudinary.com/) API, if there is no image a new image will be uploaded to Cloudinary and the image URL will be stored in the database on the recipe document, if an image already exists it will delete the existing image, upload the new image and update the database will the new images URL. Also, only the owner of a recipe will be presented with the option to delete a recipe that will fully remove the recipe and all ratings for the associated recipe from the database.
 
 <img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1599493670/upload_image_ewmd3n.png"  style="center"  width="100%">

2. A signed up (not-recipe owner) user will be presented with the option to copy a recipe, this fundamentally work very similar to the edit recipe except this does not overwrite the original recipe, it adds a new instance of it with a new ID and the author/owner of this new version is the user who copied it.

 <img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1599493331/edit_copy_recipe_zv70zy.png"  style="center"  width="100%">

3. A non-signed up user will only be able to view the recipe, attempts to do actions that are limited to signed up users will redirect them to the home page.

## TECHNOLOGIES USED

  

### Languages

*  [HTML](https://en.wikipedia.org/wiki/HTML) - Struture of the page.

*  [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - Style of the page.

*  [Javascript](https://en.wikipedia.org/wiki/JavaScript) - User and API interaction/animation.

*  [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) 3.8.3 - Backend of app.  

* [Jinja2](https://pypi.org/project/Jinja2/) 2.11.2 - Templating language.

### APIs

*  [Cloudinary](https://cloudinary.com/)

### Frameworks
*	[Flask 1.1.2](https://flask.palletsprojects.com/en/1.1.x/)

### Libraries

*  [Bootstrap 4.5](https://getbootstrap.com/)

*  [Font Awesome 5.14](https://fontawesome.com/)

*  [JQuery 3.5.1](https://jquery.com/)

*  [Chart.js 2.8.0](https://www.chartjs.org/)


### Tools

* [Github](https://github.com/) - Repository Hosting.

* [Gitpod](https://www.gitpod.io/) - IDE.

* [Google Chrome developer tools](https://developers.google.com/web/tools/chrome-devtools) - UX Testing.

* [Responsive Test Tools](http://responsivetesttool.com/) - UX Testing.

* [W3C - HTML Validator](https://validator.w3.org/) - Validate HTML.

* [W3C - CSS Validator](https://jigsaw.w3.org/css-validator/) - Validate CSS.

* [Codebeautify](https://codebeautify.org/css-beautify-minify) - Format CSS.

* [AutoPrefixer](https://autoprefixer.github.io/) - Add vendor prefixes to CSS.

* [Codepen](https://codepen.io/) - Isolated code testing.

* [Balsamiq](https://balsamiq.com/) - Wireframes.

* [Stackedit](https://stackedit.io/) - Live markdown editor.

* [vecteezy](https://www.vecteezy.com/) - App graphics.

* [GitGuardian.com](https://dashboard.gitguardian.com/) - Monitor repo commits for senstive information(API keys etc).

> Note: Additional dependencies per requirements.txt file

## TESTING / ISSUE RESOLUTION

  

Each section has had extensive individual testing across multiple browsers including the use of chrome developer tools & [Website Responsive Testing Tool](http://responsivetesttool.com/) to test on a wide variety for sizes and aspect ratios, please see some key points to note below:

  

1. Sensitive Data - upon deploying the live version of the site I noticed that my env.py file (containing API keys, Secrets etc.) had been committing to my repo despite being included in my git ignore file, after discovering this my plan was to rewrite the files out of my git history with `git filter-branch --index-filter 'git rm --cached --ignore-unmatch env.py' HEAD` but after consulting with Code Institute it was determined the best approach would be to remove the latest file and change all my keys, which I did.

  

2. User Testing - after deploying the live version of the site I had several family/friends try to use the app without instruction and based on these there was several fixes and updates to be made. in terms of fixes, the most notable was if a user was the "Top Chef" on the site and then delete their account, instead of the next highest rated user becoming top chef the section would just be blank, this behaviour was rectified. There was also a lot of feedback in terms of "expected behaviour", where a user would try click something they expected to be a link (such as recipe name, chef name) it wasn't set up as a nav link, this was also updated.

  

3. Session Testing - this was a major part of this project, ensuring only users who were authorised to do certain actions could do certain actions. Some of the key scenarios for testing were as follows:
`No Account User`  to ensure they only had read the ability to the site, this user cannot add, update, delete any recipes without first signing up for an account and being in an active session. This goes beyond ti just presenting the link to the user but having server site code to detect if the user manual tried to access the functions via manual input of the URL.
`Account User` be able to add a new recipe, rate recipes, be able to be top chef, be able to save other users recipes as for easy access, ensure dashboard populates correctly if the user has rated recipes.**
`Account User - Recipe Owner` to ensure only the owner of a recipe could edit/delete a recipe and add an image for that recipe.
`Account User - Not Recipe Owner` to be able to copy and create their own version of another users recipe without it impacting the original recipe.

>**As part of this testing it was discovered that the dashboard was populating based on ratings given out by the user instead of ratings for the users' recipes, this was rectified.
  

5. General UX Testing - Validating links: - TO BE UPDATED

| Element/Link| Linked to / Action| 
| - | - | 
|Logo|Home|
|Spotlight/Featured|Homepage sections|
|All Recipes|All recipes function|
|Sign In|Sign In modal|
|Sign In button|Sign in function|
|Create one button|Create account modal|
|Create Account button|Create account function|
|Password Fields|JS to validate match|
|Password visable icons|Display password on hover|
|Rating Stars|Highlight on hover / Rating function on click|
|Add/Edit/Copy/Delete/Save/Unsave recipes|Linked to appropriate functions|
|Sign Out|End session|
|Edit Account|Edit account modal|
|Update Account button|Update account function|
|Delete Account|Delete account modal|
|Delete Account button|Delete account function|
|Username links|Display that users recipes|




## DEPLOYMENT

  

### Hosting
As this app depending on backend python code it requires hosting on a server that can run this code, there are several options available here such as [AWS](https://aws.amazon.com/getting-started/hands-on/launch-an-app/), [Azure](https://azure.microsoft.com/en-us/free/python/search/?&ef_id=CjwKCAjwnef6BRAgEiwAgv8mQYQ2u3TBwNQaph4w1PVAZ0mpLjV_Ja8FpqxLBB1hcLB261n1nIeUeBoCmRYQAvD_BwE:G:s&OCID=AID2100059_SEM_CjwKCAjwnef6BRAgEiwAgv8mQYQ2u3TBwNQaph4w1PVAZ0mpLjV_Ja8FpqxLBB1hcLB261n1nIeUeBoCmRYQAvD_BwE:G:s&dclid=CMKMnZyr3usCFYNjFQgd1iUP2A) & [Heroku](https://www.heroku.com/). This project has been hosting on Heroku.


  
### Environment Variables - TO BE UPDATED

You will need to set up the following environment variables on your system.

| Variable name         | Used for                 | Notes                                                        |
| --------------------- | ------------------------ | ------------------------------------------------------------ |
| CLOUDINARY_API_KEY| Cloudinary Image package | Found in your Cloudinary account dashboard                    |
| CLOUDINARY_API_SECRET| Cloudinary Image package | Found in your Cloudinary account dashboard                    |
| CLOUDINARY_CLOUD_NAME| Cloudinary Image package | Found in your Cloudinary account dashboard                    |
| db_name**| Mongo DB | This is the name of your database collection |
| MONGO_URI**| Mongo DB | Found in the connect button on the database cluster          |
| secret_key**| Flask   | This is a unique secret used for session encryption,  you can use any random string for this |
| IP                    | Flask                    | You can use `0.0.0.0` here to indicate a local IP address    |
| PORT                  | Flask                    | You can use the default port `5000`                          |




**From MongoDB:
1. db_name:
<img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1599732673/DBname_rlobu4.png"  style="center"  width="15%">
2. MONGO_URI:
<img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1599732964/MongoURI_atcgyp.png"  style="center"  width="70%">
3. secret_key:
Can be generated in terminal via `python -c 'import os; print(os.urandom(16))'` There is a good answer on StackExchange for this [here](https://unix.stackexchange.com/questions/230673/how-to-generate-a-random-string) which give options to include/exclude certain characters.

### Requirements
1. Python 3.8.3 or later
2. Git
3. IDE (Integrated Development Environment) or code editor

### Cloning a Repository

1. Go to the main page of the GitHub repository and click on the dropdown menu **'Clone or download'**

2. Copy the URL and go to your local IDE

3. In the terminal of your IDE type in **'git clone'** and then paste the URL copied from step 2

4. Press **Enter** and the clone will be created

  
### Installing Dependencies
For the code to run the dependencies will need to be installed, to do this in the terminal use `pip3 install -r requirements.txt`, if updates are made and further dependencies have been added please use `pip3 freeze --local > requirements.txt`to update the requirements.txt file

## CREDITS

  

### Media

- The images/icons/graphics used in this site were obtained from [INSERT](https://www.INSERT.com/) (See Fair Use Disclaimer)

  

### Acknowledgements

  

I received inspiration for this project from the below websites:


1.  [XXX](https://www.INSERT.co.uk/food)

2.  [XXX](https://www.INSERT.com/)

> Also big thanks to 

### Code Snippets / References

Below links helped me in various parts of the project to overcome issues:

#### Javascript / JQuery:


#### Python / Django:


#### Bootstrap:


#### Misc:


  

## FAIR USE DISCLAIMER

- The images, icons, and graphics used in this project are not owned by me and I have not been permitted to use these, the purpose of their inclusion is purely for visuals within the project and the entire project is for nonprofit educational purposes. If this site was to ever go outside the remit of "nonprofit educational" then these images would be removed before such action.