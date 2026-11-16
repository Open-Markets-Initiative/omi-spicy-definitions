# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class SpectraOrderslogsnapshotV800Tests(unittest.TestCase):

    def test_orderbooksnapshotmessage(self):
        module = "moex/spectra/orderslogsnapshot/spectra_orderslogsnapshot_v8_0_0.spicy"
        for payload in payloads.of("omi-data-packets/Moex/Spectra.OrdersLogSnapshot.Simba.v8.0.0/OrderBookSnapshotMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_sequenceresetmessage(self):
        module = "moex/spectra/orderslogsnapshot/spectra_orderslogsnapshot_v8_0_0.spicy"
        for payload in payloads.of("omi-data-packets/Moex/Spectra.OrdersLogSnapshot.Simba.v8.0.0/SequenceResetMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
