# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class JnxequitiesPtsV111Tests(unittest.TestCase):

    def test_cancelordermessage(self):
        module = "jnx/jnxequities/pts/jnxequities_pts_v1_11_server.spicy"
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Ouch.v1.11/CancelOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_enterordermessage(self):
        module = "jnx/jnxequities/pts/jnxequities_pts_v1_11_client.spicy"
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Ouch.v1.11/EnterOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_loginacceptedpacket(self):
        module = "jnx/jnxequities/pts/jnxequities_pts_v1_11_client.spicy"
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Ouch.v1.11/LoginAcceptedPacket.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_loginrequestpacket(self):
        module = "jnx/jnxequities/pts/jnxequities_pts_v1_11_client.spicy"
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Ouch.v1.11/LoginRequestPacket.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderacceptedmessage(self):
        module = "jnx/jnxequities/pts/jnxequities_pts_v1_11_client.spicy"
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Ouch.v1.11/OrderAcceptedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordercanceledmessage(self):
        module = "jnx/jnxequities/pts/jnxequities_pts_v1_11_server.spicy"
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Ouch.v1.11/OrderCanceledMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutedmessage(self):
        module = "jnx/jnxequities/pts/jnxequities_pts_v1_11_server.spicy"
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Ouch.v1.11/OrderExecutedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderrejectedmessage(self):
        module = "jnx/jnxequities/pts/jnxequities_pts_v1_11_server.spicy"
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Ouch.v1.11/OrderRejectedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_replaceordermessage(self):
        module = "jnx/jnxequities/pts/jnxequities_pts_v1_11_client.spicy"
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Ouch.v1.11/ReplaceOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
