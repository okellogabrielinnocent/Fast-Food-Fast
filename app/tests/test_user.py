from .test_base import TestBase



class UserTesting(TestBase):
    """class for testing user sign up and login"""

    def test_create_user(self):
        """test registering a new user """
        
        response = self.client.post('/API/v1/auth/user/signup',
                               data=TestBase.create_user,
                               content_type="application/json")
        self.assertEqual(response.status_code, 201)
        self.assertIn(b"User registered successfuly", response.data)

    def test_duplicate_username(self):
        """test method to check duplication"""
        
        response = self.client.post('/API/v1/auth/user/signup',
                               data=TestBase.duplicate_user,
                               content_type="application/json")
        self.assertEqual(response.status_code, 409)
        self.assertIn(b"Username is already existing",response.data)
            
    def test__user_missing_user_name(self):
        """test method to validate missing field"""
        
        response = self.client.post('/API/v1/auth/user/signup',
                               data=TestBase.missing_username_field,
                               content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"field is missing", response.data)
    def test__empty_username(self):
        """test method to validate empty username"""
        
        response = self.client.post('/API/v1/auth/user/signup',
                               data=TestBase.empty_username,
                               content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Username can not be empty",response.data)
    
    def test_number_username(self):
        """test method to validate username(numbers)"""
        
        response = self.client.post('/API/v1/auth/user/signup',
                               data=TestBase.validate_number_in_field,
                               content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Username can not numbers",response.data)
    def test_password_validation(self):
        """test method for password validation"""
        
        # response = self.client.post('/API/v1/auth/user/signup',
        #                        data=TestBase.invalidpassword,
        #                        content_type="application/json")
        # self.assertEqual(response.status_code, 400)
        # self.assertIn(b"invalid password data", response.data)

    def test_login(self):
        """test method to login a user"""
        
        response = self.client.post('/API/v1/auth/login',
                                    data=TestBase.user_login,
                                    content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Login successful", response.data)
    
    def test_login_with_wrong_credentials(self):
        """test method to login a user with wrong credentials"""
        
        response = self.client.post('/API/v1/auth/login',
                                    data=TestBase.login_wrong_credentials,
                                    content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"field is missing", response.data)

    def test_login_with_wrong_user_credentials(self):
        """test method to login a user with wrong credentials"""
        
        response = self.client.post('/API/v1/auth/login',
                                    data=TestBase.login_wrong_credentials,
                                    content_type="application/json")
        # self.assertEqual(response.status_code, 404)
        self.assertIn(b"Username or password is not valid", response.data)