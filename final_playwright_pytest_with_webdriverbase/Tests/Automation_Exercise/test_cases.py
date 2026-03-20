# import time
# from data.test_data import TEST_DATA
# from Pages.registerPage import registerPage, registerPageLocator
# from Pages.loginPage import loginPage, loginPageLocator
# from Pages.contactUsPage import contactUsPage, contactUsPageLocator
# from Pages.testCasePage import testCasePage, testCasePageLocator
# from Pages.productPage import productPage, productPageLocator
# from Pages.homePage import homePage, homePageLocator
# from Pages.cartPage import cartPage, cartPageLocator
# from Pages.paymentPage import paymentPage, paymentPageLocator

# from Shared.webpagebase import webpagebase
# from Shared.commonfunctions import commonfunctions


# class Tests(webpagebase):

#     def setUp(self):
#         super().setUp()

#         self.obj_registerPage = registerPage(self.page)
#         self.obj_loginPage = loginPage(self.page)
#         self.obj_contactUsPage = contactUsPage(self.page)
#         self.obj_testCasePage = testCasePage(self.page)
#         self.obj_productPage = productPage(self.page)
#         self.obj_homePage = homePage(self.page)
#         self.obj_cartPage = cartPage(self.page)
#         self.obj_paymentPage = paymentPage(self.page)
#         self.cf = commonfunctions(self.page)
    
#     def test_verify_account_registered_deleted(self):
#         '''Test Case 1: Register User'''
#         try:
#             # homepage verification
#             homepage_element = self.obj_registerPage.presence_of_element(registerPageLocator.login_signup) 
#             self.assertTrue(homepage_element,'Homepage is not visible')
#             print("Homepage is visible")

#             # click on login/singup of homepage
#             self.obj_registerPage.click_button(registerPageLocator.login_signup) 

#             # signup page verification
#             signup_element = self.obj_registerPage.presence_of_element(registerPageLocator.signup_text) 
#             self.assertTrue( signup_element,'singup page is not visible')
#             print('signup page is visible') 

#             # enter the username and email
#             email_cfg = TEST_DATA["signup"]["email_strategy"]
#             email = f'{email_cfg["prefix"]}{int(time.time())}{email_cfg["domain"]}' 
#             self.obj_registerPage.user_signup_input(TEST_DATA["signup"]["name"], email)

#             # click on signup
#             self.obj_registerPage.click_button(registerPageLocator.singUp_btn)

#             # account information verification
#             acc_info_element = self.obj_registerPage.presence_of_element(registerPageLocator.acc_info_intro_text)
#             self.assertTrue(acc_info_element,'account information page is not visible')
#             print('account information page is visible')
            
#             # account information details filling 
#             self.obj_registerPage.fill_acc_form_details(
#                 TEST_DATA["signup"]["title"],
#                 TEST_DATA["signup"]["password"],
#                 TEST_DATA["signup"]["dob"]
#             )
#             cb = TEST_DATA["signup"]["checkboxes"]
#             self.obj_registerPage.check_the_box(cb["newsletter"], cb["special_offer"])
#             addr = TEST_DATA["signup"]["address"]
#             self.obj_registerPage.fill_address_form_details(
#                 addr["first_name"],
#                 addr["last_name"],
#                 addr["company"],
#                 addr["address1"],
#                 addr["address2"],
#                 addr["country"],
#                 addr["state"],
#                 addr["city"],
#                 addr["zipcode"],
#                 addr["mobile"]
#             )
#             # click on create account button
#             self.obj_registerPage.click_button(registerPageLocator.address_info_create_account_btn)

#             # account creation verification
#             account_created_element = self.obj_registerPage.presence_of_element(registerPageLocator.account_created_text)
#             self.assertTrue(account_created_element,'account is not created')
#             print('successfully account is created')    

#             # click on continue button of account created   
#             self.obj_registerPage.click_button(registerPageLocator.acc_created_continue_btn) 

#             # username visiblity verification
#             username_element = self.obj_registerPage.presence_of_element(registerPageLocator.username_visible_btn)   
#             self.assertTrue(username_element,'failed to show logged in')
#             print('successfully showed logged in')   

#             # delete account click    
#             self.obj_registerPage.click_button(registerPageLocator.del_acc_btn)   

#             # account deletion verification 
#             del_continue_element = self.obj_registerPage.presence_of_element(registerPageLocator.deleted_account_text)
#             self.assertTrue(del_continue_element,'error while deleting account')
#             print('account deleted successfully')

#             # continue button click on deleted account page 
#             self.obj_registerPage.click_button(registerPageLocator.del_acc_continue_btn) 

#         except RuntimeError as e:
#             print(f"Test failed due to error: {e}") 

#     def test_verify_account_login_right_credentials(self):
#         '''Test Case 2: Login User with correct email and password'''
#         try:
#             homepage_element = self.obj_loginPage.presence_of_element(loginPageLocator.login_signup) 
#             self.assertTrue(homepage_element,'page is not visible')
#             print("Homepage is visible")   

#             # click on login/signup button on homepage 
#             self.obj_loginPage.click_button(loginPageLocator.login_signup) 

#             # login page visiblity verification
#             login_element = self.obj_loginPage.presence_of_element(loginPageLocator.login_page_text) 
#             self.assertTrue( login_element,'login page is not visible')
#             print('login page is visible')       

#             '''this will create account and return login credential for login'''
#             # Create a fresh account first 
#             email, password = self.obj_registerPage.create_account(
#                 TEST_DATA["signup"],
#                 TEST_DATA["signup"]["email_strategy"],
#             )

#             # Logout to ensure we perform an actual login step
#             self.obj_loginPage.click_button(loginPageLocator.logout_button)

#             login_element = self.obj_loginPage.presence_of_element(loginPageLocator.login_page_text)
#             self.assertTrue(login_element, 'login page is not visible after logout')

#             # enter the the login details and click on the login button   
#             self.obj_loginPage.user_login_input(email, password)
#             self.obj_loginPage.click_button(loginPageLocator.login_btn) 

#             # username visiblity verificaiton
#             username_element = self.obj_loginPage.presence_of_element(loginPageLocator.username_visible_btn)   
#             self.assertTrue(username_element,'failed to show logged in')
#             print('successfully showed logged in')  

#             # click on delete button 
#             self.obj_loginPage.click_button(loginPageLocator.del_acc_btn)   

#             # account deletion verification
#             del_continue_element = self.obj_loginPage.presence_of_element(loginPageLocator.del_acc_text)
#             self.assertTrue(del_continue_element,'error while deleting account')
#             print('account deleted successfully')  

#             # Continue after deletion 
#             self.obj_loginPage.click_button(loginPageLocator.del_acc_continue_btn)

#         except RuntimeError as e:
#             print(f"Test failed due to error: {e}") 

#     def test_verify_account_login_wrong_credentials(self):
#         '''Test Case 3: Login User with incorrect email and password'''
#         try:
#             # homepage visiblity verification
#             homepage_element = self.obj_loginPage.presence_of_element(loginPageLocator.login_signup) 
#             self.assertTrue(homepage_element,'page is not visible')
#             print("Homepage is visible")   

#             # click on login/signup button on homepage 
#             self.obj_loginPage.click_button(loginPageLocator.login_signup)

#             # login page visiblity verification
#             login_element = self.obj_loginPage.presence_of_element(loginPageLocator.login_page_text) 
#             self.assertTrue( login_element,'login page is not visible')
#             print('login page is visible')        

#             # enter the the login details and click on the login button   
#             bad = TEST_DATA["login"]["invalid"]
#             self.obj_loginPage.user_login_input(bad["email"], bad["password"])
#             self.obj_loginPage.click_button(loginPageLocator.login_btn) 

#             # wrong credentials error verification
#             error_element = self.obj_loginPage.presence_of_element(loginPageLocator.error_after_password)
#             self.assertTrue(error_element,'credentials are right')
#             print('credentials are wrong out of password or email_address')  

#         except RuntimeError as e:
#             print(f"Test failed due to error: {e}")  

#     def test_verify_account_logout_user(self):
#         '''Test Case 4: Logout User'''
#         try:
#             # homepage visiblity verification
#             homepage_element = self.obj_loginPage.presence_of_element(loginPageLocator.login_signup) 
#             self.assertTrue(homepage_element,'page is not visible')
#             print("Homepage is visible")   

#             # click on login/signup button on homepage 
#             self.obj_loginPage.click_button(loginPageLocator.login_signup)

#             # login page visiblity verification
#             login_element = self.obj_loginPage.presence_of_element(loginPageLocator.login_page_text) 
#             self.assertTrue( login_element,'login page is not visible')
#             print('login page is visible')              

#             # enter the the login details and click on the login button   
#             logout_user = TEST_DATA["login"]["logout_user"]
#             self.obj_loginPage.user_login_input(logout_user["email"], logout_user["password"])
#             self.obj_loginPage.click_button(loginPageLocator.login_btn) 

#             # username visiblity verificaiton
#             username_element = self.obj_loginPage.presence_of_element(loginPageLocator.username_visible_btn)   
#             self.assertTrue(username_element,'failed to show logged in')
#             print('successfully showed logged in')  

#             # click on logout button 
#             self.obj_loginPage.click_button(loginPageLocator.logout_button)   

#             # back to login page visiblity verification
#             login_element = self.obj_loginPage.presence_of_element(loginPageLocator.login_page_text) 
#             self.assertTrue( login_element,'login page is not visible')
#             print('login page is visible')  

#         except RuntimeError as e:
#             print(f"Test failed due to error: {e}")                                     

#     def test_verify_acccount_register_email_exist(self):
#         '''Test Case 5: Register User with existing email'''
#         try:
#             # homepage verification
#             homepage_element = self.obj_registerPage.presence_of_element(registerPageLocator.login_signup) 
#             self.assertTrue(homepage_element,'page is not visible')
#             print("Homepage is visible")

#             # click on login/singup of homepage
#             self.obj_registerPage.click_button(registerPageLocator.login_signup)

#             # signup page verification
#             signup_element = self.obj_registerPage.presence_of_element(registerPageLocator.signup_text) 
#             self.assertTrue( signup_element,'singup page is not visible')
#             print('signup page is visible') 

#             # enter the username and password 
#             existing = TEST_DATA["existing_signup"]
#             self.obj_registerPage.user_signup_input(existing["name"], existing["email"])

#             # click on signup
#             self.obj_registerPage.click_button(registerPageLocator.singUp_btn)

#             # error while signup
#             error_element = self.obj_registerPage.presence_of_element(registerPageLocator.error_after_email)
#             self.assertTrue(error_element,'error is not there')
#             print('already email address is exist')
            
#         except RuntimeError as e:
#             print(f"Test failed due to error: {e}") 

#     def test_verify_acccount_contact_us(self):
#             '''Test Case 6: Contact Us Form'''
#             try:
#                 # homepage verification
#                 homepage_element = self.obj_contactUsPage.presence_of_element(contactUsPageLocator.contact_us_button) 
#                 self.assertTrue(homepage_element,'page is not visible')
#                 print("Homepage is visible")

#                 # click on contact us of homepage
#                 self.obj_contactUsPage.click_button(contactUsPageLocator.contact_us_button)

#                 # contactUs page visiblity verification
#                 contact_us_element = self.obj_contactUsPage.presence_of_element(contactUsPageLocator.get_in_touch_text) 
#                 self.assertTrue(contact_us_element,'contact us page is not visible')
#                 print('contact us page is visible') 

#                 # enter the details 
#                 contact = TEST_DATA["contact_us"]
#                 self.obj_contactUsPage.contact_us_input(contact["name"], contact["email"], contact["subject"], contact["message"])

#                 # upload the file
#                 self.obj_contactUsPage.file_send(contactUsPageLocator.contact_us_file_upload,contactUsPageLocator.file_path)

#                 # click on submit button
#                 self.obj_contactUsPage.click_button(contactUsPageLocator.contact_us_submit)

#                 # click on okay button prompted by browser
#                 self.cf.accept_alert()

#                 # file is uploaded or not verification
#                 success_message_element = self.obj_contactUsPage.presence_of_element(contactUsPageLocator.success_message)
#                 self.assertTrue(success_message_element,'file is not uploaded')
#                 print('file is uploaded successfully')

#                 # click on home button
#                 self.obj_contactUsPage.click_button(contactUsPageLocator.home_page_button)

#                 # verify that landed on homepage
#                 homepage_element = self.obj_contactUsPage.presence_of_element(contactUsPageLocator.contact_us_button) 
#                 self.assertTrue(homepage_element,'page is not visible')
#                 print("Homepage is visible")
                

#             except RuntimeError as e:
#                 print(f"Test failed due to error: {e}")      

#     def test_verify_test_cases_page(self):
#             '''Test Case 7: Verify Test Cases Page'''
#             try:
#                 # homepage verification
#                 homepage_element = self.obj_testCasePage.presence_of_element(testCasePageLocator.test_case_button)
#                 self.assertTrue(homepage_element,'page is not visible')
#                 print("Homepage is visible")

#                 # click on test case page 
#                 self.obj_testCasePage.click_button(testCasePageLocator.test_case_button)

#                 # test case page visiblity verification
#                 test_case_element = self.obj_testCasePage.presence_of_element(testCasePageLocator.test_case_text) 
#                 self.assertTrue(test_case_element,'test case page is not visible')
#                 print('test case page is visible') 

#             except RuntimeError as e:
#                 print(f"Test failed due to error: {e}")    

#     def test_verify_product_detail_page(self):
#         '''Test Case 8: Verify All Products and product detail page'''
#         try:
#             # homepage verification
#             homepage_element = self.obj_productPage.presence_of_element(productPageLocator.product_button)
#             self.assertTrue(homepage_element,'page is not visible')
#             print("Homepage is visible")

#             # click on products page 
#             self.obj_productPage.click_button(productPageLocator.product_button)

#             # ALL PRODUCTS page visiblity verification
#             product_page_element = self.obj_productPage.presence_of_element(productPageLocator.product_page_text) 
#             self.assertTrue(product_page_element,'all products page is not visible')
#             print('all products page is visible') 

#             # product list visible verification
#             products_visible_element = self.obj_productPage.all_product_is_visible()
#             self.assertTrue(products_visible_element, 'product list is not visible')
#             print('product list is visible')

#             # click on view product of first product
#             self.obj_productPage.click_on_product(TEST_DATA["products"]["view_product_index"])  # converted to string then

#             # verify that user landed on product detail page
#             product_detail_page_element = self.obj_productPage.presence_of_element(productPageLocator.product_detail_page_check)
#             self.assertTrue(product_detail_page_element,'user is not landed product detail page')
#             print('user is landed on product detail page')

#             # product name is visible or not checking
#             product_name_element = self.obj_productPage.presence_of_element(productPageLocator.product_name)
#             self.assertTrue(product_name_element,'product name is not visible')
#             print('product name is visible')

#             # product category is visible or not checking
#             product_category_element = self.obj_productPage.presence_of_element(productPageLocator.product_category)
#             self.assertTrue(product_category_element,'product category is not visible')
#             print('product category is visible')

#             # product price is visible or not checking
#             product_price_element = self.obj_productPage.presence_of_element(productPageLocator.product_price)
#             self.assertTrue(product_price_element,'product price is not visible')
#             print('product price is visible')

#             # product availability is visible or not checking
#             product_availability_element = self.obj_productPage.presence_of_element(productPageLocator.product_availability)
#             self.assertTrue(product_availability_element,'product availability is not visible')
#             print('product availability is visible')

#             # product condition is visible or not checking
#             product_condition_element = self.obj_productPage.presence_of_element(productPageLocator.product_condition)
#             self.assertTrue(product_condition_element,'product condition is not visible')
#             print('product condition is visible')

#             # product brand is visible or not checking
#             product_brand_element = self.obj_productPage.presence_of_element(productPageLocator.product_brand)
#             self.assertTrue(product_brand_element,'product brand is not visible')
#             print('product brand is visible')

#         except RuntimeError as e:
#             print(f"Test failed due to error: {e}")  

#     def test_verify_search_product(self):
#         '''Test Case 9: Search Product'''
#         try:
#             # homepage verification
#             homepage_element = self.obj_productPage.presence_of_element(productPageLocator.product_button)
#             self.assertTrue(homepage_element,'page is not visible')
#             print("Homepage is visible")

#             # click on products page 
#             self.obj_productPage.click_button(productPageLocator.product_button)

#             # ALL PRODUCTS page visiblity verification
#             product_page_element = self.obj_productPage.presence_of_element(productPageLocator.product_page_text) 
#             self.assertTrue(product_page_element,'all products page is not visible')
#             print('all products page is visible') 

#             # serch for product
#             keyword = TEST_DATA["search"]["keyword"]
#             self.obj_productPage.search_product(keyword)

#             # verify SEARCHED PRODUCTS text
#             searched_text = self.obj_productPage.presence_of_element(productPageLocator.searched_products_text)
#             self.assertTrue(searched_text, "'SEARCHED PRODUCTS' not visible")
#             print("'SEARCHED PRODUCTS' is visible")

#             # get searched products
#             products_element = self.obj_productPage.validate_searched_products(keyword)
#             self.assertTrue(products_element,"Search result contains invalid products")
#             print('searched product contains valid result')

#         except RuntimeError as e:
#             print(f"Test failed due to error: {e}")      
                   
#     def test_verify_subscription_in_home_page(self):
#         '''Test Case 10: Verify Subscription in home page'''
#         try:
#             # homepage verification
#             homepage_element = self.obj_homePage.presence_of_element(homePageLocator.product_button)
#             self.assertTrue(homepage_element,'page is not visible')
#             print("Homepage is visible")

#             # scroll to footer 
#             self.obj_homePage.scroll_to_footer()

#             #  Verify text 'SUBSCRIPTION'
#             subscription_text_element = self.obj_homePage.presence_of_element(homePageLocator.subscription_text) 
#             self.assertTrue(subscription_text_element,'subscription is not visible')
#             print('subscription is visible') 

#             # enter email address
#             self.obj_homePage.email_input(TEST_DATA["subscription"]["email"])

#             # click on submit arrow button
#             self.obj_homePage.click_button(homePageLocator.arrow_button)

#             # verify 'You have been successfully subscribed!' 
#             success_text_element = self.obj_homePage.presence_of_element(homePageLocator.success_message) 
#             self.assertTrue(success_text_element,'subscription message is not visible')
#             print('subscription message is visible') 


#         except RuntimeError as e:
#             print(f"Test failed due to error: {e}")  

#     def test_verify_subscription_in_cart_page(self):
#         '''Test Case 11: Verify Subscription in Cart page'''
#         try:
#             # homepage verification
#             homepage_element = self.obj_cartPage.presence_of_element(cartPageLocator.cart_button)
#             self.assertTrue(homepage_element,'page is not visible')
#             print("Homepage is visible")

#             # click cart button
#             self.obj_cartPage.click_button(cartPageLocator.cart_button)

#             # scroll to footer 
#             self.obj_cartPage.scroll_to_footer()

#             #  Verify text 'SUBSCRIPTION'
#             subscription_text_element = self.obj_cartPage.presence_of_element(cartPageLocator.subscription_text) 
#             self.assertTrue(subscription_text_element,'subscription is not visible')
#             print('subscription is visible') 

#             # enter email address
#             self.obj_cartPage.email_input(TEST_DATA["subscription"]["email"])

#             # click on submit arrow button
#             self.obj_cartPage.click_button(homePageLocator.arrow_button)

#             # verify 'You have been successfully subscribed!' 
#             success_text_element = self.obj_cartPage.presence_of_element(cartPageLocator.success_message) 
#             self.assertTrue(success_text_element,'subscription message is not visible')
#             print('subscription message is visible') 


#         except RuntimeError as e:
#             print(f"Test failed due to error: {e}") 

#     def test_verify_add_products_in_cart(self):
#         '''Test Case 12: Add Products in Cart'''
#         try:
#             # homepage verification
#             homepage_element = self.obj_productPage.presence_of_element(productPageLocator.product_button)
#             self.assertTrue(homepage_element,'page is not visible')
#             print("Homepage is visible")

#             # click products button
#             self.obj_productPage.click_button(productPageLocator.product_button)

#             # Hover over first product and click 'Add to cart'
#             indices = TEST_DATA["products"]["cart_add_indices"]
#             self.obj_productPage.add_product_to_cart_by_index(indices[0])

#             # click on continue shopping button
#             self.obj_productPage.click_button(productPageLocator.continue_shopping_button)

#             # Hover over second product and click 'Add to cart'
#             self.obj_productPage.add_product_to_cart_by_index(indices[1])      
            
#             # Click on 'View Cart' button
#             self.obj_productPage.click_button(productPageLocator.view_cart_button)

#             #  Verify both products are added to Cart
#             product_element = self.obj_cartPage.verify_products_added(TEST_DATA["products"]["expected_cart_count"])
#             self.assertTrue(product_element,"product is not added into cart")
#             print("product is added into cart")

#             # Verify their prices, quantity and total price
#             total_element = self.obj_cartPage.verify_price_quantity_total()
#             self.assertTrue(total_element,"price, quantity, total price is not verified")
#             print("price, quantity, total price are verified")

#         except RuntimeError as e:
#             print(f"Test failed due to error: {e}")  

#     def test_verify_product_quantity_in_cart(self):
#         '''Test Case 13: Verify Product quantity in Cart'''
#         try:
#             # homepage verification
#             homepage_element = self.obj_homePage.presence_of_element(homePageLocator.home_button)
#             self.assertTrue(homepage_element,'page is not visible')
#             print("Homepage is visible")

#             # click view product button
#             self.obj_homePage.click_particular_product_by_name(TEST_DATA["products"]["quantity_product_name"])

#             #  Verify product detail is opened
#             product_detail_page_element = self.obj_productPage.presence_of_element(productPageLocator.product_detail_page_check)
#             self.assertTrue(product_detail_page_element,'user is not landed product detail page')
#             print('user is landed on product detail page')

#             # increase quantity to 4
#             self.obj_productPage.set_quantity(TEST_DATA["products"]["quantity"])

#             # Click 'Add to cart' button
#             self.obj_productPage.click_button(productPageLocator.add_to_cart_btn)

#             # Click 'View Cart' button
#             self.obj_productPage.click_button(productPageLocator.view_cart_button)

#             # Verify that product is displayed in cart page with exact quantity
#             product_quantity_element = self.obj_cartPage.check_product_quantity(TEST_DATA["products"]["quantity"])
#             self.assertTrue(product_quantity_element,'product is displayed in cart page with not exact quantity')
#             print('product is displayed in cart page with exact quantity')


#         except RuntimeError as e:
#             print(f"Test failed due to error: {e}")   

#     def test_verify_place_order_register_while_checkout(self):
#         '''Test Case 14: Place Order: Register while Checkout'''
#         try:
#             # homepage verification
#             homepage_element = self.obj_homePage.presence_of_element(homePageLocator.product_button)
#             self.assertTrue(homepage_element, "Homepage not visible")
#             print("Homepage is visible")

#             # click on product 
#             self.obj_productPage.click_button(productPageLocator.product_button)

#             # Add product to cart
#             self.obj_productPage.add_product_to_cart_by_index(TEST_DATA["products"]["single_add_index"])

#             # click 'Cart' button
#             self.obj_productPage.click_button(productPageLocator.view_cart_button)

#             # Cart page verification
#             cart_page = self.obj_cartPage.presence_of_element(cartPageLocator.cart_rows)
#             self.assertTrue(cart_page, "Cart page not visible")
#             print("Cart page is visible")

#             # Proceed to checkout button click
#             self.obj_cartPage.click_button(cartPageLocator.proceed_to_checkout)

#             # Register / Login button click
#             self.obj_cartPage.click_button(cartPageLocator.register_login_button)

#             # Signup user
#             email_cfg = TEST_DATA["signup"]["email_strategy"]
#             email = f'{email_cfg["prefix"]}{int(time.time())}{email_cfg["domain"]}'
#             self.obj_registerPage.user_signup_input(TEST_DATA["checkout_signup"]["name"], email)
#             self.obj_registerPage.click_button(registerPageLocator.singUp_btn)

#             self.obj_registerPage.fill_acc_form_details(
#                 TEST_DATA["checkout_signup"]["title"],
#                 TEST_DATA["checkout_signup"]["password"],
#                 TEST_DATA["checkout_signup"]["dob"],
#             )
#             cb = TEST_DATA["checkout_signup"]["checkboxes"]
#             self.obj_registerPage.check_the_box(cb["newsletter"], cb["special_offer"])
#             addr = TEST_DATA["checkout_signup"]["address"]
#             self.obj_registerPage.fill_address_form_details(
#                 addr["first_name"],
#                 addr["last_name"],
#                 addr["company"],
#                 addr["address1"],
#                 addr["address2"],
#                 addr["country"],
#                 addr["state"],
#                 addr["city"],
#                 addr["zipcode"],
#                 addr["mobile"],
#             )

#             self.obj_registerPage.click_button(registerPageLocator.address_info_create_account_btn)

#             account_created = self.obj_registerPage.presence_of_element(registerPageLocator.account_created_text)
#             self.assertTrue(account_created, "Account not created")
#             print("Account created successfully")

#             self.obj_registerPage.click_button(registerPageLocator.acc_created_continue_btn)

#             # Logged in verification
#             logged_in = self.obj_registerPage.presence_of_element(registerPageLocator.username_visible_btn)
#             self.assertTrue(logged_in, "User not logged in")
#             print("User logged in successfully")

#             # Cart in  Checkout again
#             # click on cart button
#             self.obj_cartPage.click_button(cartPageLocator.cart_button)

#             # click on proceed to checkout
#             self.obj_cartPage.click_button(cartPageLocator.proceed_to_checkout)

#             # address details verification
#             address_element = self.obj_cartPage.presence_of_element(cartPageLocator.address_details_text)
#             self.assertTrue(address_element, "Address section missing")
#             print("Address section verified")

#             # Review Your Order details verification
#             review_order_element = self.obj_cartPage.presence_of_element(cartPageLocator.review_order_text)
#             self.assertTrue(review_order_element, "Review order section missing")
#             print("Review order section verified")

#             # Place the order
#             self.obj_cartPage.enter_comment_and_place_order(TEST_DATA["order"]["comment"])

#             # Enter payment details
#             pay = TEST_DATA["payment"]
#             self.obj_paymentPage.enter_payment_details(
#                 pay["name_on_card"],
#                 pay["card_number"],
#                 pay["cvc"],
#                 pay["expiry_month"],
#                 pay["expiry_year"],
#             )

#             # Verify success message 'Your order has been placed successfully!'
#             success_element = self.obj_paymentPage.presence_of_element(paymentPageLocator.success_message)
#             self.assertTrue(success_element, "Order not placed successfully")
#             print("Order placed successfully")

#             # Delete account button 
#             self.obj_registerPage.click_button(registerPageLocator.del_acc_btn)

#             #  Verify 'ACCOUNT DELETED!' 
#             deleted_element = self.obj_registerPage.presence_of_element(registerPageLocator.deleted_account_text)
#             self.assertTrue(deleted_element, "Account not deleted")
#             print("Account deleted successfully")

#             # click on continue button
#             self.obj_registerPage.click_button(registerPageLocator.del_acc_continue_btn)

#         except RuntimeError as e:
#             print(f"Test failed due to error: {e}")

#     def test_verify_place_order_register_before_checkout(self):
#         '''Test Case 15: Place Order: Register before Checkout'''
#         try:
#             # homepage verification
#             homepage_element = self.obj_homePage.presence_of_element(homePageLocator.product_button)
#             self.assertTrue(homepage_element, "Homepage not visible")
#             print("Homepage is visible")

#             # click on signup/login 
#             self.obj_registerPage.click_button(registerPageLocator.login_signup)

#             # Signup user
#             email_cfg = TEST_DATA["signup"]["email_strategy"]
#             email = f'{email_cfg["prefix"]}{int(time.time())}{email_cfg["domain"]}'
#             self.obj_registerPage.user_signup_input(TEST_DATA["checkout_signup"]["name"], email)
#             self.obj_registerPage.click_button(registerPageLocator.singUp_btn)

#             self.obj_registerPage.fill_acc_form_details(
#                 TEST_DATA["checkout_signup"]["title"],
#                 TEST_DATA["checkout_signup"]["password"],
#                 TEST_DATA["checkout_signup"]["dob"],
#             )
#             cb = TEST_DATA["checkout_signup"]["checkboxes"]
#             self.obj_registerPage.check_the_box(cb["newsletter"], cb["special_offer"])
#             addr = TEST_DATA["checkout_signup"]["address"]
#             self.obj_registerPage.fill_address_form_details(
#                 addr["first_name"],
#                 addr["last_name"],
#                 addr["company"],
#                 addr["address1"],
#                 addr["address2"],
#                 addr["country"],
#                 addr["state"],
#                 addr["city"],
#                 addr["zipcode"],
#                 addr["mobile"],
#             )

#             self.obj_registerPage.click_button(registerPageLocator.address_info_create_account_btn)

#             account_created = self.obj_registerPage.presence_of_element(registerPageLocator.account_created_text)
#             self.assertTrue(account_created, "Account not created")
#             print("Account created successfully")

#             self.obj_registerPage.click_button(registerPageLocator.acc_created_continue_btn)

#             # Logged in verification
#             logged_in = self.obj_registerPage.presence_of_element(registerPageLocator.username_visible_btn)
#             self.assertTrue(logged_in, "User not logged in")
#             print("User logged in successfully")

#             # Add product to cart
#             self.obj_productPage.add_product_to_cart_by_index(TEST_DATA["products"]["single_add_index"])

#             # click 'Cart' button
#             self.obj_productPage.click_button(productPageLocator.view_cart_button)

#             # Cart page verification
#             cart_page = self.obj_cartPage.presence_of_element(cartPageLocator.cart_rows)
#             self.assertTrue(cart_page, "Cart page not visible")
#             print("Cart page is visible")

#             # Proceed to checkout button click
#             self.obj_cartPage.click_button(cartPageLocator.proceed_to_checkout)

#             # address details verification
#             address_element = self.obj_cartPage.presence_of_element(cartPageLocator.address_details_text)
#             self.assertTrue(address_element, "Address section missing")
#             print("Address section verified")

#             # Review Your Order details verification
#             review_order_element = self.obj_cartPage.presence_of_element(cartPageLocator.review_order_text)
#             self.assertTrue(review_order_element, "Review order section missing")
#             print("Review order section verified")

#             # Place the order
#             self.obj_cartPage.enter_comment_and_place_order(TEST_DATA["order"]["comment"])

#             # Enter payment details
#             pay = TEST_DATA["payment"]
#             self.obj_paymentPage.enter_payment_details(
#                 pay["name_on_card"],
#                 pay["card_number"],
#                 pay["cvc"],
#                 pay["expiry_month"],
#                 pay["expiry_year"],
#             )

#             # Verify success message 'Your order has been placed successfully!'
#             success_element = self.obj_paymentPage.presence_of_element(paymentPageLocator.success_message)
#             self.assertTrue(success_element, "Order not placed successfully")
#             print("Order placed successfully")

#             # Delete account button 
#             self.obj_registerPage.click_button(registerPageLocator.del_acc_btn)

#             #  Verify 'ACCOUNT DELETED!' 
#             deleted_element = self.obj_registerPage.presence_of_element(registerPageLocator.deleted_account_text)
#             self.assertTrue(deleted_element, "Account not deleted")
#             print("Account deleted successfully")

#             # click on continue button
#             self.obj_registerPage.click_button(registerPageLocator.del_acc_continue_btn)

#         except RuntimeError as e:
#             print(f"Test failed due to error: {e}")

#     def test_verify_place_order_login_before_checkout(self):
#         '''Test Case 16: Place Order: Login before Checkout'''
#         try:
#             # homepage verification
#             homepage_element = self.obj_homePage.presence_of_element(homePageLocator.product_button)
#             self.assertTrue(homepage_element, "Homepage not visible")
#             print("Homepage is visible")

#             # click on signup/login 
#             self.obj_registerPage.click_button(registerPageLocator.login_signup)

#             login_element = self.obj_loginPage.presence_of_element(loginPageLocator.login_page_text)
#             self.assertTrue(login_element, "login page is not visible")

#             # Create a fresh account with address details, then login with it (rerunnable)
#             email, password = self.obj_registerPage.create_account(
#                 TEST_DATA["checkout_signup"],
#                 TEST_DATA["signup"]["email_strategy"],
#             )
#             self.obj_loginPage.click_button(loginPageLocator.logout_button)

#             login_element = self.obj_loginPage.presence_of_element(loginPageLocator.login_page_text)
#             self.assertTrue(login_element, "login page is not visible after logout")

#             # enter the the login details and click on the login button   
#             self.obj_loginPage.user_login_input(email, password)
#             self.obj_loginPage.click_button(loginPageLocator.login_btn)

#             # Logged in verification
#             logged_in = self.obj_registerPage.presence_of_element(registerPageLocator.username_visible_btn)
#             self.assertTrue(logged_in, "User not logged in")
#             print("User logged in successfully")

#             # Add product to cart
#             self.obj_productPage.add_product_to_cart_by_index(TEST_DATA["products"]["single_add_index"])

#             # click 'Cart' button
#             self.obj_productPage.click_button(productPageLocator.view_cart_button)

#             # Cart page verification
#             cart_page = self.obj_cartPage.presence_of_element(cartPageLocator.cart_rows)
#             self.assertTrue(cart_page, "Cart page not visible")
#             print("Cart page is visible")

#             # Proceed to checkout button click
#             self.obj_cartPage.click_button(cartPageLocator.proceed_to_checkout)

#             # address details verification
#             address_element = self.obj_cartPage.presence_of_element(cartPageLocator.address_details_text)
#             self.assertTrue(address_element, "Address section missing")
#             print("Address section verified")

#             # Review Your Order details verification
#             review_order_element = self.obj_cartPage.presence_of_element(cartPageLocator.review_order_text)
#             self.assertTrue(review_order_element, "Review order section missing")
#             print("Review order section verified")

#             # Place the order
#             self.obj_cartPage.enter_comment_and_place_order(TEST_DATA["order"]["comment"])

#             # Enter payment details
#             pay = TEST_DATA["payment"]
#             self.obj_paymentPage.enter_payment_details(
#                 pay["name_on_card"],
#                 pay["card_number"],
#                 pay["cvc"],
#                 pay["expiry_month"],
#                 pay["expiry_year"],
#             )

#             # Verify success message 'Your order has been placed successfully!'
#             success_element = self.obj_paymentPage.presence_of_element(paymentPageLocator.success_message)
#             self.assertTrue(success_element, "Order not placed successfully")
#             print("Order placed successfully")

#             # Delete account button 
#             self.obj_registerPage.click_button(registerPageLocator.del_acc_btn)

#             #  Verify 'ACCOUNT DELETED!' 
#             deleted_element = self.obj_registerPage.presence_of_element(registerPageLocator.deleted_account_text)
#             self.assertTrue(deleted_element, "Account not deleted")
#             print("Account deleted successfully")

#             # click on continue button
#             self.obj_registerPage.click_button(registerPageLocator.del_acc_continue_btn)

#         except RuntimeError as e:
#             print(f"Test failed due to error: {e}")

#     def test_verify_place_remove_products_from_cart(self):
#         '''Test Case 17: Remove Products From Cart'''
#         try:
#             # homepage verification
#             homepage_element = self.obj_homePage.presence_of_element(homePageLocator.product_button)
#             self.assertTrue(homepage_element, "Homepage not visible")
#             print("Homepage is visible")

#             # click products button
#             self.obj_productPage.click_button(productPageLocator.product_button)
            
#             # Add product to cart
#             indices = TEST_DATA["products"]["cart_add_indices"]
#             self.obj_productPage.add_product_to_cart_by_index(indices[0])

#             # click on continue shopping button
#             self.obj_productPage.click_button(productPageLocator.continue_shopping_button)

#             # Hover over second product and click 'Add to cart'
#             self.obj_productPage.add_product_to_cart_by_index(indices[1])      

#             # click 'Cart' button
#             self.obj_productPage.click_button(productPageLocator.view_cart_button)

#             # Cart page verification
#             cart_page = self.obj_cartPage.presence_of_element(cartPageLocator.cart_rows)
#             self.assertTrue(cart_page, "Cart page not visible")
#             print("Cart page is visible")

#             # Click 'X' button corresponding to particular product
#             self.obj_cartPage.remove_product()

#             # Verify that product is removed from the cart
#             empty_element = self.obj_cartPage.presence_of_element(cartPageLocator.empty_cart_text)
#             self.assertTrue(empty_element,'product is not removed from the cart')
#             print("product is successfully removed from the cart")


#         except RuntimeError as e:
#             print(f"Test failed due to error: {e}")
            
#     def test_verify_view_category_products(self):
#         '''Test Case 18: View Category Products'''
#         try:
#             #  Verify that categories are visible on left side bar
#             categories_visible = self.obj_productPage.presence_of_element(productPageLocator.category_section_header)
#             self.assertTrue(categories_visible, "categories sidebar is not visible")
#             print("Categories sidebar is visible")

#             #  Click on any category link under 'Women' category, for example: Dress
#             cat1 = TEST_DATA["categories"]["first"]
#             self.obj_productPage.select_category(cat1["main"], cat1["sub"])

#             # Verify that category page is displayed and confirm text 'WOMEN - TOPS PRODUCTS'
#             women_category_visible = self.obj_productPage.is_category_page_displayed(cat1["header"])
#             self.assertTrue(women_category_visible, "Women Tops category page is not visible")
#             print("Women Tops category page is visible")

#             # Click on any category link under 'Men' category, for example: Tshirts
#             cat2 = TEST_DATA["categories"]["second"]
#             self.obj_productPage.select_category(cat2["main"], cat2["sub"])

#             # Verify that category page is displayed and confirm text 'MEN - TOPS PRODUCTS'
#             men_category_visible = self.obj_productPage.is_category_page_displayed(cat2["header"])
#             self.assertTrue(men_category_visible, "Men Tshirts category page is not visible")
#             print("Men Tshirts category page is visible")

#         except RuntimeError as e:
#             print(f"Test failed due to error: {e}") 

#     def test_verify_view_brand_products(self):
#         '''Test Case 19: View & Cart Brand Products'''
#         try:
#             # click on  Products page
#             self.obj_productPage.click_button(productPageLocator.product_button)

#             # brand sidebar section verification
#             brands_visible = self.obj_productPage.presence_of_element(productPageLocator.brand_section_header)
#             self.assertTrue(brands_visible, "Brands sidebar is not visible")
#             print("Brands sidebar is visible")

#             # click first brand
#             brand1 = TEST_DATA["brands"]["first"]
#             self.obj_productPage.click_button(productPageLocator.brand_link_by_name.format(brand_name=brand1))

#             #  Verify that user is navigated to POLO page 
#             brand_one_header = self.obj_productPage.presence_of_element(productPageLocator.brand_page_header.format(brand_name=brand1))
#             self.assertTrue(brand_one_header, "Polo brand page not visible")

#             # Verify POLO brand products are displayed
#             brand_one_products = self.obj_productPage.presence_of_element(productPageLocator.brand_products)
#             self.assertTrue(brand_one_products, "Polo brand products not visible")
#             print("Polo brand products are visible")

#             # click another brand
#             brand2 = TEST_DATA["brands"]["second"]
#             self.obj_productPage.click_button(productPageLocator.brand_link_by_name.format(brand_name=brand2))

#             #  Verify that user is navigated to H&M page 
#             brand_two_header = self.obj_productPage.presence_of_element(productPageLocator.brand_page_header.format(brand_name=brand2))
#             self.assertTrue(brand_two_header, "H&M brand page not visible")

#             # Verify H&M brand products are displayed
#             brand_two_products = self.obj_productPage.presence_of_element(productPageLocator.brand_products)
#             self.assertTrue(brand_two_products, "H&M brand products not visible")
#             print("H&M brand products are visible")

#         except RuntimeError as e:
#             print(f"Test failed due to error: {e}")

#     def test_verify_search_products_cart_after_login(self):
#         '''Test Case 20: Search Products and Verify Cart After Login'''
#         try:
#             # click Products page
#             self.obj_productPage.click_button(productPageLocator.product_button)

#             #  Verify user is navigated to ALL PRODUCTS page successfully
#             all_products = self.obj_productPage.presence_of_element(productPageLocator.product_page_text)
#             self.assertTrue(all_products, "ALL PRODUCTS page is not visible")
#             print("ALL PRODUCTS page is visible")

#             # search for product
#             keyword = TEST_DATA["search"]["keyword"]
#             self.obj_productPage.search_product(keyword)

#             # Verify 'SEARCHED PRODUCTS' is visible
#             searched_text = self.obj_productPage.presence_of_element(productPageLocator.searched_products_text)
#             self.assertTrue(searched_text, "'SEARCHED PRODUCTS' not visible")
#             print("'SEARCHED PRODUCTS' is visible")

#             # Verify all the products related to search are visible
#             valid_results = self.obj_productPage.validate_searched_products(keyword)
#             self.assertTrue(valid_results, "Search results contain unrelated products")
#             print("Search results are valid")

#             # add first searched products to cart 
#             indices = TEST_DATA["products"]["cart_add_indices"]
#             self.obj_productPage.add_product_to_cart_by_index(indices[0])

#             # click on continue shopping button
#             self.obj_productPage.click_button(productPageLocator.continue_shopping_button)

#             # add second searched products to cart
#             self.obj_productPage.add_product_to_cart_by_index(indices[1])

#             # click on view cart button
#             self.obj_productPage.click_button(productPageLocator.view_cart_button)

#             # verify that products are visible in cart before login
#             items_before_login = self.obj_cartPage.verify_products_added(TEST_DATA["products"]["expected_cart_count"])
#             self.assertTrue(items_before_login, "Products not visible in cart before login")
#             print("Products are visible in cart before login")

#             # Click 'Signup / Login' button
#             self.obj_registerPage.click_button(registerPageLocator.login_signup)

#             # submit login credentials
#             login = TEST_DATA["login"]["valid"]
#             self.obj_loginPage.user_login_input(login["email"], login["password"])
#             self.obj_loginPage.click_button(loginPageLocator.login_btn)

#             # click on cart button
#             self.obj_cartPage.click_button(cartPageLocator.cart_button)

#             # verify that products are visible in cart after login
#             items_after_login = self.obj_cartPage.verify_products_added(TEST_DATA["products"]["expected_cart_count"])
#             self.assertTrue(items_after_login, "Products not visible in cart after login")
#             print("Products are visible in cart after login")

#         except RuntimeError as e:
#             print(f"Test failed due to error: {e}")   

#     def test_verify_add_review_on_product(self):
#         '''Test Case 21: Add review on product'''
#         try:
#             # Click on 'Products' button
#             self.obj_productPage.click_button(productPageLocator.product_button)

#             # Verify user is navigated to ALL PRODUCTS page successfully
#             all_products = self.obj_productPage.presence_of_element(productPageLocator.product_page_text)
#             self.assertTrue(all_products, "ALL PRODUCTS page is not visible")
#             print("ALL PRODUCTS page is visible")

#             # Click on first 'View Product' button 
#             first_view_product = f"({productPageLocator.all_product_view_page_button})[1]"
#             self.obj_productPage.click_button(first_view_product)

#             # Verify 'Write Your Review' is visible
#             review_title = self.obj_productPage.presence_of_element(productPageLocator.write_your_review_text)
#             self.assertTrue(review_title, "'Write Your Review' is not visible")
#             print("'Write Your Review' is visible")

#             # Enter name, email and review and submit
#             review = TEST_DATA["review"]
#             self.obj_productPage.submit_review(review["name"], review["email"], review["text"])

#             # Verify success message 'Thank you for your review.'
#             success = self.obj_productPage.presence_of_element(productPageLocator.review_success_message)
#             self.assertTrue(success, "Review success message not visible")
#             print("Thank you for your review. is visible")

#         except RuntimeError as e:
#             print(f"Test failed due to error: {e}")

#     def test_verify_add_to_cart_from_recommended_items(self):
#         '''Test Case 22: Add to cart from Recommended items'''
#         try:
#             # Homepage visible
#             homepage_visible = self.obj_homePage.presence_of_element(homePageLocator.product_button)
#             self.assertTrue(homepage_visible, "Homepage is not visible")
#             print("Homepage is visible")

#             # Scroll to bottom of page
#             self.obj_homePage.scroll_to_footer()

#             # Verify 'RECOMMENDED ITEMS' are visible
#             recommended_visible = self.obj_homePage.presence_of_element(homePageLocator.recommended_items_text)
#             self.assertTrue(recommended_visible, "'RECOMMENDED ITEMS' is not visible")
#             print("'RECOMMENDED ITEMS' is visible")

#             # Click on 'Add To Cart' on Recommended product
#             self.obj_homePage.click_particular_product_by_index(1)

#             # Click on 'View Cart' button 
#             self.obj_productPage.click_button(productPageLocator.view_cart_button)

#             # Verify that product is displayed in cart page
#             cart_has_product = self.obj_cartPage.presence_of_element(cartPageLocator.cart_rows)
#             self.assertTrue(cart_has_product, "Product is not displayed in cart")
#             print("Product is displayed in cart")

#         except RuntimeError as e:
#             print(f"Test failed due to error: {e}")

#     def test_verify_address_details_in_checkout_page(self):
#         '''Test Case 23: Verify address details in checkout page'''
#         try:
#             # Verify home page is visible
#             homepage_visible = self.obj_homePage.presence_of_element(homePageLocator.product_button)
#             self.assertTrue(homepage_visible, "Home page is not visible")
#             print("Home page is visible")

#             # Click Signup / Login
#             self.obj_registerPage.click_button(registerPageLocator.login_signup)

#             # Signup and create account process
#             email_cfg = TEST_DATA["signup"]["email_strategy"]
#             email = f'{email_cfg["prefix"]}{int(time.time())}{email_cfg["domain"]}'
#             self.obj_registerPage.user_signup_input(TEST_DATA["checkout_signup"]["name"], email)
#             self.obj_registerPage.click_button(registerPageLocator.singUp_btn)

#             # Fill account info and address info
#             self.obj_registerPage.fill_acc_form_details(
#                 TEST_DATA["checkout_signup"]["title"],
#                 TEST_DATA["checkout_signup"]["password"],
#                 TEST_DATA["checkout_signup"]["dob"],
#             )
#             cb = TEST_DATA["checkout_signup"]["checkboxes"]
#             self.obj_registerPage.check_the_box(cb["newsletter"], cb["special_offer"])

#             addr = TEST_DATA["checkout_signup"]["address"]
#             self.obj_registerPage.fill_address_form_details(
#                 addr["first_name"],
#                 addr["last_name"],
#                 addr["company"],
#                 addr["address1"],
#                 addr["address2"],
#                 addr["country"],
#                 addr["state"],
#                 addr["city"],
#                 addr["zipcode"],
#                 addr["mobile"],
#             )

#             self.obj_registerPage.click_button(registerPageLocator.address_info_create_account_btn)

#             # Verify ACCOUNT CREATED and Continue
#             created = self.obj_registerPage.presence_of_element(registerPageLocator.account_created_text)
#             self.assertTrue(created, "ACCOUNT CREATED! is not visible")
#             print("ACCOUNT CREATED! is visible")

#             self.obj_registerPage.click_button(registerPageLocator.acc_created_continue_btn)

#             # Verify Logged in as username
#             logged_in = self.obj_registerPage.presence_of_element(registerPageLocator.username_visible_btn)
#             self.assertTrue(logged_in, "Logged in as username is not visible")
#             print("Logged in as username is visible")

#             # Add product to cart
#             self.obj_productPage.click_button(productPageLocator.product_button)
#             self.obj_productPage.add_product_to_cart_by_index(TEST_DATA["products"]["single_add_index"])
#             self.obj_productPage.click_button(productPageLocator.view_cart_button)

#             # Verify cart page displayed
#             cart_visible = self.obj_cartPage.presence_of_element(cartPageLocator.cart_rows)
#             self.assertTrue(cart_visible, "Cart page is not visible")
#             print("Cart page is visible")

#             # Proceed to checkout
#             self.obj_cartPage.click_button(cartPageLocator.proceed_to_checkout)

#             # Verify address section visible
#             address_section = self.obj_cartPage.presence_of_element(cartPageLocator.address_details_text)
#             self.assertTrue(address_section, "Address Details section is not visible")
#             print("Address Details section is visible")

#             # Verify delivery address matches registration address
#             delivery_text = self.obj_cartPage.get_delivery_address_text()
#             self.assertTrue(addr["address1"] in delivery_text, "Delivery address1 not matching")
#             self.assertTrue(addr["address2"] in delivery_text, "Delivery address2 not matching")
#             self.assertTrue(addr["country"] in delivery_text, "Delivery country not matching")
#             self.assertTrue(addr["state"] in delivery_text, "Delivery state not matching")
#             self.assertTrue(addr["city"] in delivery_text, "Delivery city not matching")
#             self.assertTrue(addr["zipcode"] in delivery_text, "Delivery zipcode not matching")
#             self.assertTrue(addr["mobile"] in delivery_text, "Delivery mobile not matching")
#             print("Delivery address matches registration address")

#             # Verify billing address matches registration address
#             billing_text = self.obj_cartPage.get_billing_address_text()
#             self.assertTrue(addr["address1"] in billing_text, "Billing address1 not matching")
#             self.assertTrue(addr["address2"] in billing_text, "Billing address2 not matching")
#             self.assertTrue(addr["country"] in billing_text, "Billing country not matching")
#             self.assertTrue(addr["state"] in billing_text, "Billing state not matching")
#             self.assertTrue(addr["city"] in billing_text, "Billing city not matching")
#             self.assertTrue(addr["zipcode"] in billing_text, "Billing zipcode not matching")
#             self.assertTrue(addr["mobile"] in billing_text, "Billing mobile not matching")
#             print("Billing address matches registration address")

#             # click Delete account button
#             self.obj_registerPage.click_button(registerPageLocator.del_acc_btn)

#             # Verify 'ACCOUNT DELETED!' and click 'Continue' button
#             deleted = self.obj_registerPage.presence_of_element(registerPageLocator.deleted_account_text)
#             self.assertTrue(deleted, "ACCOUNT DELETED! is not visible")
#             print("ACCOUNT DELETED! is visible")

#             self.obj_registerPage.click_button(registerPageLocator.del_acc_continue_btn)

#         except RuntimeError as e:
#             print(f"Test failed due to error: {e}")  

#     def test_verify_Download_Invoice_after_purchase_order(self):
#         '''Test Case 24: Download Invoice after purchase order'''
#         try:
#             # Verify home page is visible
#             homepage_visible = self.obj_homePage.presence_of_element(homePageLocator.product_button)
#             self.assertTrue(homepage_visible, "Home page is not visible")
#             print("Home page is visible")

#             # Add product to cart
#             self.obj_productPage.click_button(productPageLocator.product_button)
#             self.obj_productPage.add_product_to_cart_by_index(TEST_DATA["products"]["single_add_index"])
#             self.obj_productPage.click_button(productPageLocator.view_cart_button)

#             # Verify cart page displayed
#             cart_visible = self.obj_cartPage.presence_of_element(cartPageLocator.cart_rows)
#             self.assertTrue(cart_visible, "Cart page is not visible")
#             print("Cart page is visible")

#             # Proceed to checkout
#             self.obj_cartPage.click_button(cartPageLocator.proceed_to_checkout)

#             # Register / Login button click
#             self.obj_cartPage.click_button(cartPageLocator.register_login_button)

#             # Signup user
#             email_cfg = TEST_DATA["signup"]["email_strategy"]
#             email = f'{email_cfg["prefix"]}{int(time.time())}{email_cfg["domain"]}'
#             self.obj_registerPage.user_signup_input(TEST_DATA["checkout_signup"]["name"], email)
#             self.obj_registerPage.click_button(registerPageLocator.singUp_btn)

#             self.obj_registerPage.fill_acc_form_details(
#                 TEST_DATA["checkout_signup"]["title"],
#                 TEST_DATA["checkout_signup"]["password"],
#                 TEST_DATA["checkout_signup"]["dob"],
#             )
#             cb = TEST_DATA["checkout_signup"]["checkboxes"]
#             self.obj_registerPage.check_the_box(cb["newsletter"], cb["special_offer"])

#             addr = TEST_DATA["checkout_signup"]["address"]
#             self.obj_registerPage.fill_address_form_details(
#                 addr["first_name"],
#                 addr["last_name"],
#                 addr["company"],
#                 addr["address1"],
#                 addr["address2"],
#                 addr["country"],
#                 addr["state"],
#                 addr["city"],
#                 addr["zipcode"],
#                 addr["mobile"],
#             )

#             self.obj_registerPage.click_button(registerPageLocator.address_info_create_account_btn)

#             account_created = self.obj_registerPage.presence_of_element(registerPageLocator.account_created_text)
#             self.assertTrue(account_created, "Account not created")
#             print("Account created successfully")

#             self.obj_registerPage.click_button(registerPageLocator.acc_created_continue_btn)

#             # Verify Logged in as username
#             logged_in = self.obj_registerPage.presence_of_element(registerPageLocator.username_visible_btn)
#             self.assertTrue(logged_in, "Logged in as username is not visible")
#             print("Logged in as username is visible")

#             # click on cart button
#             self.obj_cartPage.click_button(cartPageLocator.cart_button)

#             # click on proceed to checkout
#             self.obj_cartPage.click_button(cartPageLocator.proceed_to_checkout)

#             # address details verification
#             address_element = self.obj_cartPage.presence_of_element(cartPageLocator.address_details_text)
#             self.assertTrue(address_element, "Address section missing")
#             print("Address section verified")

#             # Review Your Order details verification
#             review_order_element = self.obj_cartPage.presence_of_element(cartPageLocator.review_order_text)
#             self.assertTrue(review_order_element, "Review order section missing")
#             print("Review order section verified")

#             # Place the order
#             self.obj_cartPage.enter_comment_and_place_order(TEST_DATA["order"]["comment"])

#             # Enter payment details
#             pay = TEST_DATA["payment"]
#             self.obj_paymentPage.enter_payment_details(
#                 pay["name_on_card"],
#                 pay["card_number"],
#                 pay["cvc"],
#                 pay["expiry_month"],
#                 pay["expiry_year"]
#             )

#             # Verify success message 'Your order has been placed successfully!'
#             success_element = self.obj_paymentPage.presence_of_element(paymentPageLocator.success_message)
#             self.assertTrue(success_element, "Order not placed successfully")
#             print("Order placed successfully")
            
#             # Click 'Download Invoice' button and verify invoice is downloaded successfully.
#             invoice_downloaded = self.obj_paymentPage.download_invoice(self.download_path)
#             self.assertTrue(invoice_downloaded, "Invoice not downloaded")
#             print("Invoice downloaded successfully")

#             # click on continue button
#             self.obj_paymentPage.click_button(paymentPageLocator.payment_page_continue_button)
   
#             # delete account click    
#             self.obj_registerPage.click_button(registerPageLocator.del_acc_btn)   

#             # account deletion verification 
#             del_continue_element = self.obj_registerPage.presence_of_element(registerPageLocator.deleted_account_text)
#             self.assertTrue(del_continue_element,'error while deleting account')
#             print('account deleted successfully')

#             # continue button click on deleted account page 
#             self.obj_registerPage.click_button(registerPageLocator.del_acc_continue_btn) 

#         except RuntimeError as e:
#             print(f"Test failed due to error: {e}")

#     def test_verify_scroll_up_using_arrow_button_and_scroll_down_functionality(self):
#         '''Test Case 25: Verify Scroll Up using 'Arrow' button and Scroll Down functionality'''
#         try:
#             # homepage verification
#             homepage_element = self.obj_homePage.presence_of_element(homePageLocator.product_button)
#             self.assertTrue(homepage_element,'page is not visible')
#             print("Homepage is visible")

#             # scroll to footer 
#             self.obj_homePage.scroll_to_footer()

#             #  Verify text 'SUBSCRIPTION'
#             subscription_text_element = self.obj_homePage.presence_of_element(homePageLocator.subscription_text) 
#             self.assertTrue(subscription_text_element,'subscription is not visible')
#             print('subscription is visible') 

#             #  Click on arrow at bottom right side to move upward
#             self.obj_homePage.click_button(homePageLocator.bottom_to_top_arrow_button)

#             # Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen
#             top_banner_text_element = self.obj_homePage.presence_of_element(homePageLocator.top_banner_text) 
#             self.assertTrue(top_banner_text_element,"Top banner text is not visible after scrolling up")
#             print('Top banner text is visible after scrolling up and Scroll up functionality working properly') 


#         except RuntimeError as e:
#             print(f"Test failed due to error: {e}")  
          
#     def test_verify_scroll_up_without_arrow_button_and_scroll_down_functionality(self):
#         '''Test Case 26: Verify Scroll Up without 'Arrow' button and Scroll Down functionality'''
#         try:
#             # homepage verification
#             homepage_element = self.obj_homePage.presence_of_element(homePageLocator.product_button)
#             self.assertTrue(homepage_element,'page is not visible')
#             print("Homepage is visible")

#             # scroll to footer 
#             self.obj_homePage.scroll_to_footer()

#             #  Verify text 'SUBSCRIPTION'
#             subscription_text_element = self.obj_homePage.presence_of_element(homePageLocator.subscription_text) 
#             self.assertTrue(subscription_text_element,'subscription is not visible')
#             print('subscription is visible') 

#             #  scroll up page to top
#             self.obj_homePage.scroll_to_top()

#             # Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen
#             top_banner_text_element = self.obj_homePage.presence_of_element(homePageLocator.subscription_text) 
#             self.assertTrue(top_banner_text_element,"Top banner text is not visible after scrolling up")
#             print('Top banner text is visible after scrolling up and Scroll up functionality working properly') 


#         except RuntimeError as e:
#             print(f"Test failed due to error: {e}")            





