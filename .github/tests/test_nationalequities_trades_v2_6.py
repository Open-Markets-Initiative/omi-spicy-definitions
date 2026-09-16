# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class NationalequitiesTradesV26Tests(unittest.TestCase):

    def test_securitystatusmessage(self):
        module = "nyse/nationalequities/trades/nationalequities_trades_v2_6.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NationalEquities.Trades.Pillar.v2.6/SecurityStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_trademessage(self):
        module = "nyse/nationalequities/trades/nationalequities_trades_v2_6.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NationalEquities.Trades.Pillar.v2.6/TradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
