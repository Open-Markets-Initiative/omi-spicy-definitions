# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class NyseequitiesBboV24GTests(unittest.TestCase):

    def test_quotemessage(self):
        module = "nyse/nyseequities/bbo/nyseequities_bbo_v2_4_g.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.Bbo.Xdp.v2.4.g/QuoteMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitystatusmessage(self):
        module = "nyse/nyseequities/bbo/nyseequities_bbo_v2_4_g.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.Bbo.Xdp.v2.4.g/SecurityStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_sequencenumberresetmessage(self):
        module = "nyse/nyseequities/bbo/nyseequities_bbo_v2_4_g.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.Bbo.Xdp.v2.4.g/SequenceNumberResetMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_symbolindexmappingmessage(self):
        module = "nyse/nyseequities/bbo/nyseequities_bbo_v2_4_g.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.Bbo.Xdp.v2.4.g/SymbolIndexMappingMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_tradingsessionchangemessage(self):
        module = "nyse/nyseequities/bbo/nyseequities_bbo_v2_4_g.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.Bbo.Xdp.v2.4.g/TradingSessionChangeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
