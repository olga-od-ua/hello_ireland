# TESTING.md

!NB: it is recommended to view the TESTING.md and README.md files in the GitHub Dark Theme turned on for distinct demarcation of the files' sections and screenshots. The Dark Theme can be turned on by going into your GitHub settings from the dropdown in the top right and then navigating to Appearance in the Account Settings from the menu on the left. Go to Theme Mode and select Single Theme (instead of the Sync with system) and then select a Dark Theme; refresh the page.

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
## [Bugs](#bugs-and-fixes)
## [RETURN TO README](https://github.com/olga-od-ua/hello_ireland/blob/main/README.md)

## User stories testing:

### Viewing and Navigation

1. As a Customer I want to be able to see the full list of all products in order to select single products to purchase.

- This can be achieved from the Home page by clicking on "GO TO IMAGES BUTTON", the castle image or by following the All Images link in the main menu. Back to All products button and other buttons returning the customer to the Products page are also extensively available across the website.

![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_1.png)

2. As a Customer I want to be able to view individual product details so that I can see the image in a higher resolution by opening it in a new window, identify the price, product rating, description, available sizes.

- This is achieved by either clicking on the image itself or by clicking on the DETAILS button.

![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_2.png)

3. As a Customer I want to be able to see the grand total of my order at any time so that I can decide whether to buy more products or remove some from the basket.

- This goal is achieved through the grand total that is displayed right next to the shopping basket icon on the navigation bar.

![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_3.png)

4. As a Site User I want to be able to find some information about the website.

- The User will see the About Us navigation bar link and will be able to navigate to the About Us page where they will be able to find the general information about the website, see its best reviews and the photographers whose images are for sale.

![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_4.png)

### Registration and User Accounts

5. As a Site User I want to be able to easily register for an account so that I can have a personal account and to be able to view my profile.

- This is achieved through the "Register" link in the navbar.

![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_5a.png)
![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_5b.png)

6. As a Site User I want to be able to easily login and logout so that I can access my personal information.

- Log in functionality is available in multiple views of the website with the main location being the navbar. Logout functionality is available from the navbar only.

![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_6a.png)
![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_6b.png)
![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_6c.png)
![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_6d.png)

7. As a Site User I want to be able to easily recover password so that I can get access to my account.

- This is achievable from the login view from any login link the user follows.

![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_7a.png)
![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_7b.png)

8. As a Site User I want to be able to receive an email confirmation after registering in order to verify that my account registration was successful.

- A confirmation email is sent upon successful registration and the user can confirm their email by following the link provided in the confirmation email.

![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_8a.png)
![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_8b.png)
![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_8c.png)

9. As a Site User I want to be able to have a personalized user account so that I can view my personal order history, save my payment details.

- This is also achievable after a successful registration and the profile can be accessed by a user through My Profile navbar link.

![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_9.png)

### Sorting and Searching

10. As a Shopper I want to be able to sort the list of available products in order to identify the best-priced, alphabetically and categorically sorted products.

- The user is able to sort products alphabetically, by category and by price (low to high and high to low) within All products.

![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_10.png)

11. As a Shopper I want to be able to sort a specific category of products in order to identify the best-priced product in a selected category, sort products in that category by name.

- The user is able to sort products alphabetically, by category and by price (low to high and high to low) within a specific category of products.

![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_11.png)

12. As a Shopper I want to be able to search for a product by name, location or description	in order to find a specific product I'd like to purchase.

- The user can use a search bar from the navigation menu in order to perform such a search.

![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_12.png)

13. As a Shopper I want to be able to see what I've searched for in the search result and the number of my search results in order to quickly decide whether the product I need is available.

- This is also achievable through the search bar from the navbar and the results of an example search can be found in the User story number 13.

### Purchasing and Checkout

14. As a Shopper I want to be able to easily select the quantity of the products I want to purchase	so that I can add the correct product and its quantity to my shopping bag.

- A User can select the quantity of the desired product from the product details page.

![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_14.png)

15. As a Shopper I want to be able to view items in my shopping bag	so that I can identify the total cost of my order and the items I have ordered.

- All this information can be found in the User's shopping bag which is reachable from the navbar as well as from the "Go to secure checkout" button from the messages.

![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_15.png)

16. As a Shopper I want to be able to adjust the quantity of a particular item in my shopping bag so that I can easily make changes to my order before checkout.

- Users can adjust the quantity of a particular size of a particular item with the help of the quantity input field and the Update and Remove buttons.

![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_16.png)

17. As a Shopper I want to be able to easily submit my payment details in order to checkout effectively.

- This is achievable through the "Secure checkout" button. The user will be redirected to the Shipping information form and the credit card input.

![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_17.png)

18. As a Shopper I want to be assured that my personal and payment information is safe and secure so that I can confidently provide information that is needed to complete a purchase.

- This is achieved by providing clear instructions to the User to fill out the checkout form and input the card details as well as providing a very detailed summary of the changes.

19. As a Shopper I want to be able to view an order confirmation after checkout	so that I can verify that the order is correct.

- The User will see an order confirmation summary upon successful checkout.

![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_19.png)

20. As a Shopper I want to be able to receive an email confirmation after checkout in order to have a copy of the order confirmation for my records.

- Such email is received upon successful checkout. Please see the screenshot below.

![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_20.png)

### Admin and Store Management

21. As a Store Owner I want to be able to add a new product so that I can add new items to my shop.

- This is achievable through the Add product form from the Product Management link on the navbar.

![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_21.png)

22. As a Store Owner I want to be able to edit a product so that I can change product criteria such as price, description, image etc.

- This is possible by clicking on the "Edit" buttons on either the Products view or the Product Details view.

![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_22a.png)
![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_22b.png)

23. As a Store Owner I want to be able to delete a product so that I can remove items that are no longer on sale.

- This is possible by clicking on the "Delete" buttons on either the Products view or the Product Details view. Same screenshots as in User Story number 22 apply.

### Reviews and Ratings

24. As a Site User I want to be able to see reviews of products from other users in order to quickly decide whether this particular image is worth the purchase.

- Reviews are displayed on each product details page.

![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_24.png)

25. As a Site User I want to be able to leave a review or several reviews on a specific product in order to quickly and easily share my opinion and impression of the given product.

- An authenticated user can leave a review by clicking on the "Add a Review" button which will redirect the User to the Review form.

![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_25.png)

26. As a Site User I want to be able to delete my own review/reviews I have ever left on the website so that I can easily delete the information I personally shared about a specific product.

- An authenticated User will be able to delete their reviews by clicking on the red "Delete Your Review" button. See screenshot for User Story number 24.

### Favourite Products

27. As a Shopper/Site User I want to be able to add images that I liked to my favourites in order to quickly and easily find them in the future (e.g. save an image for a later purchase or review).

- An authenticated User will be able to add any image to the list of their favourite images by clicking on the "Add to favourites" button from the Product Details view. Once the image is in their Favourites, the button switches to the "Remove from favourites" button.

![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_27a.png)
![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_27b.png)

28. As a Shopper/Site User I want to be able to view images that I marked as my favourites so that I can proceed to purchase them.

- An authenticated User will be able to see their Favourite images in My Favourites section via the relevant navbar link.

![See screenshot below](media/readme_images/UX_stories/UX_stories_testing/UX_story_28.png)

29. As a Shopper/Site User I want to be able to remove images that I no longer want to be marked as My Favourites so that I can easily manage My Favourites section of my account.

- An authenticated User will be able to remove images from the list of their Favourite images from the My Favourites section or from the relevant Product Details view by clicking on the "Remove from favourites" buttons. These buttons can be seen on screenshots for User Stories number 27 and 28.

## **[BACK TO TOP](#content-quick-links)** *
<hr style="height:2px;border-width:0;color:gray;background-color: #eca50b">

## Code Validation:

### **Html**:

![Html validation](media/readme_images/validation/HTML_validation.png)
HTML code of the website passed the validation without major errors or warnings. The "Bad value https://fonts.googleapis.com/css?family=Lora:400,700|Montserrat:300 for attribute href on element link: Illegal character in query: | is not allowed." error cannot be fixed as it is a required format by Google Fonts.

The "The type attribute is unnecessary for JavaScript resources." warning was left unchanged as it is has a vital role in the code. 

The error "Element li not allowed as child of element nav in this context" which was fixed by wrapping each list element of the mobile-top-header.html in an unordered list elements.

### **CSS**:

![CSS validation](media/readme_images/validation/CSS_validation.png)
All the CSS code passed the validation as shown on the screenshot above.

During the code review it was noticed that the css code for the styling of the checkout form fields was located in the project-level base.css file. It was moved to checkout.css.

### **PEP8 Compliance**:

All code was checked for valid indentation, whitespace, blank line space and line length using 
the [PEP8 validator](http://pep8online.com/).

### **Javascript Validation**:

All Javascript code was validated using [Jshint validator](https://jshint.com/). All JavaScript code passed the validation without any major warnings or errors. A few missing semicolons were added and a few unnecessary ones were removed.

## **[BACK TO TOP](#content-quick-links)** *
<hr style="height:5px;border-width:0;color:gray;background-color: #eca50b">

## Manual Testing:

### Responsive Design: 


### Call to action buttons:


### External links:


### Internal links:


### Lighthouse performance test:
![Lighhouse test](media/readme_images/validation/lighthouse_report.png)

Lighthouse in Chrome devtools was used to test the website's performance. According to the Lighthouse suggestion the report was generated from an Incognito mode.

Two warnings were taken into account and fixed, namely: 
- adding a meta description to base.html
- adding the rel="noopener" attribute to the external social media links located in the footer.

### Accessibility:

![Accessiblity test](wireframes/accessibility.png)


## **[BACK TO TOP](#content-quick-links)** *
<hr style="height:5px;border-width:0;color:gray;background-color: #eca50b">

## Automated Testing



![Automated Test](ADD)


## **[BACK TO TOP](#content-quick-links)** *
<hr style="height:5px;border-width:0;color:gray;background-color: #eca50b">

## User Authentication:

![Authentication](!!! ADD )

3. **Adding Reviews and Adding to Favourites**:




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

## Bugs and fixes:

* It is known that there are still some minor responsive styling issues for unpopular screen sizes that are planned to be tackled in the future.

* During the testing of the Delete Product function the following error was encountered while trying to delete a product that was still in the shopping bag: "No Product matches the given query." The following Slack post helped to resolve the issue: https://code-institute-room.slack.com/archives/C7HS3U3AP/p1631708528269000 by clearing the site data in the Application Storage.

* There is a number of flake8 and pylint errors that were not resolved due to my lack of experience and knowledge (which is constantly improving), as well as time constraints and the complexity and potential affect on the functionality of the site.

* Rating field is still displayed and is editable in the Add Product form. Since the ratings are coming from user reviews, this field should not be editable by anyone (including the site admin). This will be taken care of in the future as the time did not allow to look into this issue closely.

* The toasts messages reappear from the previous action when the back browser button is clicked. It is planned in the future to implement a timeout function and ensure the message does not reappear.

### Known Bugs

### Not bugs but the room and notes for improvement.

* It is planned to prepopulate user's full name in the checkout form for authanticated users.




## **[BACK TO TOP](#content-quick-links)** *
<hr style="height:5px;border-width:0;color:gray;background-color: #eca50b">




