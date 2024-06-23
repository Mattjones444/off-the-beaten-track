\# Off the Beaten Track Milestone 4 Full Stack Development Project

![Website Mock Up](/media/readme/mockup.jpg)

\# Purpose

This project is aimed at promoting a new adventure holiday activity service called [Off the Beaten Track]( **<https://leveluphealth-cd483f475adf.herokuapp.com/**), which aims to give people the opportunity to search for and book activities in a range of different countries.

The core purposes of the app:

\- Introduce users to the Off the Beaten Track holiday activity service.

\- Display a range of exciting activties in a range of destinations.

\- Help to make it easy for users to book activities on a trustworthy site.

\- To see reviews of adventurous activities and make better choices about the activities they're booking.

\- earn the professional credibility and confidence of the clients visiting the site.

The app is built using HTML, CSS, Django, Python and Postgres as a Milestone Project #4 for the Code Institute's Full Stack Developer course.  

[The live website is available here](https://leveluphealth-cd483f475adf.herokuapp.com/)

\_\_\_

\# UX Design

\## User stories

\### As a \*\*first time user\*\*

\- I want to easily understand the main purpose of the app and learn more about the services.

\- I want to be able to easily navigate and quickly find activities relevant to me.

\- I want to find ways to join the community and follow the company on different social media.

\- I want to find and easily book activities through the app.

\- I want to let other users know my opinion of the activities I have chosen.

\- I want to save my information and use it to make purchasing an activity easier next time.

\### As a \*\*returning\*\* and a \*\*frequent user\*\*

\- I want to see a variety of activities organised in different ways.

\- I want to write a review of my completed activity and see reviews on other user's activities.

\- I want to join the community.

\- I want to book further activities.

### All users want to be able to access and comfortably view the website on mobile devices.

\_\_\_

## Structure

### Home Page

\- Grabs the user's attention and grips it through the bold design and hero image.

\- Visual cues and text signals to the user the core purpose of the app.

\- Call to action button which takes users straight to the activity choices.

#### User Goal:

   - Understand the main purpose of the website.

   - Find quick links to get started.

   - Easily navigate and interact with the website.

#### Website Goal:

   - Quickly and clearly explain the service the app is selling.

   - Interest and engage the user.

   - Give users a direct link to the service being sold.

   - Initiate future engagement, such as following on social media and seeing special offers. 

### Activities Page

\- Provides the user with a range of activities across a variety of countries

\- Gives the user the ability to filter by activity type, rating, category, price or country. 

\- Gives the user the ability to search the site using the search bar. 

#### User Goal:

   - To easily find activities that are most relevant to me.

   - To see a range of activities in my price range, holiday destination or chosen activity type. 


#### Website Goal:

   - Provide users with a good selection of appealing activities to choose from to enable them to find something relevant to them.

   - Sell the activities and deliver and experience to the user. 

   - Convince the user to join the community and encourage them to book multiple times.

### Activities Detail Page

\- Allows the user to view more information about the activity they've chosen.

\- Users can choose a date and indicate the number of guest particpating in the activity. 


#### User Goal:

   - Get more information on the activity I have chosen.

   - See information on when activities are available.

#### Website Goal:

   - Provide a enticing descriptions of the activities to encourge users to book them.



\## Wireframes

\### \*\*Home\*\*

![Homepage-wireframe (full size)](/level_up/static/readme/homepage_desktop.png)

![Homepage-wireframe (full size)](/level_up/static/readme/homepage_mobile.png)

\### \*\*Dashboard\*\*

![Dashboard wireframe (full size)](/level_up/static/readme/dashboard_desktop.png)

![Dashboard wireframe (full size)](/level_up/static/readme/dashboard_mobile.png)

\### \*\*My Intentions\*\*

![My Intentions (full size)](/level_up/static/readme/myintentions_desktop.png)

![My Intentions (full size)](/level_up/static/readme/myintentions_mobile.png)

\_\_\_





\## Design

As Off the Beaten Track is a service, the app design shapes future brand recognition and styling, through bold colours and a unique look. The project's design springs from the ethos and values of Level_Up Health, as it is professional, new and fresh, which aims to give clients the feeling that the product is a new approach to leading a healthier life. It also engenders trust that the company will act in a professional manner regarding the product and service they are providing. 


\### Colour Scheme

![Palette](media/readme/colour-pallette.png)

The conventional, modern, solid colour palette choice serves to engender trust, academia and professionalism, whilst maintaining a modern feel. 

\#### \*\*Cerise\*\* 

represents boldness, confidence and a hint of style.

\#### \*\*Timberwolf grey\*\* 

Cool, neutral and calm to offset the Cerise. 

\#### \*\*Black\*\* 

Contasting with the Cerise. 

\#### \*\*Persian Green\*\*  

represents new opportunities and fresh growth. 

\### Typography

[Roboto](https://fonts.google.com/specimen/Roboto) was chosen for body text as it is light and easy to read.

\### Images

The images in this project were sourced from [Canva](https://canva.com/). They were specifically selected to correlate with the main website colour palette and increase the aesthetic impact of the design.

\### Visual Effects

\#### Shadows

As the Home Page consists of multiple colourful overlapping blocks, it was important to add volume and make the content easier to perceive so the viewer's eye doesn't have to focus on understanding spatial relationships between elements, which might be daunting. However, to provide better performance on mobile devices, it was implemented only for screens larger than 992px.


\#### Logo and Page Headings Gradient

Level_Up Health has a basic logo at the moment, which still needs further work as it was made purely for the purposes of this project. Work needs to be done to make it stand out further.  

\#### Buttons

Each button offers a similar growing effect described above combined with a change of its background colour: it is black by default, and it turns Persian Green when hovered over with a mouse. To provide better performance on mobile devices, it was implemented only for screens larger than 978px.

\#### Navbar Hover effect

The navbar includes a hover-over effect to make the experience more interactive and navigation more intuitive. When the user engages with the link or hovers over the link, its background colour changes to light brown to subtly highlight the item without compromising legibility.

\_\_\_

\# Features

\## Existing Features

\- \*\*Navigation bar\*\*

![navbar](/level_up/static/readme/navbar.png)


Each page has a full responsive navigation bar at the top. It includes the Logo (which is a link to the Home page), a search bar, 'My Account' icon compromising of a register and login option, for unauthenticated users. Authenticated users can select their profile information and site admins can add activities. It retains an identical layout throughout the website across all devices to ensure simple and intuitive navigation. The Navbar will allow the user to reach any section of the website from any point on the website without unnecessary steps and using browser navigation buttons.            


For mobile devices, it transforms into a compact "hamburger menu". This dropdown menu features the same items, displayed as a column on a semi-transparent background.  

The secondary navbar provides users with the ability to select activities based on price, rating, category, activity type and country. 


\- \*\*Hero image\*\*

![heroimage](/level_up/static/readme/heroimage.png)

This section is the first thing the user sees opening each page, it is an eye-catching image for aesthetical stimulation, which also helps to deliver the page's semantics as visual associations are commonly very strong. On the Home page, it also includes a call to action button taking users straight to the menu of activities.

\- \*\*Footer\*\*

![footer](/level_up/static/readme/footer.png)

The Footer contains the links to the social media and allows the user to continue engagement with the company on various platforms. 


\- \*\*Activities page\*\*

![activities](/assets/readme/successstories.png)

This page contains a large range of activities for users to browse and select,which can be accessed through filtering depending on their interests. Each activity card features a vivid, appealing image of the activity, encouraging the user to click on the card, a clear title for the activity and the location, country, price and rating. Users can filter these activities based on price, rating and category. They can also sort them by price (low-high and high-low), rating (low-high and high-low) and alphbetically. 

\- \*\*Activity Details page\*\*

![activity details](/level_up/static/readme/registration.png)

This page will allow the user to find out more about an activity they have selected. The image appears on the page, which matches the one the user has selected to maintain visual continuity. There is further information on the page around price, category, group size, duration and rating (featuring a link to the reviews section). Users can begin the purchasing process on this page by selecting how many guests will be participating in the activity and the date that they would like to book the activity for. The 'Add to Bag' button allows them to add this activity to thier basket.  


\- \*\*Reviews page\*\*

![activity details](/level_up/static/readme/registration.png)

This page is designed for users to add reviews of the activities they have booked. The title of the activity is displayed at the top of the page and the image associated with each activity also appears. There is a form for submitting a review, which includes encouraging users to give their name, star rating and a description of the review. This is then added to the review section at the bottom of the page. If there aren't currently any reviews, 'No reviews added' will display. 


\## Responsive layout

The site is designed to be flexible, fluid, responsive and aesthetically enjoyable on all screen sizes and resolutions starting from 378px. To ensure better performance on mobile devices, mobile versions (smaller in size with different aspect ratios) most of the hero images are in a smaller image format. It was considered necessary because the images play a significant role in delivering the semantics of the website and providing the intended user experience. 

![Responsiveness testing results:] [Excel](/level_up/static/readme/responsivenesstestingm3.xlsx), [Excel]]



\## Future Considerations

Users would benefit from date sensitive push notifications via the app that remind them, 24 hours before the due date, that they committed to completing that particular intention. Along with intentions in the My_intentions page that are ordered by due date. 

New features can be added to the dashboard to show users a visual representation of their progress.

To enable to app as a commercial prospect, users could gain free entry for a set period of time and then a payment feature could be added. 

Users would also benefit from identifying their fitness goals at the beginning of their journey and the app making reference to these goals as they complete intentions. 


\_\_\_

\# Technologies

\- HTML to accomplish the structure of the website.

\- CSS to style the website.

\- [Gitpod](https://www.gitpod.io/) IDE to develop the website.

\- [GitHub](https://GitHub.com/) to host the source code and GitHub Pages to deploy and host the live site.

\- Git to provide version control (to commit and push code to the repository). 

\- [FontAwesome](https://fontawesome.com/) v5.15.3 Icons.

\- [Google Fonts](https://fonts.google.com/) for typography.

\- [Google Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools) for debugging, inspecting pages' elements and testing layout.

\- [TinyJPG](https://tinyjpg.com/) to optimise images for readme. 

\- [Favicon.cc](https://www.favicon.cc/) to create the website favicon.

\- [Coolors](https://coolors.co/image-picker) to source colour palette from image.

\- [Balsamiq](https://balsamiq.com/wireframes/) to design wireframes.

\- Google Chrome's [Lighthouse](https://developers.google.com/web/tools/lighthouse) to assess accessibility.

\- [Screen Reader for Google Chrome](https://chrome.google.com/webstore/detail/screen-reader-for-google/nddfhonnmhcldcbmhbdldfpkbfpgjoeh/related?hl=en) to assess screen-reader accessibility.

\- Toptal [Colorfilter](https://www.toptal.com/designers/colorfilter/) to assess colour-blind accessibility.

\- [W3C HTML Markup Validator](https://validator.w3.org/) to validate HTML code.

\- [W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) to validate CSS code.

\- [Snyk Python Validator](https://snyk.io/code-checker/python/) to validate Python code.


\- Code Institute's Gitpod Template to generate the workspace for the project.

\_\_\_

\# Testing

\## User Story Testing

![User Testing results:] [Excel](/level_up/static/readme/usertestingm3.xlsx), [Excel]]

\## Feature Testing

All Features were tested manually, find the results below.

The website was tested in three browsers: Chrome, Firefox and Safari on Desktops, tablets and multiple mobile devices (macOS and Android).

![Features\_testing](/level_up/static/readme/featuretesting.xlsx)

![Features Testing results:] [Excel](/level_up/static/readme/featuretesting.xlsx), [Excel]]


\## Automated Testing

1\. \*\*[W3 Markup Validation](https://validator.w3.org/) - HTML Validation\*\*

All pages were run through HTML Validator. No errors were detected.

2\. \*\*[W3 Jigsaw](https://jigsaw.w3.org/css-validator/) - CSS Validation\*\*

CSS Stylesheet was run through CSS Validator. No errors were detected.

3\. \*\*[Synk](https://snyk.io/) - Python Validation\*\*

CSS Stylesheet was run through CSS Validator. No errors were detected.

4\. \*\*[Google Lighthouse](https://developers.google.com/web/tools/lighthouse)\*\*

\*\*Home Page\*\*

Mobile

![Mobile Home](/level_up/static/readme/lighthousehomepage_mobile.png)

Desktop

![Desktop Home](/level_up/static/readme/lighthousehomepage_desktop.png)

\*\*Dashboard Page\*\*

Mobile

![Mobile Success Stories](/level_up/static/readme/lighthousdashboard_mobile.png)

Desktop

![Desktop Success Stories](/level_up/static/readme/lighthousedashboard_desktop.png)

\*\*My Intentions Page\*\*

Mobile

![Mobile Signup](/level_up/static/readme/lighthousemyintentions_mobile.png)

Desktop

![Desktop Signup](/level_up/static/readme/lighthousemyintentions_desktop.png)

\## Accessibility Testing

\### Screen Reader for Goggle Chrome

The website was tested with [Screen Reader for Goggle Chrome](https://chrome.google.com/webstore/detail/screen-reader/kgejglhpjiefppelpmljglcjbhoiplfn?hl=en). No issues arose. 

\### Toptal Colorfilter

The website was tested with Toptal [Colorfilter](https://www.toptal.com/designers/colorfilter/) to make sure it is accessible for colour-blind users. No accessibility issues were detected.

[Result preview 1](https://www.toptal.com/designers/colorfilter?orig_uri=https://leveluphealth-cd483f475adf.herokuapp.com/&process_type=protan)

\_\_\_

\# Deployment

This project was hosted on Github. A repository was created by:

1\. Navigate to Github.com and login.

2\. On the left-hand sidebar, click the 'New' button.

3\. Name the repository and click on the 'Create Repository' button. 

During the creation of the project, the 'git add .', 'git commit -m', 'git push' and 'git pull' commands were used. 

This project was deployed to GitHub pages. The steps to deploy are as follows:

1\. Log into GitHub.

2\. Select `codeinstitute` from the list of repositories.

3\. Select `Settings` From the Repositories sub-headings.

4\. In the left side menu select `Pages`.

5\. Click on the link labelled 'Visit Site' to go to the live deployed page. This site is also deployed on Heroku.

\_\_\_

This project was deployed on Heroku by:

1\. In GitPod CLI, the root directory of the project, run:
    pip freeze --local > requirements.txt
    to create a requirements.txt file containing project dependencies.

2\. Create Procfile folder ensuring capital P in the route directory.
     - Enter web: python run.py within the file
     - Ensure you do not add a blank line to the end of the file as this can cause problems for deployment.

3\. Push your two 2 new files to your GitHub repository

4\. Login to Heroku, select Create new app, add the name of your app and select your nearest region.

5\. Go to the settings tab, click reveal config vars and input.

6\. Ensure NOTE to enter DEVELOPMENT and DB_URL from the env.py file as a Config Var. 

7\. Go to the “Deploy” tab of your app In the Deployment method section, select “Connect to GitHub

8\. Search for your repository 

9\. You now have the option to select 'Enable Automatic Deploys'

10\. Click deploy Main

11\. click the “More” button and select “Run console this is to migrate the tables from our database;
      - Type python3 into the console and click Run
      - from level_up import db
      - db.create_all()
      - exit()
      - Please note any additional changes will need to be migrated.

\# Credits


\## Media

\- all images were sourced from Canva.com

\- favicon.ico was created by me. 

\## Code

\- Guidance on HTML attributes and common conventions were obtained from [W3Schools](https://www.w3schools.com/) and [Mozilla's Web Documentation](https://developer.mozilla.org/en-US/).

\- Understanding of shadows was obtained from [W3Schools](https://www.w3schools.com/).

\## Acknowledgements

I would like to thank my mentor, Ronan McClelland, for his guidance and invaluable advice and sense of humour.