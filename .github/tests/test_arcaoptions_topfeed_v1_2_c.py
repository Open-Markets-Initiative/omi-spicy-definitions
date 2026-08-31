# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class ArcaoptionsTopfeedV12CTests(unittest.TestCase):

    def test_message(self):
        module = "nyse/arcaoptions/topfeed/arcaoptions_topfeed_v1_2_c.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.TopFeed.Pillar.v1.2.c/HeartBeat.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_optionsquotemessage(self):
        module = "nyse/arcaoptions/topfeed/arcaoptions_topfeed_v1_2_c.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.TopFeed.Pillar.v1.2.c/OptionsQuoteMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_sequencenumberresetmessage(self):
        module = "nyse/arcaoptions/topfeed/arcaoptions_topfeed_v1_2_c.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.TopFeed.Pillar.v1.2.c/SequenceNumberResetMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
