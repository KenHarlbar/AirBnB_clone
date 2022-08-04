#!/usr/bin/env python3
"""Module to test Base class module"""

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBase(unittest.TestCase):
    """Test case for base module"""

    def setUp(self):
        self.created_b1 = round(datetime.now().timestamp())
        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def test_init(self):
        """Test init function"""
        self.assertNotEqual(self.b1.id, self.b2.id)
        
        self.assertAlmostEqual(round(self.b1.created_at.timestamp()), round(self.b1.updated_at.timestamp()))

        self.assertAlmostEqual(round(self.b1.created_at.timestamp()), self.created_b1)

    def test_save(self):
        """Test save function"""
        updated_b1 = round(datetime.now().timestamp())
        self.b1.save()
        self.assertAlmostEqual(round(self.b1.updated_at.timestamp()), updated_b1)

    def test_string(self):
        """Test __str__ function"""
        self.assertEqual(self.b1.__str__(), f"[BaseModel] ({self.b1.id}) {self.b1.__dict__}")

    def test_to_dict(self):
        """Test to_dict function of BaseModel"""
        b1_dict = self.b1.to_dict()
        self.assertEqual(b1_dict["__class__"], "BaseModel")
        self.assertEqual(b1_dict["created_at"], self.b1.created_at.isoformat())
        self.assertEqual(b1_dict["updated_at"], self.b1.updated_at.isoformat())
