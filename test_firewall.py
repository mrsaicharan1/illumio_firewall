import unittest
from firewall import Firewall
class TestFireWall(unittest.TestCase):
    def test_ip_address(self,ip):
        self.assertTrue("192.168.1.5-192.168.255.255")

if __name__ == "__main__":
    unittest.main()
