# Oh Hello Ireland

Oh Hello Ireland is an online store that sells unique images of Ireland. When buying an image the customer receives all the copyrights for that particular image. Currently images are broken down into 5 main categories: Buildings, Landscapes, Portraits, Ocean & Sealife and Wildlife.

Unlike other image stock online stores, Oh Hello Ireland sells images made by the best Irish photographers, meaning that all the objects in the images are presented through the eyes of true Irish people, reflecting their nature and culture.

## The live website can be viewed here: [Oh Hello Ireland](https://hello-ireland.herokuapp.com/)

![Oh Hello Ireland](media/readme_images/am_i_responsive.png)

# CONTENT QUICK LINKS
## [UX](#wireframes)
## [FEATURES](#implemented-features)
## [SITEMAP](#sitemap-layout)
## [DATABASE](#database-schema)
## [TECHNOLOGIES](#technologies-used)
## [TESTING](#testing)
## [DEPLOYMENT](#deployment)
## [CREDITS](#code-credits)
## [ACKNOWLEDGEMENTS](#acknowledgements)
## [DISCLAIMER](#disclaimer)

# Wireframes



# Implemented Features



- REVIEWS. Any Site User can leave a review (or several reviews) on any product. There is no editing available in order to capture the thoughts of that specific reviewer at the time of the review and avoid having users to edit minor details of their reviews thus confusing other Site Users with contradicting information. Users, however, are allowed to delete their own reviews entirely.

Every product details page displays all the reviews, the rating given at the time of the review, the review message, the date and the reviewer's username.

## Future Features

1. There is currently no sizes or dimensions information available, as well as no size or dimensions selection for an image available throughout the website. Due to time constraints these features have not been implemented yet and are planned to be implemented in the future. Frame sizes will become available when images can be sold in printed versions. It is also planned to display dimensions of digital images in the product details in the future.

NB: it was initially planned to have 5 different frame sizes (A1, A2, A3, A4 and A5) and this can be traced in the website development history, however this feature was not worked through thouroughly enough to be presented in the final website version.

2. Currently any authenticated user can leave a review for any product. As a future feature, it is planned to destinguish whether the reviewer bought the image they are reviewing in the past or whether they bought a different image or whether they have not made a purchase from the website yet.

3. Currently any authenticated user can leave as many reviews as they like. In the future it is planned to put some restrictions in place (e.g. only one review per product or allowing to only review products that the user had bought in the past).

4. As a future feature, it is planned to display all the reviews that a specific user left on the website on their account for their reference and management (i.e. deletion).

5. Once there is a considerable number of reviews on one page at a time (e.g. more than 10-15) it is planned to implement pagination or other feature to make the reviews part of the website more readable and intuitive.

6. Social links in the footer were added for visual purposes only and do not carry out any critical functionality. They are currently linked to the home page of the respective website. In the future they will be redirecting the user to the appropriate destination. 

7. Rating field will be removed from the Add a Product form and the ratings data will be taken from user reviews. As this feature is not implemented yet (once again due to time constraints), sorting by rating is not fully functioning. 

# TECHNOLOGIES USED

1. [Balsamiq](https://balsamiq.com/wireframes/)
    - This technology helped my visualize my website before starting to write any code, which made the development process a lot more structured and logical.

2. [HTML 5](https://en.wikipedia.org/wiki/HTML)
    - HTML was used as the main mark up language.

3. [CSS 3](https://en.wikipedia.org/wiki/CSS)
    - CSS 3 was used to style the elements and create a more visually appealing website.

4. [Javascript](https://www.javascript.com/)
    - Javascript was used to to extend functionality of Django framework features and create other interactive facets.

5. [Jquery](https://jquery.com/)
    - Jquery, same as JavaScript, was used to to extend functionality of Django framework features and create other short-hand interactive facets.

6. [Bootstrap 4.4.1](https://getbootstrap.com/docs/)
    - Bootstrap was used for quick and easy style and layout solutions.

7. [Font Awesome](https://fontawesome.com/)
    - Fontawesome was used for all the icons of the website for aesthetic and UX purposes.

8. [Gitpod](https://www.gitpod.io/)
    - Git pod was used as an IDE workspace to write and run all the code and its changes. Git was used as a version control to commit and push all the code to the respective GitHub repository.

9. [Github](https://github.com/)
    - GitHub was used for storage of all the commits and code back up.

10. [W3C HTML validator](https://validator.w3.org/)
    - W3C validation service was used to ensure all the HTML code passed the validation.

11. [W3C CSS validator](https://jigsaw.w3.org/css-validator/)
    - W3C validation service was used to ensure all the HTML code passed the validation.

12. [Jshint validator](https://jshint.com/)
    - Jshint was used to ensure all JavaScript code passed validation.

13. [PEP8 validator](http://pep8online.com/)
    - PEP8 online was used to ensure all python files pass PEP8 industry standards.

???15. [Lucid Chart](https://www.lucidchart.com/pages/)
* Lucid chart was used to create the sitemap.

???16. [db diagram](https://dbdiagram.io/home)
* Db diagram was used to create the database schema.

17. [PIP3](https://pip.pypa.io/en/stable/)
    - PIP3 was used to install all packaging tools.

18. [Am I responsive](http://ami.responsivedesign.is/)
    - 'Am I responsive' was used to create screenshots from four main types of devices to be displayed in the README file.

19. [Python3](https://www.python.org/download/releases/3.0/)
    - Python was used as the backend programming language.

20. [Django](https://www.djangoproject.com/)
    - Django was used as the framework for all the backend functionality. All the backend database data is injected into the html templates using django template tags.

21. [SQLite3](https://www.sqlite.org/index.html)
    - SQLite was used as the default relational database.

22. [Postgresql](https://www.postgresql.org/)
    - Postgresql was used as the database for the deployed Oh Hello Ireland Heroku app.

23. [Heroku](https://id.heroku.com/login)
    - Heroku was used as the hosting platform for this project.

24. [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
    - Chrome Developer Tools were used extensively during the development to ensure good responsiveness of the website and for debugging.

28. [Stripe](https://stripe.com/ie)
    - Stipe test API was used to take secure test payments from customers in the Checkout app.

29. [Amazon AWS](https://aws.amazon.com/)
    - Amazon AWS was used for hosting all the static files for the purposes of improving the site's performance and scalability.

30. [Cloudinary](https://cloudinary.com/)
    - Cloudinary was used for storing the full-sized products' images as well as the favicon image.

31. [Grammarly](https://app.grammarly.com/)
    - Grammarly was used to perform spellcheck across all project files.






![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome olga-od-ua,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
