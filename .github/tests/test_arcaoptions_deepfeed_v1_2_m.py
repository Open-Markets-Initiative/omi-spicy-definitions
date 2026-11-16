# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class ArcaoptionsDeepfeedV12MTests(unittest.TestCase):

    def test_optionsaddordermessage(self):
        module = "nyse/arcaoptions/deepfeed/arcaoptions_deepfeed_v1_2_m.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.DeepFeed.Pillar.v1.2.m/OptionsAddOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_optionscrosstrademessage(self):
        module = "nyse/arcaoptions/deepfeed/arcaoptions_deepfeed_v1_2_m.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.DeepFeed.Pillar.v1.2.m/OptionsCrossTradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_optionsdeleteordermessage(self):
        module = "nyse/arcaoptions/deepfeed/arcaoptions_deepfeed_v1_2_m.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.DeepFeed.Pillar.v1.2.m/OptionsDeleteOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_optionsimbalancemessage(self):
        module = "nyse/arcaoptions/deepfeed/arcaoptions_deepfeed_v1_2_m.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.DeepFeed.Pillar.v1.2.m/OptionsImbalanceMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_optionsmodifyordermessage(self):
        module = "nyse/arcaoptions/deepfeed/arcaoptions_deepfeed_v1_2_m.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.DeepFeed.Pillar.v1.2.m/OptionsModifyOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_optionsnondisplayedtrademessage(self):
        module = "nyse/arcaoptions/deepfeed/arcaoptions_deepfeed_v1_2_m.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.DeepFeed.Pillar.v1.2.m/OptionsNonDisplayedTradeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_optionsorderexecutionmessage(self):
        module = "nyse/arcaoptions/deepfeed/arcaoptions_deepfeed_v1_2_m.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.DeepFeed.Pillar.v1.2.m/OptionsOrderExecutionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_optionsreplaceordermessage(self):
        module = "nyse/arcaoptions/deepfeed/arcaoptions_deepfeed_v1_2_m.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.DeepFeed.Pillar.v1.2.m/OptionsReplaceOrderMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_optionsstatusmessage(self):
        module = "nyse/arcaoptions/deepfeed/arcaoptions_deepfeed_v1_2_m.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.DeepFeed.Pillar.v1.2.m/OptionsStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_outrightseriesindexmappingmessage(self):
        module = "nyse/arcaoptions/deepfeed/arcaoptions_deepfeed_v1_2_m.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.DeepFeed.Pillar.v1.2.m/OutrightSeriesIndexMappingMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitystatusmessage(self):
        module = "nyse/arcaoptions/deepfeed/arcaoptions_deepfeed_v1_2_m.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.DeepFeed.Pillar.v1.2.m/SecurityStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_sequencenumberresetmessage(self):
        module = "nyse/arcaoptions/deepfeed/arcaoptions_deepfeed_v1_2_m.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.DeepFeed.Pillar.v1.2.m/SequenceNumberResetMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_sourcetimereferencemessage(self):
        module = "nyse/arcaoptions/deepfeed/arcaoptions_deepfeed_v1_2_m.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.DeepFeed.Pillar.v1.2.m/SourceTimeReferenceMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_symbolclearmessage(self):
        module = "nyse/arcaoptions/deepfeed/arcaoptions_deepfeed_v1_2_m.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.DeepFeed.Pillar.v1.2.m/SymbolClearMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_symbolindexmappingmessage(self):
        module = "nyse/arcaoptions/deepfeed/arcaoptions_deepfeed_v1_2_m.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.DeepFeed.Pillar.v1.2.m/SymbolIndexMappingMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
