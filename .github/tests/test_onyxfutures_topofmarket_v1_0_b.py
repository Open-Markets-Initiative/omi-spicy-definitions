# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class OnyxfuturesTopofmarketV10BTests(unittest.TestCase):

    def test_bestbidandoffermessage(self):
        module = "miax/onyxfutures/topofmarket/onyxfutures_topofmarket_v1_0_b.spicy"
        for payload in payloads.of("omi-data-packets/Miax/OnyxFutures.TopOfMarket.Mach.v1.0.b/BestBidAndOfferMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_heartbeat(self):
        module = "miax/onyxfutures/topofmarket/onyxfutures_topofmarket_v1_0_b.spicy"
        for payload in payloads.of("omi-data-packets/Miax/OnyxFutures.TopOfMarket.Mach.v1.0.b/Heartbeat.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_instrumenttradingstatusnotificationmessage(self):
        module = "miax/onyxfutures/topofmarket/onyxfutures_topofmarket_v1_0_b.spicy"
        for payload in payloads.of("omi-data-packets/Miax/OnyxFutures.TopOfMarket.Mach.v1.0.b/InstrumentTradingStatusNotificationMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_systemstatemessage(self):
        module = "miax/onyxfutures/topofmarket/onyxfutures_topofmarket_v1_0_b.spicy"
        for payload in payloads.of("omi-data-packets/Miax/OnyxFutures.TopOfMarket.Mach.v1.0.b/SystemStateMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
