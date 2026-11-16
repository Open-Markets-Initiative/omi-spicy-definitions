# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class AmexoptionsTopfeedV12KTests(unittest.TestCase):

    def test_optionsquotemessage(self):
        module = "nyse/amexoptions/topfeed/amexoptions_topfeed_v1_2_k.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexOptions.TopFeed.Pillar.v1.2.k/OptionsQuoteMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_optionsstatusmessage(self):
        module = "nyse/amexoptions/topfeed/amexoptions_topfeed_v1_2_k.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexOptions.TopFeed.Pillar.v1.2.k/OptionsStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_outrightseriesindexmappingmessage(self):
        module = "nyse/amexoptions/topfeed/amexoptions_topfeed_v1_2_k.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexOptions.TopFeed.Pillar.v1.2.k/OutrightSeriesIndexMappingMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitystatusmessage(self):
        module = "nyse/amexoptions/topfeed/amexoptions_topfeed_v1_2_k.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexOptions.TopFeed.Pillar.v1.2.k/SecurityStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_sequencenumberresetmessage(self):
        module = "nyse/amexoptions/topfeed/amexoptions_topfeed_v1_2_k.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexOptions.TopFeed.Pillar.v1.2.k/SequenceNumberResetMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_sourcetimereferencemessage(self):
        module = "nyse/amexoptions/topfeed/amexoptions_topfeed_v1_2_k.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexOptions.TopFeed.Pillar.v1.2.k/SourceTimeReferenceMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_symbolclearmessage(self):
        module = "nyse/amexoptions/topfeed/amexoptions_topfeed_v1_2_k.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexOptions.TopFeed.Pillar.v1.2.k/SymbolClearMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_symbolindexmappingmessage(self):
        module = "nyse/amexoptions/topfeed/amexoptions_topfeed_v1_2_k.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/AmexOptions.TopFeed.Pillar.v1.2.k/SymbolIndexMappingMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
