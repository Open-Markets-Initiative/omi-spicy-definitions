# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class NyseequitiesOpenbook.aggregatedV21DTests(unittest.TestCase):

    def test_orderbookdeltaupdatemessage(self):
        module = "nyse/nyseequities/openbook.aggregated/nyseequities_openbook.aggregated_v2_1_d.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.OpenBook.Aggregated.Xdp.v2.1.d/OrderbookDeltaUpdateMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderbooksnapshotmessage(self):
        module = "nyse/nyseequities/openbook.aggregated/nyseequities_openbook.aggregated_v2_1_d.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.OpenBook.Aggregated.Xdp.v2.1.d/OrderbookSnapshotMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_sequencenumberresetmessage(self):
        module = "nyse/nyseequities/openbook.aggregated/nyseequities_openbook.aggregated_v2_1_d.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.OpenBook.Aggregated.Xdp.v2.1.d/SequenceNumberResetMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_symbolindexmappingmessage(self):
        module = "nyse/nyseequities/openbook.aggregated/nyseequities_openbook.aggregated_v2_1_d.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.OpenBook.Aggregated.Xdp.v2.1.d/SymbolIndexMappingMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
