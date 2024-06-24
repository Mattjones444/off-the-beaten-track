# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files and used the [Validate by uri](https://validator.w3.org/#validate_by_uri) for the live pages.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Foff-the-beaten-track-b019d3277c26.herokuapp.com%2F) | ![screenshot](/media/readme/htmlvalidation-main.png) | Pass: No Errors|
| Activity | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Foff-the-beaten-track-b019d3277c26.herokuapp.com%2Factivity) | ![screenshot](/media/readme/htmlvalidation-activity.png) | Pass: No Errors |
| Bag | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Foff-the-beaten-track-b019d3277c26.herokuapp.com%2Fbag) | ![screenshot](/media/readme/htmlvalidation-bag.png) | Pass: No Errors |
| Checkout | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Foff-the-beaten-track-b019d3277c26.herokuapp.com%2Fcheckout) | ![screenshot](/media/readme/htmlvalidation-checkout.png) | Pass: No Errors |



### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| base.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Flunar-glow-77444c493d2e.herokuapp.com) | ![screenshot](documentation/css-validation-base.png) | Pass: No Errors |
| checkout.css | n/a | ![screenshot](documentation/css-validation-checkout.png) | Pass: No Errors |
| profile.css | n/a | ![screenshot](documentation/css-validation-profile.png) | Pass: No Errors |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| stripe_elements.js | ![screenshot](documentation/js-validation-stripe.png) | Undefined Stripe variable - external library |
| countryfield.js | ![screenshot](documentation/js-validation-countryfield.png) | Pass: No Errors |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Bag urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/bag/urls.py) | ![screenshot](documentation/py-validation-bag-urls.png) | Pass: No Errors |
| Bag views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/d3lyth/lunar_glow/main/profiles/models.py) | ![screenshot](documentation/py-validation-bag-views.png) | Pass: No Errors |
| Bag apps.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/bag/apps.py) | ![screenshot](documentation/py-validation-bag-apps.png) | Pass: No Errors |
| Bag bagtools.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/bag/templatetags/bag_tools.py) | ![screenshot](documentation/py-validation-bag-bagtools.png) | Pass: No Errors |
| Checkout admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/checkout/admin.py) | ![screenshot](documentation/py-validation-checkout-admin.png) | Pass: No Errors |
| Checkout forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/checkout/forms.py) | ![screenshot](documentation/py-validation-checkout-forms.png) | Pass: No Errors |
| Checkout models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/checkout/models.py) | ![screenshot](documentation/py-validation-checkout-models.png) | Pass: No Errors |
| Checkout signals.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/checkout/signals.py) | ![screenshot](documentation/py-validation-checkout-signals.png) | Pass: No Errors |
| Checkout urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/checkout/urls.py) | ![screenshot](documentation/py-validation-checkout-urls.png) | Pass: No Errors |
| Checkout views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/checkout/views.py) | ![screenshot](documentation/py-validation-checkout-views.png) | Pass: No Errors |
| Checkout webhook_handler.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/checkout/webhook_handler.py) | ![screenshot](documentation/py-validation-checkout-webhook_handler.png) | Pass: No Errors |
| Checkout webhooks.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/checkout/webhooks.py) | ![screenshot](documentation/py-validation-checkout-webhooks.png) | Error: Line too long |
| FAQs admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/faqs/admin.py) | ![screenshot](documentation/py-validation-faqs-admin.png) | Pass: No Errors |
| FAQs models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/faqs/models.py) | ![screenshot](documentation/py-validation-faqs-models.png) | Pass: No Errors |
| FAQs urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/faqs/urls.py) | ![screenshot](documentation/py-validation-faqs-urls.png) | Pass: No Errors |
| FAQs views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/faqs/views.py) | ![screenshot](documentation/py-validation-faqs-views.png) | Pass: No Errors |
| Home urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/home/urls.py) | ![screenshot](documentation/py-validation-home-urls.png) | Pass: No Errors |
| Home views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/home/views.py) | ![screenshot](documentation/py-validation-home-views.png) | Pass: No Errors |
| Lunar Glow settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/lunar_glow/settings.py) | ![screenshot](documentation/py-validation-lunarglow-settings.png) | Pass: No Errors |
| Lunar Glow urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/lunar_glow/urls.py) | ![screenshot](documentation/py-validation-lunarglow-urls.png) | Pass: No Errors |
| Newsletter admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/newsletter/admin.py) | ![screenshot](documentation/py-validation-newsletter-admin.png) | Pass: No Errors |
| Newsletter forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/newsletter/forms.py) | ![screenshot](documentation/py-validation-newsletter-forms.png) | Pass: No Errors |
| Newsletter models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/newsletter/models.py) | ![screenshot](documentation/py-validation-newsletter-models.png) | Pass: No Errors |
| Newsletter urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/newsletter/urls.py) | ![screenshot](documentation/py-validation-newsletter-urls.png) | Pass: No Errors |
| Newsletter views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/newsletter/views.py) | ![screenshot](documentation/py-validation-newsletter-views.png) | Pass: No Errors |
| Products admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/products/admin.py) | ![screenshot](documentation/py-validation-products-admin.png) | Pass: No Errors |
| Products forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/products/forms.py) | ![screenshot](documentation/py-validation-products-forms.png) | Pass: No Errors |
| Products models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/products/models.py) | ![screenshot](documentation/py-validation-products-models.png) | Pass: No Errors |
| Products urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/products/urls.py) | ![screenshot](documentation/py-validation-products-urls.png) | Pass: No Errors |
| Products views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/products/views.py) | ![screenshot](documentation/py-validation-products-views.png) | Pass: No Errors |
| Products widgets.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/products/widgets.py) | ![screenshot](documentation/py-validation-products-widgets.png) | Pass: No Errors |
| Profiles forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/profiles/forms.py) | ![screenshot](documentation/py-validation-profiles-forms.png) | Pass: No Errors |
| Profiles models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/profiles/models.py) | ![screenshot](documentation/py-validation-profiles-models.png) | Pass: No Errors |
| Profiles urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/profiles/urls.py) | ![screenshot](documentation/py-validation-profiles-urls.png) | Pass: No Errors |
| Profiles views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/profiles/views.py) | ![screenshot](documentation/py-validation-profiles-views.png) | Pass: No Errors |
| Scent Profile admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/scentprofile/admin.py) | ![screenshot](documentation/py-validation-scentprofile-admin.png) | Pass: No Errors |
| Scent Profile models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/scentprofile/models.py) | ![screenshot](documentation/py-validation-scentprofile-models.png) | Pass: No Errors |
| Scent Profile urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/scentprofile/urls.py) | ![screenshot](documentation/py-validation-scentprofile-urls.png) | Pass: No Errors |
| Scent Profile views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/scentprofile/views.py) | ![screenshot](documentation/py-validation-scentprofile-views.png) | Pass: No Errors |
| Root Level custom_storages.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/custom_storages.py) | ![screenshot](documentation/py-validation-rootlevel-custom_storages.png) | Pass: No Errors |
| Root Level manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D3lyth/lunar_glow/main/manage.py) | ![screenshot](documentation/py-validation-rootlevel-manage.png) | Pass: No Errors |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.
The browsers tested include:
- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Edge](https://www.microsoft.com/edge)
- [Safari](https://support.apple.com/downloads/safari)
- [Brave](https://brave.com/download)
- [Opera](https://www.opera.com/download)

| Browser | Home | Products | FAQs | Newsletter | Which Scent? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browser-chrome-home.png) | ![screenshot](documentation/browser-chrome-products.png) | ![screenshot](documentation/browser-chrome-faqs.png) | ![screenshot](documentation/browser-chrome-newsletter.png) | ![screenshot](documentation/browser-chrome-whichscent.png) |Works as expected |
| Firefox | ![screenshot](documentation/browser-firefox-home.png) | ![screenshot](documentation/browser-firefox-products.png) | ![screenshot](documentation/browser-firefox-faqs.png) | ![screenshot](documentation/browser-firefox-newsletter.png) | ![screenshot](documentation/browser-firefox-whichscent.png) |Works as expected |
| Edge | ![screenshot](documentation/browser-edge-home.png) | ![screenshot](documentation/browser-edge-products.png) | ![screenshot](documentation/browser-edge-faqs.png) | ![screenshot](documentation/browser-edge-newsletter.png) | ![screenshot](documentation/browser-edge-whichscent.png) |Works as expected |
| Safari | ![screenshot](documentation/browser-safari-home.png) | ![screenshot](documentation/browser-safari-products.png) | ![screenshot](documentation/browser-safari-faqs.png) | ![screenshot](documentation/browser-safari-newsletter.png) | ![screenshot](documentation/browser-safari-whichscent.png) |Minor CSS differences |
| Brave | ![screenshot](documentation/browser-brave-home.png) | ![screenshot](documentation/browser-brave-products.png) | ![screenshot](documentation/browser-brave-faqs.png) | ![screenshot](documentation/browser-brave-newsletter.png) | ![screenshot](documentation/browser-brave-whichscent.png) |Works as expected |
| Opera | ![screenshot](documentation/browser-opera-home.png) | ![screenshot](documentation/browser-opera-products.png) | ![screenshot](documentation/browser-opera-faqs.png) | ![screenshot](documentation/browser-opera-newsletter.png) | ![screenshot](documentation/browser-opera-whichscent.png) |Minor differences |


## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | Products | FAQs | Newsletter | Which Scent | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Mobile (DevTools - Samsung Galaxy S20 Ultra) | ![screenshot](documentation/responsive-mobile-home.png) | ![screenshot](documentation/responsive-mobile-products.png) | ![screenshot](documentation/responsive-mobile-faqs.png) | ![screenshot](documentation/responsive-mobile-newsletter.png) |![screenshot](documentation/responsive-mobile-whichscent.png) | Works as expected |
| Tablet (iPad Air) | ![screenshot](documentation/responsive-tablet-home.png) | ![screenshot](documentation/responsive-tablet-products.png) | ![screenshot](documentation/responsive-tablet-faqs.png) | ![screenshot](documentation/responsive-tablet-newsletter.png) | ![screenshot](documentation/responsive-tablet-whichscent.png) | Works as expected |
| Desktop | ![screenshot](documentation/responsive-desktop-home.png) | ![screenshot](documentation/responsive-desktop-products.png) | ![screenshot](documentation/responsive-desktop-faqs.png) | ![screenshot](documentation/responsive-desktop-newsletter.png) |![screenshot](documentation/responsive-tablet-whichscent.png) |  Works as expected |
| XL Monitor | ![screenshot](documentation/responsive-xl-home.png) | ![screenshot](documentation/responsive-xl-products.png) | ![screenshot](documentation/responsive-xl-faqs.png) | ![screenshot](documentation/responsive-xl-newsletter.png) | ![screenshot](documentation/responsive-xl-whichscent.png) | Scaling starts to have minor issues |
| 4K Monitor | ![screenshot](documentation/responsive-4k-home.png) | ![screenshot](documentation/responsive-4k-products.png) | ![screenshot](documentation/responsive-4k-faqs.png) | ![screenshot](documentation/responsive-4k-newsletter.png) | ![screenshot](documentation/responsive-4k-whichscent.png) | Noticeable scaling issues |
| iPhone 14 | ![screenshot](documentation/responsive-iphone-home.png) | ![screenshot](documentation/responsive-iphone-products.png) | ![screenshot](documentation/responsive-iphone-faqs.png) | ![screenshot](documentation/responsive-iphone-newsletter.png) | ![screenshot](documentation/responsive-iphone-whichscent.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse-home-mobile.png) | ![screenshot](documentation/lighthouse-home-desktop.png) | Slow response time due to large images |
| Products | ![screenshot](documentation/lighthouse-products-mobile.png) | ![screenshot](documentation/lighthouse-products-desktop.png) | Slow response time due to large images |
| FAQs | ![screenshot](documentation/lighthouse-faqs-mobile.png) | ![screenshot](documentation/lighthouse-faqs-desktop.png) | Slow response time due to large images |
| Newsletter | ![screenshot](documentation/lighthouse-newsletter-mobile.png) | ![screenshot](documentation/lighthouse-newsletter-desktop.png) | Slow response time due to large images |
| Which Scent? | ![screenshot](documentation/lighthouse-whichscent-mobile.png) | ![screenshot](documentation/lighthouse-whichscent-desktop.png) | Slow response time due to large images |
| Bag | ![screenshot](documentation/lighthouse-bag-mobile.png) | ![screenshot](documentation/lighthouse-bag-desktop.png) | Slow response time due to large images |
| Checkout | ![screenshot](documentation/lighthouse-checkout-mobile.png) | ![screenshot](documentation/lighthouse-checkout-desktop.png) | Slow response time due to large images |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
| | Page is expected to open the signup/login page when the user does clicks on 'My Profile'. | Tested the feature by clicking on 'My Profile'  | The feature behaved as expected, and it did open to the signup/login page | Test concluded and passed | ![screenshot](documentation/feature01.png) |
| | Search bar is expected to return results that include keywords whne searched | Tested the feature by searching various words | The feature behaved as expected. | Test concluded and passed | ![screenshot](documentation/feature02.png) |
| Navigation - All Pages | | | | | |
| | Navigation links are expected to do take the user to the correct page when the user does clicks on them | Tested the feature by clicking on links and checking which pages open | The feature behaved as expected, and opened correct pages| Test concluded and passed | ![screenshot](documentation/feature03.png) |
| | Feature is expected to go to the shopping bag when clicked | Tested the feature by clicking on the bag | The feature worked as expected. | Test concluded and passed | ![screenshot](documentation/feature04.png) |
| Newsletter | | | | | |
| | Feature is expected to allow user to fill a form and subscribe to a newsletter | Tested the feature by doing adding name and e-mail address to the form | Tested the feature by filling in the form details | Test concluded and passed | ![screenshot](documentation/feature05.png) |
| Scent Profile| | | | | |
| | Feature is expected to send the user to a products page of all the products with a particular scent when button on carousel is clicked | Tested the feature by clicking on button | The feature worked as expected.  | Test concluded and passed | ![screenshot](documentation/feature06.png) |
| FAQs | | | | | |
| | Feature is expected to show the answer to an FAQ as a droop down when the question is clicked upon. | Tested the feature by clicking on question | The feature behaved as expected, and it showed the answer | Test concluded and passed | ![screenshot](documentation/feature07.png) |
| Shopping Bag | | | | | |
| | Feature is expected to add, remove and delete items in the bag | Tested the feature by adding items to the bag, change the numbeer of items and delete items | The feature worked as expected. | Test concluded and passed | ![screenshot](documentation/feature08.png) |
| Admin Panel | | | | | |
| | Feature is expected to allow the admin user to manage order details of customers | Tested the feature by changing quantities and deleting items from order| The feature worked as expected. | Test concluded and passed | ![screenshot](documentation/feature09.png) |
| | Feature is expected to allow administrator to have access to various tables such as orders, products, subscribers and faqs to allow adding, editing, and removal of faqs, products and subscribers  | Tested the feature by adding, editing, and removal of faqs, products and subscribers | The feature worked as expected.| Test concluded and passed | ![screenshot](documentation/feature10.png) |


Soe other tests were conducted which include results below:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| Navigation | | | | |
| | Click on any link in navbar | Redirection to all pages | Pass | |
| | Search bar | Searches work as expected | Pass | |
| Newsletter | | | | |
| | Click on Newsletter link in navbar | Redirection to newsletter form | Pass | |
| | Enter first/last name | Field will accept freeform text | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Click the Submit button | Redirects user to form-dump | Pass |  |
| Sign Up | | | | |
| | Click on Sign Up button | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Asks user to confirm email page | Pass | Email sent to user |
| | Confirm email | Redirects user to blank Sign In page | Pass | |
| Log In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Profile | | | | |
| | Click on Profile button | User will be redirected to the Profile page | Pass | |
| | Click on the Edit button | User will be redirected to the edit profile page | Pass | |
| | Click on the My Orders link | User will be redirected to the My Orders page | Pass | |
| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |
| Products | | | | |
| | Click on product image | User will be redirected to the Product Details page | Pass | |
| Product Details | | | | |
| | Click on + / - button to add/remove product from bag | Quantity in bag will increase/decrease | Pass | |
| | Click on add to bag button to add product to bag | Item will be added to bag | Pass | |
| | Click on keep shopping button to add product to bag | Item will be added to bag | Pass | |
| Which Scent? | | | | |
| | Click on scroll button to move through the carousel | Carousel will move to the next scent profile | Pass | |


## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a new user, I want to create an account and set up my profile, so that I can store my order details and preferences securely, enhancing my shopping experience. | ![screenshot](documentation/feature01.png) |
| As a user, I want to easily browse, search, and sort through various candles and wax melts, so that I can quickly find products that match my preferences and improve my shopping experience. | ![screenshot](documentation/feature02.png) |
| As a user, I want clear navigation elements and interactive buttons, so that I can easily move between sections/pages and perform actions efficiently, enhancing my overall experience on the site. | ![screenshot](documentation/feature03.png) |
| As an administrator, I want to manage products effectively by adding new items, updating details, and removing discontinued products, so that I can keep the inventory fresh and relevant for users. | ![screenshot](documentation/feature04.png) |
| As a user, I want to subscribe to newsletters and receive updates about new products and promotions, so that I can stay informed and engaged with the website, leading to repeat visits. | ![screenshot](documentation/feature05.png) |
| As a user, I want to explore scent profiles and find products that match my preferred fragrances, so that I can make informed purchasing decisions and enhance my satisfaction with the products. | ![screenshot](documentation/feature06.png) |
| As a user, I want access to a comprehensive FAQ section to find answers to common questions, so that I can resolve uncertainties and improve my shopping experience on the site. | ![screenshot](documentation/feature07.png) |
| As a user, I want to manage my shopping bag by adding, editing, or removing items before checkout, so that I can review and adjust my orders conveniently, ensuring a smooth purchasing process. | ![screenshot](documentation/feature08.png) |
| As an administrator, I want to view and manage order details, as well as handle customer inquiries efficiently, so that I can streamline order processing and provide excellent customer service. | ![screenshot](documentation/feature09.png) |
| As an administrator, I want access to a dashboard to manage various aspects of the website, including products, user profiles, orders, FAQs, and newsletter subscribers, so that I can efficiently oversee and maintain the site for optimal performance and user experience. | ![screenshot](documentation/feature10.png) |

## Bugs

- Checkout Success form not totalling the order amount correctly and just showing £0.00.

    - To fix this, I changed to code to access the totals from the order object instead of the bag context.

- Python `E501 line too long` (93 > 79 characters)

    - To fix this, I refactored the code so that the line was not too long.

- CSS Footer Styling issues - the footer was not pushing to the bottom of the page.

    - To fix this, I ran the page through the validator and noticed an open `<div>` tag, which when closed, rectified the problem.

## Unfixed Bugs

- Element `<ul>` not allowed as a child element of `small`

    - Attempted fix: This is a known bug with Django-Allauth and is acceptable. ![screenshot](documentation/bug01.png) 

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.