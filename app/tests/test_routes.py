from .test_base import TestBase
        
class TestRoutes(TestBase):
                
    """Define test Routes and methods ."""
    
    def test_page_not_found(self):
        response = self.client.put('/api/v1/')
        self.assertEqual(response.status_code,404)
        self.assertIn(b'The URL you have added is wrong', response.data)
    
    def test_method_not_allowed(self):
        response = self.client.put('/API/v1/auth/user/signup')
        self.assertEqual(response.status_code,405)
        self.assertIn(b'The method used is not allowed', response.data)
