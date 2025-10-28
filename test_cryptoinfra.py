# test_cryptoinfra.py
"""
Tests for CryptoInfra module.
"""

import unittest
from cryptoinfra import CryptoInfra

class TestCryptoInfra(unittest.TestCase):
    """Test cases for CryptoInfra class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoInfra()
        self.assertIsInstance(instance, CryptoInfra)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoInfra()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
