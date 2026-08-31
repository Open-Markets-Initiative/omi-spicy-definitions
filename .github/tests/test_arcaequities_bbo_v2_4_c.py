# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class ArcaequitiesBboV24CTests(unittest.TestCase):

    def test_quotemessage(self):
        module = "nyse/arcaequities/bbo/arcaequities_bbo_v2_4_c.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaEquities.Bbo.Xdp.v2.4.c/QuoteMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_sequencenumberresetmessage(self):
        module = "nyse/arcaequities/bbo/arcaequities_bbo_v2_4_c.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaEquities.Bbo.Xdp.v2.4.c/SequenceNumberResetMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_symbolindexmappingmessage(self):
        module = "nyse/arcaequities/bbo/arcaequities_bbo_v2_4_c.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaEquities.Bbo.Xdp.v2.4.c/SymbolIndexMappingMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
