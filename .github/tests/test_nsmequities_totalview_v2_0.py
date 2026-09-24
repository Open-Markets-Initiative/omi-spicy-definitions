# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class NsmequitiesTotalviewV20Tests(unittest.TestCase):

    def test_addordermessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v2_0_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v2.0/AddOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordercancelmessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v2_0_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v2.0/OrderCancelMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutedmessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v2_0_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v2.0/OrderExecutedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_systemeventmessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v2_0_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v2.0/SystemEventMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_trademessage(self):
        module = "nasdaq/nsmequities/totalview/nsmequities_totalview_v2_0_udp.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v2.0/TradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
