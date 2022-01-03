# TESTING.md

# CONTENT QUICK LINKS
## [User Stories](#user-stories-testing)
## [Validation](#code-validation)
## [Manual Tests](#manual-testing)
## [Automated Tests](#automated-testing)
## [Authenticaton](#user-authentication)
## [Forms](#form-validation)
## [Shopping Bag](#shopping-bag)
## [Checkout](#checking-out)
## [Email](#emails)
## [Modals](#modal-testing)
## [CRUD](#crud-testing)
## [Bugs](#bugs-test)
## [RETURN TO README](https://github.com/olga-od-ua/hello_ireland/blob/main/README.md)

## User stories testing:

### Viewing and Navigation

1. As a Customer I want to be able to see the full list of all products in order to select single products to purchase.

2. As a Customer I want to be able to view individual product details so that I can see the image in a higher resolution by opening it in a new window, identify the price, product rating, description, available sizes.

3. As a Customer I want to be able to see the grand total of my order at any time so that I can decide whether to buy more products or remove some from the basket

### Registration and User Accounts

4. As a Site User I want to be able to easily register for an account so that I can have a personal account and to be able to view my profile.

5. As a Site User I want to be able to easily login and logout so that I can access my personal information.

6. As a Site User I want to be able to sasily recover password so that I can get access to my account.

7. As a Site User I want to be able to receive an email confirmation after registering in order to verify that my account registration was successful.

8. As a Site User I want to be able to have a personalized user account so that I can view my personal order history, save my payment details.

### Sorting and Searching

9. As a Shopper	I want to be able to sort the list of available products in order to identify the best-priced, alphabetically and categorically sorted products.

10. As a Shopper I want to be able to sort a specific category of products in order to identify the best-priced product in a selected category, sort products in that category by name.

11. As a Shopper I want to be able to search for a product by name, location or description	in order to find a specific product I'd like to purchase.

12. As a Shopper I want to be able to see what I've searched for in the search result and the number of my search results in order to quickly decide whether the product I need is available.

### Purchasing and Checkout

13. As a Shopper I want to be able to easily select the quantity of the products I want to purchase	so that I can add the correct product and its quantity to my shopping bag.

14. As a Shopper I want to be able to view items in my shopping bag	so that I can identify the total cost of my order and the items I have ordered.

15. As a Shopper I want to be able to adjust the quantity of a particular item in my shopping bag so that I can easily make changes to my order before checkout.

16. As a Shopper I want to be able to easily submit my payment details in order to checkout effectively.

17. As a Shopper I want to be assured that my personal and payment information is safe and secure so that I can confidently provide information that is needed to complete a purchase.

18. As a Shopper I want to be able to view an order confirmation after checkout	so that I can verify that the order is correct.

19. As a Shopper I want to be able to receive an email confirmation after checkout in order to have a copy of the order confirmation for my records.

### Admin and Store Management

20. As a Store Owner I want to be able to add a new product so that I can add new items to my shop.

21. As a Store Owner I want to be able to edit a product so that I can change product criteria such as price, description, image etc..

22. As a Store Owner I want to be able to delete a product so that I can remove items that are no longer on sale.

### Reviews and Ratings

23. As a Site User I want to be able to see reviews of products from other users in order to quickly decide whether this particular image is worth the purchase.

24. As a Site User I want to be able to leave a review or several reviews on a specific product in order to quickly and easily share my opinion and impression of the given product.

25. As a Site User I want to be able to delete my own review/reviews I have ever left on the website so that I can easily delete the information I personally shared about a specific product.

### Favourite Products

26. As a Shopper/Site User I want to be able to add images that I liked to my favourites in order to quickly and easily find them in the future (e.g. save an image for a later purchase or review).

27. As a Shopper/Site User I want to be able to view images that I marked as my favourites so that I can proceed to purchase them.

28. As a Shopper/Site User I want to be able to remove images that I no longer want to be marked as My Favourites so that I can easily manage My Favourites section of my account.

## **[BACK TO TOP](#content-quick-links)** *
<hr style="height:2px;border-width:0;color:gray;background-color: #eca50b">

## Code Validation:

### **Html**:

![Html validation](media/readme_images/validation/HTML_validation.png)
HTML code of the website passed the validation without major errors or warnings. The "Bad value https://fonts.googleapis.com/css?family=Lora:400,700|Montserrat:300 for attribute href on element link: Illegal character in query: | is not allowed." error cannot be fixed as it is a required format by Google Fonts.

The "The type attribute is unnecessary for JavaScript resources." warning was left unchanged as it is has a vital role in the code. 

The error "“Element li not allowed as child of element nav in this context” which was fixed by wrapping each <li> element of the mobile-top-header.html in a <ul> unordered list.

### **CSS**:

![CSS validation](media/readme_images/validation/CSS_validation.png)
All the CSS code passed the validation as shown on the screenshot above.

During the code review it was noticed that the css code for styling of the checkout form fields was located in the project-level base.css file. It was moved to checkout.css.

### **PEP8 Compliance**:

All code was checked for valid indentation, whitespace, blank line space and line length using 
the [PEP8 validator](http://pep8online.com/).

### **Javascript Validation**:

All Javascript code was validated using [Jshint validator](https://jshint.com/). All JavaScript code passed the validation without any major warnings or errors. A few missing semicolons were added and a few unnecessary ones were removed.

## **[BACK TO TOP](#content-quick-links)** *
<hr style="height:5px;border-width:0;color:gray;background-color: #eca50b">

## Manual Testing:

### Responsive Design: 
For this project I decided to use [Bootstrap](https://getbootstrap.com/). Its grid system allows for excellent responsive designs. I used [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) to check how my application was looking on all screen sizes and adjusted as necessary. I had to use minimal media queries in my css code.

### Call to action buttons:
I checked and rechecked all buttons were working on all devices and were leading to the correct sections of the website. It was also important that I laid out 
my CTA choices in order of priorty.

### External links:
I made sure to check that all links and social media links were directed to the correct URLS and also that my target="_blank" attribute was working. 
All external links open in a new browser tab.

### Internal links:
I made sure to check that all interal links were working correctly to ensure they led to the correct destinations and that there were no broken links. I also checked that using browser back and forward buttons did not cause any errors or break the website.

### Lighthouse performance test:
![Lighhouse test](wireframes/lighthouse.png)

I used Lighthouse in Chrome devtools to test my website's performance.
I increased my SEO scores by adding meta content for seo description.
I found that testing with lighthouse generated higher scores in incognito mode due to browser caching.

### Accessibility:

![Accessiblity test](wireframes/accessibility.png)

I used [a11y](https://color.a11y.com/) to make sure my color contrasts between fonts and backgrounds was acceptable without excessively comprising my vision of the website final design.

## **[BACK TO TOP](#content-quick-links)** *
<hr style="height:5px;border-width:0;color:gray;background-color: #eca50b">

## Automated Testing



![Automated Test](ADD)


## **[BACK TO TOP](#content-quick-links)** *
<hr style="height:5px;border-width:0;color:gray;background-color: #eca50b">

## User Authentication:
I carried out exstensive testing to make sure no user error caused the site to malfunction. To achieve this I would check all urls available to non logged in and logged in users and manually change them in the browser. I got the following results: 

1. **Changing to a url that does not exists**: 
If a user attempts to change the website's path to a non-existing one they will receive a standard 404 error which lets the user know there is no such page.

![404 error](!!!ADD screenshot)

2. **Changing a user url to an admin url**:
While logged in or authenticated if a user tries to change a url to a url that only admin can access. They are given a warning message that "Only admin can do that!".

![Authentication](!!! ADD )

3. **Adding Reviews and Adding to Favourites**:
Any action that requires a user to be authenticated will guide them to the sign up form. The login decorator and templating syntax has been used to achieve user authentication.



### Features Available To Non Registerd Users:

### Features Only Available to Admin:

## **[BACK TO TOP](#content-quick-links)** *
<hr style="height:5px;border-width:0;color:gray;background-color: #eca50b">

## Form Validation:

## **[BACK TO TOP](#content-quick-links)** *
<hr style="height:5px;border-width:0;color:gray;background-color: #eca50b">

## Shopping Bag:

## **[BACK TO TOP](#content-quick-links)** *
<hr style="height:5px;border-width:0;color:gray;background-color: #eca50b">

## Checking Out:


## **[BACK TO TOP](#content-quick-links)** *
<hr style="height:5px;border-width:0;color:gray;background-color: #eca50b">

## Emails:


### Modal Testing


## **[BACK TO TOP](#content-quick-links)** *
<hr style="height:5px;border-width:0;color:gray;background-color: #eca50b">

## CRUD Testing:

1. For the testing purposes a product without an image was added to the database. It displayed the noimage.png as the image as expected.  

## **[BACK TO TOP](#content-quick-links)** *
<hr style="height:5px;border-width:0;color:gray;background-color: #eca50b">



## **[BACK TO TOP](#content-quick-links)** *
<hr style="height:5px;border-width:0;color:gray;background-color: #eca50b">

## Bugs:

* It is known that there are still some minor responsive styling issues for unpopular screen sizes that are planned to be tackled in the future.

* During the testing of the Delete Product function the following error was encountered while trying to delete a product that was still in the shopping bag: "No Product matches the given query." The following Slack post helped to resolve the issue: https://code-institute-room.slack.com/archives/C7HS3U3AP/p1631708528269000 by clearing the site data in the Application Storage.

* There is a number of flake8 and pylint errors that were not resolved due to my lack of experience and knowledge (which is constantly improving), as well as time constraints and the complexity and potential affect on the functionality of the site.

* Rating field is still displayed and is editable in the Add Product form. Since the ratings are coming from user reviews, this field should not be editable by anyone (including the site admin). This will be taken care of in the future as the time did not allow to look into this issue closely.

* The toasts messages reappear from the previous action when the back browser button is clicked. It is planned in the future to implement a timeout function and ensure the message does not reappear.


### Not bugs but the room and notes for improvement.

* It is planned to prepopulate user's full name in the checkout form for authanticated users.




## **[BACK TO TOP](#content-quick-links)** *
<hr style="height:5px;border-width:0;color:gray;background-color: #eca50b">




