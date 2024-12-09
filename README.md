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

The last update to this file was: **December 9th, 2024**

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
  - [Colours](#colours)
  - [Media Queries](#media-queries)
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
  - [Debugging](#debugging)
  - [Unfixed bugs](#unfixed-bugs)
- [Deployment](#deployment)
  - [Heroku](#heroku)
  - [How to Run this Project Localy](#how-to-run-this-project-locally)
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

## Wireframes

I have used [Balsamiq](https://balsamiq.com/wireframes/ "Balsamiq") to develop my wireframes for my website. I initially created the mobile version and then the wireframes and then scaled it up for desktop. The website has 3 pages that are all scrollable and displays/hides sections with logic in lieu of having even more HTML pages to decrease inconvenient reloading of entire website.

The wireframes are below:

I have used [Balsamiq](https://balsamiq.com/wireframes/ "Balsamiq") to develop my wireframes for my website. I initially created the mobile version and then the wireframes and then scaled it up for desktop.

The wireframes are located below:

[Landing Page - Mobile & Desktop Wireframes](static/docs/wireframes/wireframe-landing-mobile-desktop.png "home mobile and desktop wireframes")

[Product Page - Mobile & Desktop Wireframes](static/docs/wireframes/wireframe-product-mobile-desktop.png "product mobile and desktop wireframes")

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

# Deployment

## Heroku 

This project was deployed via Heroku, using the following steps:

1. Log in Heroku website, create a new app
2. Go to Settings and add the following Config Vars:
  - DATABASE_URL: Enter Postgres URL postgres://XXX
  - IP: 0.0.0.0
  - PORT: 5000
  - SECRET_KEY: XXXX
3. In the 'Deployment method' section, connect to GitHub (and also Enable Automatic Deploys).
4. Run in console: (```python3```)
5. In console, import Postgres database: (```from my_mdb import db```) and then (```db.create_all()```).
6. Deploy the website. This link is [xxx](https://xxx.herokuapp.com/ "xxx").
7. If any changes were required, they could be done, commited and pushed to GitHub and the changes would automatically be updated and deployed.


# Credits

For content and design inspiration:

- [Beards and Daisies](https://www.beardsanddaisies.co.uk/ "Beards and Daisies")

- [The Little Botanical](https://thelittlebotanical.com/  "The Little Botanical")

- [Quirky Plants](https://www.quirkyplants.co.uk/ "Quirky Plants")

\
&nbsp;

---

\
&nbsp;

Thank you, from Rachel Luke.

\
&nbsp;
[Back to Top](#table-of-contents)