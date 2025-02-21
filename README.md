<!-- # Hygge Houseplants Website

![Am I responsive - Hygge Houseplants](static/docs/amiresponsive.png "Am I responsive") -->

# Project Overview

Welcome,

This is Hygge Houseplants e-commerce website, a full-stack (django) site for plant lovers to shop plants for their homes. They will also be able to view what movies other members have been watching. This is Rachel Luke's submission for Code Institute's Fullstacks Frameworks with Django (i.e., Milestone 4).

The following are high-level details of this project:

- This is a Django project backend using a relational database that allows users to store and manipulate data entries (i.e., their plant product purchases).
- The main technologies used are HTML, CSS, JavaScript, Python+Django, PostgreSQL and Stripe Payments.
- User functionality is intuitive to users (to create, locate, display, edit and delete records).
- The site has a main navigation in the header and a structured layout.
- Git & GitHub are used for version control.
- Any external code sources used in the project are clearly identified in the code itself and in this README.md file
- The final version has been deployed via GitHub Pages.
- There are no passwords or secret keys in the project repository.

The last update to this file was: **February 21st, 2025**

\
 &nbsp;

# Table of Contents

- [Hygge Houseplants](#hygge-houseplants)
- [Project Overview](#project-overview)
- [Table of Contents](#table-of-contents)
- [UX](#ux)
  - [User Stories](#user-goals-stories)
- [UI / Design Choices](#ui-design-choices)
  - [Moodboard](#moodboard)
  - [Fonts](#fonts)
  - [Icons](#icons)
  - [Wireframes](#wireframes)
  - [Mockups](#mockups)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Features - to be implemented](#future-features)
- [Technologies used](#technologies-used)
  - [Languages](#languages)
  - [IDE](#ide)
  - [Libraries & Framework](#libraries-framework)
  - [Tools](#tools)
- [Relational Database Management](#relational-database-management)
  - [Model Plan](#model-plan)
  - [Models](#models)
- [Validating](#validating)
- [Testing](#testing)
  - [Testing User Stories](#testing-user-stories)
  - [Django Tests](#django-tests)
  - [Debugging](#debugging)
  - [Unfixed bugs](#unfixed-bugs)
- [Deployment](#deployment)
  - [Heroku](#heroku)
  - [How to Run this Project Locally](#how-to-run-this-project-locally)
- [Credits](#credits)

\
 &nbsp;

# UX

## User Stories

At the planning stage of this project, stories for three roles: Site User, Shopper and Admin were created.
These stories are grouped within 5 stages: (1) Viewing and Navigation, (2) Registration and User Accounts, (3) Sorting and Searching, (4) Purchasing and Checkout, and (5) Admin and Store Management.

Below, is a screenshot of the spreadsheet listing the Site User, Shopper and Admin stories:
![Stories](static/docs/hygge-houseplants-stories.jpg)

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

# UI / Design Choices

## Moodboard and Colour Palette

One of the first milestones of this project was to create a moodboard to help envision the overall house style of the website and ensure that all of the sections and elements are cohesive. The software I used to create the moodboard for this website is [Mila Note](https://milanote.com/ "Mila Note"). It also contains the hex codes of the chosen colour palette.

Below, is the moodboard and colour palette:
![Moodboard](static/docs/moodboard-and-color-palette.jpg)

## Fonts

- In order to engender an aestetic website, and move away from the basic fonts available, I have used [Google Fonts](https://fonts.google.com/ "Google Fonts") to find a text that best suits the feel of the website.
- For the page headers, I decided to use [Gelasio](https://fonts.google.com/specimen/Gelasio "Gelasio font"). This font stands out of the fresh and clean looks and contrasts with the other sans serif fonts.
- For the header navigation links, along with the logo, I have chosen [Figtree](https://fonts.google.com/specimen/Figtree "Figtree") as this sans-serif font reads cleanly for both lower and upper cases.
- For the body text, [Hind](https://fonts.google.com/specimen/Hind "Hind") as it is clear to read and it is minimalistic.

Additional Notes:

- I have intentionally imported the fonts in the css file and not the html files as it saved some space in the html file and as this is a static website, the slightly longer loading time is not critical.

- Backup fonts (sans-serif) have been put in place as a safety net, in case the custom fonts used are not available.

- There is a 'double reset' in the css file. It simplifies calculate rem unit as I no longer need to think in scale factor of 1.6 but 10 instead.

## Icons

During testing, the console indicated that an icon from Favicon was required as the 'logo' symbol for the browser tab. As a fitting icon, I downloaded and incoporated the film icon from [Favicon](https://favicon.io/ "Favicon").

## Breakpoints

As a starting point, I will be building my website with a mobile first mindset using the iPhone 5/SE (320px) as the smallest screen size for styling to look good on. The screen size breakpoints that I will be using are from [Bootstrap breakpoints](https://getbootstrap.com/docs/5.0/layout/breakpoints/ "Bootstrap").

| Screen Size | Class Infix | Breakpoint |
| ----------- | ----------- | ---------- |
| x-small     | none        | <576px     |
| small       | sm          | => 576px   |
| medium      | md          | => 768px   |
| large       | lg          | => 992px   |
| x-large     | xl          | => 1200px  |

\
&nbsp;
[Back to Top](#table-of-contents)
\

## Wireframes

I have used [Balsamiq](https://balsamiq.com/wireframes/ "Balsamiq") to develop my wireframes for my website. I initially created the mobile version and then the wireframes and then scaled it up for desktop. The website has 3 pages that are all scrollable and displays/hides sections with logic in lieu of having even more HTML pages to decrease inconvenient reloading of entire website.

The wireframes are below:

I have used [Balsamiq](https://balsamiq.com/wireframes/ "Balsamiq") to develop my wireframes for my website. I initially created the mobile version and then the wireframes and then scaled it up for desktop.

The wireframes are located below:

[Landing Page - Mobile & Desktop Wireframes](static/docs/wireframes/wireframe-landing-mobile-desktop.png "home mobile and desktop wireframes")

[Product Page - Mobile & Desktop Wireframes](static/docs/wireframes/wireframe-product-mobile-desktop.png "product mobile and desktop wireframes")

[Single Product Page - Mobile & Desktop Wireframes](static/docs/wireframes/wireframe-product-focus-mobile-desktop.png "single product mobile and desktop wireframes")

[Basket Page - Mobile & Desktop Wireframes](static/docs/wireframes/wireframe-basket-mobile-desktop.png "basket mobile and desktop wireframes")

[Checkout Page - Mobile & Desktop Wireframes](static/docs/wireframes/wireframe-checkout-mobile-desktop.png "checkout mobile and desktop wireframes")

[Authentication Page - Mobile & Desktop Wireframes](static/docs/wireframes/wireframe-authentication-mobile-desktop.png "authentication mobile and desktop wireframes")

[Account Page - Mobile & Desktop Wireframes](static/docs/wireframes/wireframe-account-mobile-desktop.png "account mobile and desktop wireframes")

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Mockups

Based on the wireframes, I created mockups using [Figma](https://www.figma.com/ "Figma") to help me plan the interface design. Mockups for both mobile and desktop have been created as part of the website design phase, and can be viewed via this link [Mockups](https://www.figma.com/design/DhvQKsOvO6ar8RNbsWME8C/Project-4?node-id=0-11 "Mockups").

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

# Technologies used

## Languages

- [HTML](https://en.wikipedia.org/wiki/HTML "HTML")

- [CSS](https://en.wikipedia.org/wiki/CSS "CSS")

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript "JavaScript")

- [Python](<https://en.wikipedia.org/wiki/Python_(programming_language)> "Python")

## IDE

- [GitPod](https://www.gitpod.io/ "GitPod")

## Libraries & Framework

- [Google Fonts](https://fonts.google.com/ "Google Fonts")

- [Font Awesome library](https://fontawesome.com/ "Font Awesome")

- [Favicon](https://favicon.io/ "Favicon")

- [Django](https://www.djangoproject.com/ "Django")

- [PostgreSQL](https://www.postgresql.org/ "PostgreSQL")

- [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/ "BootStrap 4")

## Tools

- [Mila Note](https://milanote.com/ "Mila Note")

- [Balsamiq](https://balsamiq.com/wireframes/ "Balsamiq")

- [CI Full Template](https://github.com/Code-Institute-Org/ci-full-template "CI Full Template")

- [Am I Responsive](https://ui.dev/amiresponsive "Am I Responsive")

- [Tables Generator](https://www.tablesgenerator.com/markdown_tables "Tables Generator")

- [DrawSQL](https://drawsql.app/ "DrawSQL")

- [TempMail](https://temp-mail.org/ "TempMail")

- [W3C HTML Validation Service](https://validator.w3.org/ "W3C HTML")

- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/ "W3C CSS")

- [W3C JS Validation Service](https://jshint.com "JSHint JS")

- [Python PEP8 checker](https://www.codewof.co.nz/style/python3/ "Python PEP8 checker")

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

# Relational Database Management

## Model Plan

The first design phase of the database models was mapped out using [DrawSQL](https://drawsql.app/ "DrawSQL"), which is a database design tool for creating scheme diagrams. Below is the model plan designed with DrawSQL:
![DrawSQL Plan](static/docs/drawSQL.png)

## Models - Product App

### Category Model

| Primary Key | Name             | User Friendly Name |
| ----------- | ---------------- | ------------------ |
| 1           | cacti_succulents | Cacti & Succulents |
| 2           | hanging_trailing | Hanging & Trailing |
| 3           | foliage_fern     | Foliage & Fern     |
| 4           | tropical         | Tropical           |

- This model contains the Category name (required field, returned by string method) and user friendly name.

- The Category name is also the field connects the Category Model and Product Model, where each Product object is connected with a Category name.

### Product Model

| Primary Key | Product Name     | Species                 | Description | Sale? | Price | Sale Price | Category | Rating | Image            | Image URL | Care Level | Light Level | Pet Friendly? |
| ----------- | ---------------- | ----------------------- | ----------- | ----- | ----- | ---------- | -------- | ------ | ---------------- | --------- | ---------- | ----------- | ------------- |
| 1           | Aloe Vera        | Aloe barbadensis miller |             | No    | 16.50 |            | 1        | 4.1    | aloevera.png     |           | 3          | 3           | No            |
| 2           | Golden Pothos    | Epipremnum aureum       |             | No    | 10.99 |            | 2        | 4.7    | goldenpothos.png |           | 2          | 1           | No            |
| 3           | Spider Plant     | Chlorophytum Comosum    |             | No    | 9.50  |            | 2        | 3.9    | spiderplant.jpg  |           | 1          | 2           | Yes           |
| 4           | Boston Fern      | Nephrolepis exaltata    |             | No    | 12.00 |            | 3        | 4.6    | bostonfern.png   |           | 2          | 2           | Yes           |
| 5           | Bird of Paradise | Strelitzia Nicolai      |             | Yes   | 18.99 |            | 4        | 4.2    | birdparadise.png |           | 1          | 3           | No            |
| 6           | Peace Lily       | Spathiphyllum wallisii  |             | Yes   | 12    | 10.50      | 4        | 4.8    | peacelily.png    |           | 3          | 1           | No            |

- This model returns the string Product Name.

- The required fields are Product Name, Description and Price.

- The Product ID is the primary key that is passed through for (all users) to add/modify/delete in bags and (for superusers) to edit/delete products.

### Plant Care Level Model

| Primary Key | Name        | User Friendly Name |
| ----------- | ----------- | ------------------ |
| 1           | low_care    | Unkillable         |
| 2           | medium_care | Easy to take care  |
| 3           | high_care   | Needs a lot of TLC |

- This model's fields are assigned to each Product object.

### Plant Light Level Model

| Primary Key | Name         | User Friendly Name |
| ----------- | ------------ | ------------------ |
| 1           | low_light    | Low Light          |
| 2           | medium_light | Medium Light       |
| 3           | high_light   | Bright Light       |

- This model's fields are assigned to each Product object.

### Discount Code Model

| Primary Key | Code          | Discount % | Description                | Active? | Validity Start Datetime | Validity End Datetime |
| ----------- | ------------- | ---------- | -------------------------- | ------- | ----------------------- | --------------------- |
| 1           | WELCOME15     | 15         | New Members Discount       | Yes     | 01/04/2024 00:00:00     | 01/04/2025 00:00:00   |
| 2           | pRL29Akc04    | 10         | Student Discount           | Yes     | 11/12/2024 00:00:00     | 11/02/2024 00:00:00   |
| 3           | BLACKFRIYAY25 | 25         | Black Friday 2024 Discount | No      | 28/11/2024 00:00:00     | 30/11/2024 00:00:00   |

- This model contains the Discount Code (required field, returned by string method) and Discount%, Discription (required), Active?, Validity Start (required field), Validity End (required field)

## Models - Profiles App

### UserProfile Model

| User | Phone Number | Country        | Street Address 1 | Street Address 2 | Town or City | County    | Postcode |
| ---- | ------------ | -------------- | ---------------- | ---------------- | ------------ | --------- | -------- |
| rL07 | 383920239    | United Kingdom | 23 Clark Suites  | Merridian Way    | Manchester   | Stockport | MA7 6NF  |

- This user profile model is for maintaining default delivery information and order history (cascaded through to Order Model by User field).

## Models - Checkout App

### Order Model

| Order Number                     | User Profile | Date                      | Full Name | Email            | Phone Number | Country        | Postcode | Town or City | Street Address 1 | Street Address 2 | County     | Delivery Cost | Order Total | Grand Total | Original Bag | Stripe PID                  |
| -------------------------------- | ------------ | ------------------------- | --------- | ---------------- | ------------ | -------------- | -------- | ------------ | ---------------- | ---------------- | ---------- | ------------- | ----------- | ----------- | ------------ | --------------------------- |
| FF682CD74CF448A9A3B7E58F6BAFF3D5 | rL07         | Feb. 21, 2025, 10:54 a.m. | Betsy     | betsy6@gmail.com | 5673255      | United Kingdom | MA7 6NF  | Stockport    | 23 Clark Suites  | Merridian Way    | Manchester | 0.00          | 49.50       | 49.50       | {"9": 3}     | pi_3QutrxF9uUBrkCny2Tgvv7ke |
|                                  |              |                           |           |                  |              |                |          |              |                  |                  |            |               |             |             |              |                             |
|                                  |              |                           |           |                  |              |                |          |              |                  |                  |            |               |             |             |              |                             |

- This model contains the Order Number (random generated 32-bit string), User Profile (username field cascaded from the UserProfile model), Date (date+time), Full Name (required), Email (required), Phone Number (required), Country (required, drop-down select), Postcode, Town or City (required), Street Address 1 (required), Street Address 2, County, Delivery Cost (read-only), Order total (read-only), Grand total (read-only), Original bag (product pk: quantity) and Stripe PID (read-only).

### OrderLineItem Model

| Product   | Quantity | Line Item Total | Delete? |
| --------- | -------- | --------------- | ------- |
| Aloe Vera | 3        | 49.50           | False   |

- This model is linked with the Order Model (the order number gets cascaded).

- The fields are Product (product name), quantity, line item total (read-only), delete? (boolean).

- This model enables admin to be able to adjust a customer's order if required post-order.

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

# Deployment

## Heroku

This project was deployed via Heroku, using the following steps:

1. Log in Heroku website, create a new app
2. Go to Settings and add the following Config Vars:

- DATABASE_URL: Enter Postgres URL postgres://EXAMPLE-POSTGRES-URL
- IP: 0.0.0.0
- PORT: 5000
- SECRET_KEY: XXXX
- CLOUDINARY_URL: cloudinary://XXX
- CL_API_KEY: XXX
- CL_SECRET: XXX
- DEBUG: TRUE (before launch, change to FALSE)
- DEVELOPMENT: TRUE (before launch, change to FALSE)
- DISABLE_COLLECTSTATIC: 1
- EMAIL_HOST_PASS: XXX
- EMAIL_HOST_USER: XXX@X.COM
- STRIPE_PUBLIC_KEY: pk_test_XXX
- STRIPE_SECRET_KEY: sk_test_XXX
- STRIPE_WH_SECRET: whsec_XXX

3. In the 'Deployment method' section, connect to GitHub (and also Enable Automatic Deploys).
4. Run in console: (`python3`)
5. In console, import Postgres database: (`from hygge_houseplants import db`) and then (`db.create_all()`).
6. Deploy the website. This link is [Hygge Houseplants - Heroku](https://ms4-hygge-houseplants-727aa19c949d.herokuapp.com/).
7. If any changes were required, they could be implemented, commited and pushed to GitHub and the changes would automatically be updated and deployed.

## How to Run this Project Locally

To work on this project within your local IDE such as VSCode, Pycharm etc:

1. Follow this link to the [Project GitHub repository](https://github.com/rachelcluke/hygge-houseplants "Project GitHub respository")
2. Under 'Code', copy the Clone URL for the repository.
3. In your local IDE, open a terminal.
4. Navigate into the desired working directory.
5. Type `git clone` and then paste the URL you copied in Step 2.
6. Hit Enter and your local clone will be created.
7. Within your project, in a terminal run `pip install -r /path/to/requirements.txt`.
8. Create an env.py file within the project folder and include the name of this file in your .gitignore file before committing.
9. Within your env.py file, add and modify the following:

   - `import os`
   - `os.environ["envpy_test"] = "envpy"`
   - `os.environ["DATABASE_URL"] = "postgresql://XXX"`
   - `os.environ["DEVELOPMENT"] = "TRUE"`
   - `os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY`
   - `os.environ["EMAIL_HOST_USER"] = "YOUREMAIL@.COM"`
   - `os.environ["EMAIL_HOST_PASS"] = "EMAIL SECURITY PASS"`
   - `os.environ["STRIPE_PUBLIC_KEY"] "pk_test_XXX" `
   - `os.environ["STRIPE_SECRET_KEY"] = "sk_test_XXX" `
   - `os.environ["STRIPE_WH_SECRET"] = "whsec_XXX" `
   - `os.environ["CL_API_KEY"] = "XXX" `
   - `os.environ["CL_SECRET"] = "XXX"`
   - `os.environ["USE_CLOUDINARY"] = "TRUE"`

For further reference on cloning a respository from GitHub, click [here.](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository "Cloning a repository")

For further reference on creating an email host pass, click [here.](https://help.referral-factory.com/en/articles/9782920-how-to-set-up-your-own-email-server-using-gmail "Set up Gmail server")

For further reference on creating a Stripe Keys, click [here.](https://docs.stripe.com/keys "Stripe Dev Documentation")

For further reference on creating and storing Cloudinary keys, click [here.](https://dev.to/spymonk/integrating-cloudinary-storage-with-django-4ipb "Cloudinary Integration")

&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

# Credits

For mentoring, code advising and project reviewing:

- [Simen Daehlin](https://github.com/Eventyret "Simen Daehlin")

For technical support and guidance:

- [Tutors at Code Institute](https://codeinstitute.net/blog/meet-our-support-teams/ "Code Institute Support")

For content and design inspiration:

- [Beards and Daisies](https://www.beardsanddaisies.co.uk/ "Beards and Daisies")

- [The Little Botanical](https://thelittlebotanical.com/ "The Little Botanical")

- [Quirky Plants](https://www.quirkyplants.co.uk/ "Quirky Plants")

\
&nbsp;

Finally, a big shoutout to my family, friends and loved ones for their unwavering encouragement and support.

---

\
&nbsp;

Thank you all, from Rachel Luke.

\
&nbsp;
[Back to Top](#table-of-contents)
