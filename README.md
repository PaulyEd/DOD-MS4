

[![alt text](https://res.cloudinary.com/dm2vu1yzr/image/upload/v1611064945/DOD_n69qw3.png)](https://DOD-pe.herokuapp.com/)

  

# <Dev_on_Demand>

  
The purpse of this project is to demostrate the knowledge & skills developed in the final section of my course with The Code Institute. <Dev_on_Demand> is a e-commerce Django web app with a CRUD based SQL backend, its purpose is to allow freelance developers a place to market themselves and allow consumers to buy time with varying developers across numerous code based disaplines/practices, the purpose of the time bought is entirely at the consumers discreation, this could range from consultation for a business enterprise application to assisting a computer science student in a mentor/technical guidance role.

Note: this project felt like a sizable leap from the previous one and as such I felt most comfortable coding along with the Code Institute 'Boutique Ado' project and tailoring it to my needs as I went.

To test Stripe payment functionality in this project please use below details:
- Card number: 4242 4242 4242 4242 (4000 0025 0000 3155 - for extra auth step)
- CVC: any 3 digit number
- Exparation Date: any future date
- Address: any address details


## Table of Contents
  
- [RecipeMe](#recipeme)
  * [Table of Contents](#table-of-contents)
  * [UX & FEATURES](#ux---features)
    + [User Stories](#user-stories)
    + [Design](#design)
      - [Wireframes](#wireframes)
        * [Home](#home)
        * [Dashboard](#dashboard)
        * [Recipe](#recipe)
      - [Primary Django Models](#primary-django-models)
    + [Features / Design Choices](#features---design-choices)
      - [Navbar](#navbar)
      - [Bootstrap](#bootstrap)
      - [Colour Scheme](#colour-scheme)
      - [Search](#search)
      - [Side Bar Cart/Bag](#side-bar-cart-bag)
      - [Admin](#admin)
        * [Admin](#admin-1)
        * [Add a developer](#add-a-developer)
        * [Pending Reviews](#pending-reviews)
      - [Cart](#cart)
      - [Checkout + Stripe](#checkout---stripe)
      - [Profile](#profile)
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
| 14                             | Shopper     | Sort the list of developer by rating or price                     | View the available developers by the rating and price                         |
| 15                             | Shopper     | Search for a developer by language/framework                      | Quickly find the developer with the skills I need                             |
| Purchasing and Checkout        |             |                                                                   |                                                                               |
| 16                             | Customer    | View items in my bag to be purchased                              | see the developers and total cost before I purchase                           |
| 17                             | Customer    | Adjust the quantity or remove items in my bag                     | Easily make changes before checkout                                           |
| 18                             | Customer    | Enter my payment information                                      | To complete purchase                                                          |
| 19                             | Customer    | View an order confirmation after checkout                         | Verify there are no mistakes with order or payment information                |
| Admin and store management     |             |                                                                   |                                                                               |
| 20                             | Store Owner | Add a developer                                                   | Add a new developers to the store                                             |
| 21                             | Store Owner | Edit a developer                                                  | Change any details in the rate or description                                 |
| 22                             | Store Owner | Delete a developer                                                | Remove developers that are no longer available                                |
| 23                             | Store Owner | Moderate reviews                                                  | To prevent inappropriate comments on site and allow devs to dispute 'unfair' reviews |


### Design

This Project is designed to allow users to find developers that meet their required skillset and experience, purchase time with those developers and review them to that other customers can see what other peoples experiences have been like with specific developers.

#### Wireframes

For this project I used [Balsamiq](https://balsamiq.com/) to create my initial frontend design using wireframes, very basic setup was done initially and the wireframes were updated as the project progressed along with my vision for how I wanted the app to look.

##### Home

| Desktop / Tablet      | Mobile                 | 
| --------------------- | ------------------------ | 
|<img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1611493587/Home_-_Desktop_kuzcbx.png"  style="center"  width="100%"> | <img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1611493586/Home_-_Mobile_zgzluj.png"  style="center"  width="100%"> |
 
##### Developers
| Desktop / Tablet      | Mobile                 | 
| --------------------- | ------------------------ | 
|x<img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1611493585/Devs_-_Desktop_acyd7s.png"  style="center"  width="100%">| <img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1611493585/Devs_-_Mobile_a0ywav.png"  style="center"  width="100%">|
 

#### Primary Django Models

Order Model: Mirrored from 'Boutique Ado' project - used to maintain customer orders
Developer Model: Similar to 'Products' from 'Boutique Ado' project in terms of primary offering for sale  - model that stores all the information related to the offering of the store
UserProfile Model: Mirrored from 'Boutique Ado' project - used to maintain customer profiles
Review Model: Entirely custom - used to store information related to customer reviews of developers

### Features / Design Choices

#### Navbar

Central navigation point of the project, split into different files for desktop and mobile variations, provides quick access to all the major link/functions of the site.

 <img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1611493594/Navbar_fbd3fe.png"  style="center"  width="100%">

#### Bootstrap

This was an intensive project, and I had to put most of my time into learning Django, therefore Bootstrap was leveraged heavily in this project so time wasnt lost on custom HTML/CSS to much. 

 <img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1599476970/Spotlight_awkwmw.png"  style="center"  width="70%">
 
#### Colour Scheme

Bootstrap Primary, White and off-white was the main colour scheme used on this site as I felt the colour was appropriate, had a nice contrast and most importantly given the timeframe, was native to bootstrap and such was a quick solution.

 <img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1599476969/Featured_iicnpw.png"  style="center"  width="70%">

#### Search

Allows users to enter a term(s) and return results a developers name, what languages they speak and what languages or frameworks they are experienced in.

<img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1611493594/Navbar_Search_cf7gdl.png"  style="center"  width="70%">

#### Side Bar Cart/Bag

Shows users what they current have in their bag at all times in a non-intrusive manner

 <img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1611493942/SideCart2_lpbqeq.png"  style="center"  width="40%">

#### Admin

##### Admin

Link for admin to easily get the Django admin site if they needed functionality beyond that built into primary store frontend.

<img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1611493594/Admin_options_pk97i1.png"  style="center"  width="70%">

##### Add a developer

Section for site owners to add new developers to their site.

##### Pending Reviews

Section for site owners to to moderate customer reviews on the developers.

#### Cart

Store customer selections and show details include price and quantity of developers they intend to purchase 

 <img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1611494192/cart_ced3ts.png"  style="center"  width="70%">

#### Checkout + Stripe

Allow users to complete their purchase via stripe API, have their order confimed and a summary of the order available on theur profile and emailed to them
 
 <img  src="https://res.cloudinary.com/dm2vu1yzr/image/upload/v1611494192/checkout_ifrw42.png"  style="center"  width="70%">

#### Profile

Section where customers can see activity on their account such as previous orders and review they have left on developers they have previously worked with.


## TECHNOLOGIES USED

  
### Languages

*   [HTML](https://en.wikipedia.org/wiki/HTML) - Struture of the page.

*   [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - Style of the page.

*   [Javascript](https://en.wikipedia.org/wiki/JavaScript) - User and API interaction/animation.

*   [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) 3.8.6 - Backend of app.  

### APIs

*   [Stripe](https://stripe.com/en-ie)

### Frameworks
*   [Django](https://www.djangoproject.com/)

### Libraries

*   [Bootstrap 4.5.3](https://getbootstrap.com/)

*   [Font Awesome 5.15.2](https://fontawesome.com/)

*   [JQuery 3.5.1](https://jquery.com/)

*   [Toastr.js 2.1.3](https://github.com/CodeSeven/toastr)


### Tools

*   [Github](https://github.com/) - Repository Hosting.

*   [Gitpod](https://www.gitpod.io/) - IDE.

*   [Google Chrome developer tools](https://developers.google.com/web/tools/chrome-devtools) - UX Testing.

*   [Responsive Test Tools](http://responsivetesttool.com/) - UX Testing.

*   [W3C - HTML Validator](https://validator.w3.org/) - Validate HTML.

*   [W3C - CSS Validator](https://jigsaw.w3.org/css-validator/) - Validate CSS.

*   [Codebeautify](https://codebeautify.org/css-beautify-minify) - Format CSS.

*   [AutoPrefixer](https://autoprefixer.github.io/) - Add vendor prefixes to CSS.

*   [Codepen](https://codepen.io/) - Isolated frontent code testing.

*   [Balsamiq](https://balsamiq.com/) - Wireframes.

*   [Stackedit](https://stackedit.io/) - Live markdown editor.

*   [Pexels](www.pexels.com) - Developer Pictures.

*   [JSONFormatter](https://jsonformatter.org/) - Format fixture files.

*   CSV/JSON Tools [1](https://csvjson.com/csv2json), [2](https://json-csv.com/), [3](https://www.convertcsv.com/csv-to-json.html) - Multiple tools used to help me create and convert fixture files from csv to json.

*   [Pexels](www.pexels.com) - Developer Pictures.

*   [GitGuardian.com](https://dashboard.gitguardian.com/) - Monitor repo commits for senstive information(API keys etc).

*   [GitGuardian.com](https://dashboard.gitguardian.com/) - Monitor repo commits for senstive information(API keys etc).

*   [Markdown - TOC](https://ecotrust-canada.github.io/markdown-toc/) - Generate table of contents for README.md.

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
*   https://stackoverflow.com/questions/45004245/how-to-use-toastr-in-django-for-success-or-fail-message
*   https://bbbootstrap.com/snippets/simple-toast-notification-toastr-76085299
*   https://stripe.com/docs/js/appendix/style
https://stackoverflow.com/questions/406192/get-current-url-with-jquery

#### Python / Django:
*   https://stackoverflow.com/questions/25386119/whats-the-difference-between-a-onetoone-manytomany-and-a-foreignkey-field-in-d#:~:text=of%20the%20relationship.-,ForeignKey,may%20be%20related%20to%20one.
*   https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_many/
*   https://stackoverflow.com/questions/4270330/django-show-a-manytomanyfield-in-a-template
*   https://stackoverflow.com/questions/3217492/list-of-language-codes-in-yaml-or-json
*   https://stackoverflow.com/questions/8368937/change-model-class-name-in-django-admin-interface/8369031
*   https://stackoverflow.com/questions/35288084/how-to-display-a-manytomany-fields-in-the-template
*   https://stackoverflow.com/questions/27149984/django-how-to-get-count-for-manytomany-field
*   https://stackoverflow.com/questions/15507171/django-filter-query-foreign-key
*   https://stackoverflow.com/questions/4459703/how-to-make-lists-contain-only-distinct-element-in-python
*   https://stackoverflow.com/questions/39197723/how-to-move-singup-signin-templates-into-dropdown-menu/39235634#39235634
*   https://www.youtube.com/watch?v=dXZim_jgaiI
*   https://stackoverflow.com/questions/57192979/remove-substring-from-string-if-substring-is-contained-in-a-list
*   https://www.reddit.com/r/django/comments/2q5u0p/way_to_make_a_min_and_max_values_restriction_on_a/
*   https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model
*   https://docs.djangoproject.com/en/3.1/ref/models/fields/
*   https://stackoverflow.com/questions/31130706/dropdown-in-django-model
*   https://stackoverflow.com/questions/4673985/how-to-update-an-object-from-edit-form-in-django
*   https://docs.djangoproject.com/en/3.1/topics/db/queries/
*   https://stackoverflow.com/questions/3965104/not-none-test-in-python
*   https://stackoverflow.com/questions/4843158/check-if-a-python-list-item-contains-a-string-inside-another-string
*   https://stackoverflow.com/questions/37867447/how-can-i-update-a-django-models-datetimefield-when-another-specific-field-in-t
*   https://stackoverflow.com/questions/27771000/django-template-convert-to-string
*   https://stackoverflow.com/questions/10556940/succinct-way-of-updating-a-single-field-of-a-django-model-object
*   https://stackoverflow.com/questions/8616343/django-calculate-the-sum-of-the-column-values-through-query
*   https://docs.djangoproject.com/en/dev/ref/templates/builtins/#floatformat
*   https://stackoverflow.com/questions/28515470/wsgirequest-object-has-no-attribute-get


#### Bootstrap / HTML / CSS:
*   https://jsfiddle.net/bootstrapious/c7ash30w
*   https://www.bootdey.com/snippets/view/profile-with-data-and-skills#preview
*   https://freefrontend.com/bootstrap-profiles/
*   https://stackoverflow.com/questions/10989238/center-image-horizontally-within-a-div
*   https://stackoverflow.com/questions/37920332/force-image-tag-to-be-perfect-circle
*   https://stackoverflow.com/questions/37261988/force-text-to-stay-on-one-line
*   https://bootsnipp.com/snippets/ZXKKD
*   https://css-tricks.com/snippets/css/sticky-footer/
*   https://www.w3schools.com/howto/howto_css_hide_scrollbars.asp

#### Misc:


  

## FAIR USE DISCLAIMER

- The images, icons, and graphics used in this project are not owned by me and I have not been permitted to use these, the purpose of their inclusion is purely for visuals within the project and the entire project is for nonprofit educational purposes. If this site was to ever go outside the remit of "nonprofit educational" then these images would be removed before such action.