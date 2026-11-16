# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class NationalequitiesIntegratedfeedstocksummaryV25GTests(unittest.TestCase):

    def test_stocksummarymessage(self):
        module = "nyse/nationalequities/integratedfeedstocksummary/nationalequities_integratedfeedstocksummary_v2_5_g.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NationalEquities.IntegratedFeedStockSummary.Pillar.v2.5.g/StockSummaryMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
