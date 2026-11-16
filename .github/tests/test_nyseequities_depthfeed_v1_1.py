# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class NyseequitiesDepthfeedV11Tests(unittest.TestCase):

    def test_deltamessage(self):
        module = "nyse/nyseequities/depthfeed/nyseequities_depthfeed_v1_1.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.DepthFeed.Pillar.v1.1/DeltaMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_imbalancemessage(self):
        module = "nyse/nyseequities/depthfeed/nyseequities_depthfeed_v1_1.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.DepthFeed.Pillar.v1.1/ImbalanceMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitystatusmessage(self):
        module = "nyse/nyseequities/depthfeed/nyseequities_depthfeed_v1_1.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.DepthFeed.Pillar.v1.1/SecurityStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
