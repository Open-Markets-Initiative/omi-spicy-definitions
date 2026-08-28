# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class IexequitiesDeepV106Tests(unittest.TestCase):

    def test_heartbeat(self):
        module = "iex/iexequities/deep/iexequities_deep_v1_06.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.Deep.IexTp.v1.06/Heartbeat.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_pricelevelbuyupdatemessage(self):
        module = "iex/iexequities/deep/iexequities_deep_v1_06.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.Deep.IexTp.v1.06/PriceLevelBuyUpdateMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_pricelevelsellupdatemessage(self):
        module = "iex/iexequities/deep/iexequities_deep_v1_06.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.Deep.IexTp.v1.06/PriceLevelSellUpdateMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
