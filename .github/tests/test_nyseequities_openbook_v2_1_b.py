# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class NyseequitiesOpenbookV21BTests(unittest.TestCase):

    def test_deltaupdatemessage(self):
        module = "nyse/nyseequities/openbook/nyseequities_openbook_v2_1_b.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.OpenBook.Ultra.v2.1.b/DeltaUpdateMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_fullupdatemessage(self):
        module = "nyse/nyseequities/openbook/nyseequities_openbook_v2_1_b.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.OpenBook.Ultra.v2.1.b/FullUpdateMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_heartbeatmessage(self):
        module = "nyse/nyseequities/openbook/nyseequities_openbook_v2_1_b.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.OpenBook.Ultra.v2.1.b/HeartbeatMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_sequencenumberresetmessage(self):
        module = "nyse/nyseequities/openbook/nyseequities_openbook_v2_1_b.spicy"
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.OpenBook.Ultra.v2.1.b/SequenceNumberResetMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
