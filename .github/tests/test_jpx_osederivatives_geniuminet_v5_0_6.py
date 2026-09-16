# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class JpxOsederivativesGeniuminetV506Tests(unittest.TestCase):

    def test_addordernompid(self):
        module = "jpx/osederivatives/geniuminet/jpx_osederivatives_geniuminet_v5_0_6.spicy"
        for payload in payloads.of("omi-data-packets/Jpx/OseDerivatives.GeniumInet.Itch.v5.0.6/AddOrderNoMpid.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_equilibriumpriceupdate(self):
        module = "jpx/osederivatives/geniuminet/jpx_osederivatives_geniuminet_v5_0_6.spicy"
        for payload in payloads.of("omi-data-packets/Jpx/OseDerivatives.GeniumInet.Itch.v5.0.6/EquilibriumPriceUpdate.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderbookstatemessage(self):
        module = "jpx/osederivatives/geniuminet/jpx_osederivatives_geniuminet_v5_0_6.spicy"
        for payload in payloads.of("omi-data-packets/Jpx/OseDerivatives.GeniumInet.Itch.v5.0.6/OrderBookStateMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderdeletemessage(self):
        module = "jpx/osederivatives/geniuminet/jpx_osederivatives_geniuminet_v5_0_6.spicy"
        for payload in payloads.of("omi-data-packets/Jpx/OseDerivatives.GeniumInet.Itch.v5.0.6/OrderDeleteMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutedmessage(self):
        module = "jpx/osederivatives/geniuminet/jpx_osederivatives_geniuminet_v5_0_6.spicy"
        for payload in payloads.of("omi-data-packets/Jpx/OseDerivatives.GeniumInet.Itch.v5.0.6/OrderExecutedMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutedwithpricemessage(self):
        module = "jpx/osederivatives/geniuminet/jpx_osederivatives_geniuminet_v5_0_6.spicy"
        for payload in payloads.of("omi-data-packets/Jpx/OseDerivatives.GeniumInet.Itch.v5.0.6/OrderExecutedWithPriceMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_secondsmessage(self):
        module = "jpx/osederivatives/geniuminet/jpx_osederivatives_geniuminet_v5_0_6.spicy"
        for payload in payloads.of("omi-data-packets/Jpx/OseDerivatives.GeniumInet.Itch.v5.0.6/SecondsMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
