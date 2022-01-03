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

[Balsamiq](https://balsamiq.com/wireframes/) was used to create the wireframes for this project. As the creation of the wireframes was carried out before the project development started, it does not have all the views and pages and may slightly vary from the final webstie version.

[Wireframes](media/readme_images/wireframes/wireframes_hello_ireland.pdf)
## User stories

### Viewing and Navigation

1. As a Customer I want to be able to see the full list of all products in order to select single products to purchase.

2. As a Customer I want to be able to view individual product details so that I can see the image in a higher resolution by opening it in a new window, identify the price, product rating, description, available sizes.

3. As a Customer I want to be able to see the grand total of my order at any time so that I can decide whether to buy more products or remove some from the basket.

4. As a Site User I want to be able to find some information about the website.

### Registration and User Accounts

5. As a Site User I want to be able to easily register for an account so that I can have a personal account and to be able to view my profile.

6. As a Site User I want to be able to easily login and logout so that I can access my personal information.

7. As a Site User I want to be able to esasily recover password so that I can get access to my account.

8. As a Site User I want to be able to receive an email confirmation after registering in order to verify that my account registration was successful.

9. As a Site User I want to be able to have a personalized user account so that I can view my personal order history, save my payment details.

### Sorting and Searching

10. As a Shopper I want to be able to sort the list of available products in order to identify the best-priced, alphabetically and categorically sorted products.

11. As a Shopper I want to be able to sort a specific category of products in order to identify the best-priced product in a selected category, sort products in that category by name.

12. As a Shopper I want to be able to search for a product by name, location or description	in order to find a specific product I'd like to purchase.

13. As a Shopper I want to be able to see what I've searched for in the search result and the number of my search results in order to quickly decide whether the product I need is available.

### Purchasing and Checkout

14. As a Shopper I want to be able to easily select the quantity of the products I want to purchase	so that I can add the correct product and its quantity to my shopping bag.

15. As a Shopper I want to be able to view items in my shopping bag	so that I can identify the total cost of my order and the items I have ordered.

16. As a Shopper I want to be able to adjust the quantity of a particular item in my shopping bag so that I can easily make changes to my order before checkout.

17. As a Shopper I want to be able to easily submit my payment details in order to checkout effectively.

18. As a Shopper I want to be assured that my personal and payment information is safe and secure so that I can confidently provide information that is needed to complete a purchase.

19. As a Shopper I want to be able to view an order confirmation after checkout	so that I can verify that the order is correct.

20. As a Shopper I want to be able to receive an email confirmation after checkout in order to have a copy of the order confirmation for my records.

### Admin and Store Management

21. As a Store Owner I want to be able to add a new product so that I can add new items to my shop.

22. As a Store Owner I want to be able to edit a product so that I can change product criteria such as price, description, image etc..

23. As a Store Owner I want to be able to delete a product so that I can remove items that are no longer on sale.

### Reviews and Ratings

24. As a Site User I want to be able to see reviews of products from other users in order to quickly decide whether this particular image is worth the purchase.

25. As a Site User I want to be able to leave a review or several reviews on a specific product in order to quickly and easily share my opinion and impression of the given product.

26. As a Site User I want to be able to delete my own review/reviews I have ever left on the website so that I can easily delete the information I personally shared about a specific product.

### Favourite Products

27. As a Shopper/Site User I want to be able to add images that I liked to my favourites in order to quickly and easily find them in the future (e.g. save an image for a later purchase or review).

28. As a Shopper/Site User I want to be able to view images that I marked as my favourites so that I can proceed to purchase them.

29. As a Shopper/Site User I want to be able to remove images that I no longer want to be marked as My Favourites so that I can easily manage My Favourites section of my account.

## **[BACK TO TOP](#content-quick-links)** *
<hr style="height:5px;border-width:0;color:gray;background-color: #eca50b">

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


# TESTING

Click here for the detailed [Testing Information](https://github.com/olga-od-ua/hello_ireland/blob/main/TESTING.md)


