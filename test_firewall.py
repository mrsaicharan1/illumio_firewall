import unittest
from firewall import Firewall
class TestFireWall(unittest.TestCase):

    def test(self):
        fw = Firewall('input.csv')
        self.assertTrue(fw.accept_packet("inbound","udp","80","192.168.1.6"),True)
        self.assertTrue(fw.accept_packet("outbound","tcp","25","173.177.2.3"),True)
        self.assertFalse(fw.accept_packet("inbound","udp","9","192.167.1.6"),False)
        self.assertFalse(fw.accept_packet("inbound","udp","72","192.158.1.6"),False)

if __name__ == "__main__":
    unittest.main()
