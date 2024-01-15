#!/usr/bin/python3
"""This is the test for the amenity"""
import unittest
from datetime import datetime as dt
import os
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Thiscontains functions"""
    def setUp(self):
        """This initializes static values"""
        self.amenity = Amenity
        self.funcList = dir(self.amenity())

    def test_functionExists(self):
        """This checks for amenity function"""
        modelList = [
            "__init__",
            "__str__",
            "save",
            "to_dict"
        ]
        for i in modelList:
            self.assertTrue(i in self.funcList)

    def test_instances1(self):
        """This doesnt initialize with args"""
        self.amenity(["hello", "man", "boy"])
        self.assertNotEqual(self.amenity().id, "hello")

    def test_instance2(self):
        """This initializes a dictionary"""
        newInstan = {
            "id": "b213d458-36b3-460b-ab99-84e82785be04",
            "created_at": "2024-01-12T08:38:06.286695",
            "updated_at": "2024-01-12T08:38:06.288367"
        }
        temp = self.amenity(**newIns)
        self.assertEqual(newInstan["id"], temp.id)
        self.assertEqual(dt.fromisoformat(
            newInstan["created_at"]), temp.created_at)
        self.assertEqual(dt.fromisoformat(
            newInstan["updated_at"]), temp.updated_at)

    def test_instance3(self):
        """This checks for value type"""
        self.assertTrue(type(self.amenity().id), str)
        self.assertTrue(type(self.amenity().created_at), dt)
        self.assertTrue(type(self.amenity().updated_at), dt)

    def test_strRep(self):
        """This checks for the type value"""
        self.assertTrue(type(
            self.amenity().__str__()), str)

    def test_save1(self):
        """This Checks the type value of updated_at after save function"""
        temp = self.amenity()
        temp.save()
        self.assertTrue(type(temp.updated_at), dt)

    def test_save2(self):
        """This Checks if database exists after calling save function"""
        self.amenity().save()
        osList = os.listdir()
        self.assertTrue("file.json" in osList)

    def test_to_dict1(self):
        """This is Check the return value of to_dict()"""
        self.assertTrue(type(self.amenity().to_dict()), dict)

    def test_to_dict2(self):
        """This Checks if dictionary has the primary keys available"""
        data = [
            "id",
            "__class__",
            "created_at",
            "updated_at"
        ]
        for i in data:
            self.assertTrue(i in self.amenity().to_dict())

    def test_newValue(self):
        """This adds new Values in Amenity"""
        temp = self.amenity()
        name = "Jeffery Mutuku"
        temp.name = name
        age = 89
        temp.age = age
        self.assertEqual(name, temp.name)
        self.assertEqual(age, temp.age)
        self.assertTrue("name" in temp.to_dict())
        self.assertTrue("age" in temp.to_dict())

    def test_class_attr(self):
        """This checks that name variable is first"""
        self.assertEqual(self.amenity().name, "")


if __name__ == "__main__":
    unittest.main()
