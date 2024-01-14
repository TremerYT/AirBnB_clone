#!/usr/bin/python3

"""
This is a unittest for BaseModel class
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
import os


class Test_Base_model (unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_init(self):
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))
        
    def test_save(self):
        initial_update= self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(initial_update, self.base_model.updated_at)

    def test_to_dict(self):
        model_diction = self.base_model.to_dict()
        self.assertIsInstance(model_diction, dict)
        self.assertEqual(model_diction['__class__'], 'BaseModel')
        self.assertIn('id', model_diction)
        self.assertIn('created_at', model_diction)
        self.assertIn('updated_at', model_diction)
        
    def test_str_(self):
        string_representation = str(self.base_model)
        self.assertIn("[BaseModel]", string_representation)
        self.assertIn("id", string_representation)
        self.assertIn("created_at", string_representation)
        self.assertIn("updated_at", string_representation)
        
        
if __name__ == '__main__':
    unittest.main()
