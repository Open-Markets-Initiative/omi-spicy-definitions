# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class NtxequitiesTotalviewV50Tests(unittest.TestCase):

    def test_addordernompidattributionmessage(self):
        module = "nasdaq/ntxequities/totalview/ntxequities_totalview_v5_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NtxEquities.TotalView.Itch.v5.0/AddOrderNoMpidAttributionMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderdeletemessage(self):
        module = "nasdaq/ntxequities/totalview/ntxequities_totalview_v5_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NtxEquities.TotalView.Itch.v5.0/OrderDeleteMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderreplacemessage(self):
        module = "nasdaq/ntxequities/totalview/ntxequities_totalview_v5_0.spicy"
        for payload in payloads.of("omi-data-packets/Nasdaq/NtxEquities.TotalView.Itch.v5.0/OrderReplaceMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
