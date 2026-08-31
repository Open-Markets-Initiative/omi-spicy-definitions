# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class NyseequitiesImbalancesfeedV21FTests(unittest.TestCase):

    def test_imbalancemessage(self):
        module = "nyse/nyseequities/imbalancesfeed/nyseequities_imbalancesfeed_v2_1_f.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.ImbalancesFeed.Xdp.v2.1.f/ImbalanceMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_sequenceresetmessage(self):
        module = "nyse/nyseequities/imbalancesfeed/nyseequities_imbalancesfeed_v2_1_f.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.ImbalancesFeed.Xdp.v2.1.f/SequenceResetMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
