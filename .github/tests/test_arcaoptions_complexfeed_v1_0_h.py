# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class ArcaoptionsComplexfeedV10HTests(unittest.TestCase):

    def test_complexseriesindexmappingmessage(self):
        module = "nyse/arcaoptions/complexfeed/arcaoptions_complexfeed_v1_0_h.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.ComplexFeed.Pillar.v1.0.h/ComplexSeriesIndexMappingMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_optionsquotemessage(self):
        module = "nyse/arcaoptions/complexfeed/arcaoptions_complexfeed_v1_0_h.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.ComplexFeed.Pillar.v1.0.h/OptionsQuoteMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_optionsstatusmessage(self):
        module = "nyse/arcaoptions/complexfeed/arcaoptions_complexfeed_v1_0_h.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.ComplexFeed.Pillar.v1.0.h/OptionsStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_optionstrademessage(self):
        module = "nyse/arcaoptions/complexfeed/arcaoptions_complexfeed_v1_0_h.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.ComplexFeed.Pillar.v1.0.h/OptionsTradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_sourcetimereferencemessage(self):
        module = "nyse/arcaoptions/complexfeed/arcaoptions_complexfeed_v1_0_h.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.ComplexFeed.Pillar.v1.0.h/SourceTimeReferenceMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_symbolclearmessage(self):
        module = "nyse/arcaoptions/complexfeed/arcaoptions_complexfeed_v1_0_h.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.ComplexFeed.Pillar.v1.0.h/SymbolClearMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
