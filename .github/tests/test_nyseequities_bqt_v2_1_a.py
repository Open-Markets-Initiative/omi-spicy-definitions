# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class NyseequitiesBqtV21ATests(unittest.TestCase):

    def test_consolidatedstocksummarymessage(self):
        module = "nyse/nyseequities/bqt/nyseequities_bqt_v2_1_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.Bqt.Xdp.v2.1.a/ConsolidatedStockSummaryMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_sequencenumberresetmessage(self):
        module = "nyse/nyseequities/bqt/nyseequities_bqt_v2_1_a.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.Bqt.Xdp.v2.1.a/SequenceNumberResetMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
