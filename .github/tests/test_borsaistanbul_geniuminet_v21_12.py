# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class BorsaistanbulGeniuminetV2112Tests(unittest.TestCase):

    def test_combinationorderbookleg(self):
        module = "bist/borsaistanbul/geniuminet/borsaistanbul_geniuminet_v21_12.spicy"
        for payload in payloads.of("omi-data-packets/Bist/BorsaIstanbul.GeniumInet.Itch.v21.12/CombinationOrderBookLeg.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderbookdirectory(self):
        module = "bist/borsaistanbul/geniuminet/borsaistanbul_geniuminet_v21_12.spicy"
        for payload in payloads.of("omi-data-packets/Bist/BorsaIstanbul.GeniumInet.Itch.v21.12/OrderBookDirectory.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderbookstatemessage(self):
        module = "bist/borsaistanbul/geniuminet/borsaistanbul_geniuminet_v21_12.spicy"
        for payload in payloads.of("omi-data-packets/Bist/BorsaIstanbul.GeniumInet.Itch.v21.12/OrderBookStateMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_secondsmessage(self):
        module = "bist/borsaistanbul/geniuminet/borsaistanbul_geniuminet_v21_12.spicy"
        for payload in payloads.of("omi-data-packets/Bist/BorsaIstanbul.GeniumInet.Itch.v21.12/SecondsMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_shortsellstatus(self):
        module = "bist/borsaistanbul/geniuminet/borsaistanbul_geniuminet_v21_12.spicy"
        for payload in payloads.of("omi-data-packets/Bist/BorsaIstanbul.GeniumInet.Itch.v21.12/ShortSellStatus.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_systemeventmessage(self):
        module = "bist/borsaistanbul/geniuminet/borsaistanbul_geniuminet_v21_12.spicy"
        for payload in payloads.of("omi-data-packets/Bist/BorsaIstanbul.GeniumInet.Itch.v21.12/SystemEventMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ticksizetableentry(self):
        module = "bist/borsaistanbul/geniuminet/borsaistanbul_geniuminet_v21_12.spicy"
        for payload in payloads.of("omi-data-packets/Bist/BorsaIstanbul.GeniumInet.Itch.v21.12/TickSizeTableEntry.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
