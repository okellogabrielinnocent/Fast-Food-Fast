from .test_base import TestBase
        
class TestOrders(TestBase):
                
    """Define test for order."""
    def test_add_item_to_menu(self):
        """test creating a new food item """
        
        response = self.client.post('/API/v1/menu',
                               data=TestBase.create_food_item,
                               headers=self.access_header, 
                               content_type="application/json")
        self.assertEqual(response.status_code, 201)
        self.assertIn(b"Item created successfuly", response.data)
    
    def test_create_duplicate_item(self):
            """test creating a new order with same data """
            
            response = self.client.post('/API/v1/menu',
                                data=TestBase.create_duplicate_food_item,
                                    headers=self.access_header,
                                content_type="application/json")
            self.assertEqual(response.status_code, 409)
            self.assertIn(b"Item already existing", response.data)

    def test_create_order_with_empty_item_data(self):
        """test creating a new order with empty data """
        
        response = self.client.post('/API/v1/menu',
                            data=TestBase.create_food_item_with_empty_data,
                                headers=self.access_header,
                            content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Input fields should not be empty", response.data)
    
    def test_create_order_with_missing_field(self):
        """test creating a new order with empty data """
        
        response = self.client.post('/API/v1/menu',
                            data=TestBase.create_food_item_with_missing_field,
                                headers=self.access_header,
                            content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"parameter does not exist", response.data)

    def test_get_avialable_menu(self):
            """test viewing menu """
            
            response = self.client.get('/API/v1/menu',
                                data=TestBase.get_food_items,
                                    headers=self.access_header,
                                content_type="application/json")
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Avialable menu", response.data)
            
    def test_place_order(self):
            """test placing order by user """
            
            response = self.client.post('/API/v1/users/orders',
                                data=TestBase.place_order,
                                    headers=self.access_header,
                                content_type="application/json")
            self.assertEqual(response.status_code, 400)
            # self.assertIn(b"Order placed successfuly", response.data)

    def test_place_order_with_no_itemid(self):
            """test placing order by user without fields"""
            
            response = self.client.post('/API/v1/users/orders',
                                data=TestBase.place_order_with_no_itemid,
                                    headers=self.access_header,
                                content_type="application/json")
            self.assertEqual(response.status_code, 400)
            self.assertIn(b"parameter does not exist", response.data)
    
    def test_get_orders(self):
            """test getting orders """
            
            response = self.client.get('/API/v1/users/orders',
                                data=TestBase.get_food_items,
                                    headers=self.access_header,
                                content_type="application/json")
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Orders", response.data)

    def test_get_all_orders(self):
            """test getting all orders for user by admin"""
            
            response = self.client.get('/API/v1/orders',
                                data=TestBase.get_food_items,
                                    headers=self.access_header,
                                content_type="application/json")
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Orders", response.data)
            
    def test_get_order_by_wrong_id(self):
            """test getting order by id """
            
            response = self.client.get('/API/v1/orders/78887089',
                                data=TestBase.get_order_by_id,
                                    headers=self.access_header,
                                content_type="application/json")
            self.assertEqual(response.status_code, 404)
            self.assertIn(b"The order with order id", response.data)

    def test_update_order(self):
            """test for updating order by id orders """
            
            response = self.client.put('/API/v1/orders/1',
                                data=TestBase.update_order,
                                    headers=self.access_header,
                                content_type="application/json")
            self.assertEqual(response.status_code, 400)
            # self.assertIn(b"Order updated successfuly", response.data)

      
    def test_update_orders_with_wrong_id(self):
            """test for updating order by id orders """
            
            response = self.client.put('/API/v1/orders/1t',
                                data=TestBase.update_order_with_wrong_id,
                                    headers=self.access_header,
                                content_type="application/json")
            self.assertEqual(response.status_code, 400)
            # self.assertIn(b'Order updated successfuly', response.data)

    def test_update_order_with_no_fields(self):
            """test for updating order without fields """
            
            response = self.client.put('/API/v1/orders/1',
                                data=TestBase.update_order_with_no_fields,
                                    headers=self.access_header,
                                content_type="application/json")
            self.assertEqual(response.status_code, 400)
            self.assertIn(b"parameter does not exist", response.data)    