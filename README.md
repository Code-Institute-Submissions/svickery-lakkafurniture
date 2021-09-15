# Lakka Furniture
## Bespoke Furniture E-Commerce Site

Admin credentials:
* User = admin
* password = Admin1

[View website in Github pages!]()

[View in Heroku](https://lakkafurniture.herokuapp.com/)

![alt text]()

Unfortunately my ReadME is not in depth. There have been major issues with me deploying to heroku and due to time constraints as mentioned above, I could not complete the site as necessary. I know that I will have failed this project and I will have to retake. I used a lot of templates from a project on code institute and I didn't even have the time necessary to style it how I wanted. I couldn't write in the content I wanted. But the back bone of the project is there. I just ran out of time to make it as stylistically as good as I wanted.  

A website designed for the sale of bespoke furniture goods. It is a site that was birthed from making many bespoke items over the years and deciding to mass produce some of their best products. The idea is so that all people can have unique furniture in their home. While they sell stock items, the company still can be contacted for bespoke work and quotes. 

The user goals of the website are as follows:

* Buy unique, bespoke furniture for their home
* To be able to search for particular furniture
* To join the website
* Once the user has joined, they can view their order history and save default delivery information
* To be able to add, delete and edit their purchases at checkout
* Have the option to log in and out of website
* See details of all items on the site.

## UX

#### Ideal user for the website:

* Furniture lovers
* People needing to furnish a new home
* People within the industry 
* Willing to become a member 
* Enjoys an alternative to mainstream furniture companies

#### Visitors for the website will be looking for:

* Furniture to buy
* Be able to check the ratings of products available
* Check the pictures and descriptions of products
* Search for whichever furniture they like in the database
* A pleasant visual experience in line with the products, clean and efficient

#### This website is best to help users because:

* Most furniture sites are flat pack and not unique
* It allows the user to be involved with the website and become a member
* This website is:
    - Easy to navigate
    - Efficient with information
    - Professionally designed and visually appealing

#### User stories:

As a site user, I want to:

1. As a new visitor I want to be able to access the website on any device available to me
2. As a new visitor I want to easily navigate the website
3. As a new visitor I want it so content is easily read and information must be displayed correctly 
4. As a user I want to see unique furniture 
5. As a user I want to see the price of all items
6. As a user I want to know the delivery charge if there is one 
7. As a user I want to be able to purchase as a guest
8. As a user I want to be able to make an account to see order history etc
9. As a user I want to be able to save my card details
10. As a user I want to be able to search for certain products 
11. As a user I want to see testimonials of previous work 
12. As a user I want to be able to contact the site owner for bespoke work
13. As a user I want to see social media links
14. As a user I want to be able to cancel/change order before going ahead
15. As a user I want to be able to see my purchases before going ahead
16. As a user/admin I want to be able to log in/out easily

As an admin, I want to:

1. As an admin I want to be able to create, edit and delete items from my account
2. As an admin I want to be able to create, edit and delete items from my account
3. As an admin I must have log in functionality

As a site owner, I want to:

1. I want to be able to contact customers 
2. Be able to log in and out as admin 
3. Make it so other admins can be used for furniture sellers
4. Provide a clean user experience
5. Provide information to and from database
6. Be able to add to the database easily

The site changed a lot from its original conception. Due to time constraints due to health issues and working a full time job also I had to rapidly change while thinking on my feet. The basic needs are there, but I would have preferred to add a review system to the site.  

## Technologies Used

* The project uses HTML, CSS and JavaScript languages. 
* [Github](https://github.com/) - I used this for all coding (IDE) while building the website.
* [Bootstrap](https://getbootstrap.com/docs/4.5/getting-started/introduction/) - Used for grid layouts and cards on my page. Also allowed me to use Font Awesome icons for my social media links. 
* [Font Awesome](https://fontawesome.com/) - Used for icons in conjuction with bootstrap. 
* [Google Fonts](https://fonts.google.com/) - Used for entire website fonts.
* [Stack Overflow](https://stackoverflow.com/) - Used for styling forms etc from bootstrap. 
* [Web Formatter](https://webformatter.com/) - Used to make my code cleaner and easier to read.
* [W3Schools](https://www.w3schools.com/) - Used to help with various coding questions.
* [Autoprefixer](https://autoprefixer.github.io/) - Used to ensure CSS is correct
* [JQuery](https://jquery.com/) - Used for JQuery elements applied in JavaScript and some help with writing code.
* [Rotten Tomatoes](https://www.rottentomatoes.com/) - Used to have reviews added to site.
* [W3 Validator](https://validator.w3.org/#validate_by_input) - Used to ensure HTML is correct.
* [JS Lint](https://jslint.com/) - Used to ensure JavaScript is correct.
* [Python](https://www.python.org/) - Language used to present data.
* [MongoDB](https://www.mongodb.com/) - Database used for site data schema.
* [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) - Templating language used with Python and Flask.
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Web framework used with Python.
* [Heroku](https://id.heroku.com/login) - Cloud based app for deploying websites.

## Database Schema


## Testing

* Testing could not be completed due to issues deploying to Heroku at the final hour.

#### Further Testing

 * Testing could not be completed due to issues deploying to Heroku at the final hour.
 

#### Known Bugs


## Deployment

### Heroku Deployment

This site is hosted on cloud based web app Heroku. The link is posted at the top of this page. 

To deploy to Heroku, you need to follow these steps:

1. Create an account with Heroku
2. Select the Amazon AWS
3. Create a new app and select the closest region to yourself.

Next in the local repository type in the command line:

4. pip3 freeze == local > requirements.txt

Next make a Procfile in local repo command line:

5. echo web: python3 run.py > Procfile - Note that you can use app.py instead of run.py. 

6. Then in deploy menu option on Heroku site, deploy to Github repository. Do this by clicking connect and typing in your git repo name. Wait a few minutes.
7. Make sure all files are committed in Gitpod and then go to the settings option in Heroku
8. One in settings open Reveal Config Vars
9. In Reveal Config Vars you need to give the following Key/Value statements:

IP : 0.0.0.0
PORT : 5000
MONGO_URI : mongodb+srv://<username>:<password>@cluster0.yg2jd.mongodb.net/YOURDATABASENAME?retryWrites=true&w=majority (this is found in MongoDB)
SECRET_KEY : YOURSECRETKEY
MONGO_DBNAME : YOURDATABASENAME
    
Once this is completed, look to the right hand corner and click Open App. Your deployed site should appear. 

### GitHub Deployment
    
This site is hosted by GitHub pages and deployed directly from the master branch. The site updates automatically from updates that are new commits from the master branch. For the site to deploy on GitHub pages the landing page must be correctly named 'index.html'.

I deployed the site by following the next steps:

1. Logged into GitHub and located the correct repository
2. Went into Settings at the top of my Enjoy Bristol repository
3. Located GitHub "Pages" in settings
4. Selected "Master Branch" from the "Source" dropdown
5. Page automatically refreshed, I scrolled back to "Pages" section to find the newly published site

To make a clone of this site, please follow these steps:

1. Log in to GitHub and find the repository required
2. Click "Clone or download"
3. Use the "Clone with HTTPS" option and copy the link
4. Open Git Bash
5. Edit the working directory to a location you want it to be cloned in
6. Type `git clone` and paste the url you copied previously which should look as follows:

`https://github.com/YOUR-USERNAME/YOUR-REPOSITORY` 

7. Press enter and the repository should be cloned


## Credits

#### Content

All text and content on the page was written by myself apart from some Python logic which I found on a either code institute lessons or stack overflow or youtube. 

My Terms and Conditions were taken from [LawDepot](https://www.lawdepot.com/) and changed to suit the sites needs.

#### Media

All images used on this page were taken from [unsplash.com](https://unsplash.com/). URL links taken from Google.

#### Code

Code for the navigation bar and footer were taken from [Bootstrap](https://getbootstrap.com/docs/4.5/getting-started/introduction/).

Code for the forms and buttons was taken from [W3 Schools](https://www.w3schools.com/).

Code for User Authentication and CRUD functionality taken from Code Institue lessons.

All other code was written by myself with help from sites [Stack Overflow](https://stackoverflow.com/)


## Acknowledgments

Acknoledgments are for my mentor Adegbenga Adeye. Jim Morel and Brian XS who I met through Slack helped with various other issues. 
