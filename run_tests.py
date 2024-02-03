# run_tests.py

import unittest

def run_tests():
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir='.', pattern='test_*.py', top_level_dir='.')
    
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()
