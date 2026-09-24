# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class SiacOpraOutputV62Tests(unittest.TestCase):

    def test_administrativemessage(self):
        module = "siac/opra/output/siac_opra_output_v6_2.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Opra.Output.Obi.v6.2/AdministrativeMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_controlmessage(self):
        module = "siac/opra/output/siac_opra_output_v6_2.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Opra.Output.Obi.v6.2/ControlMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_longequityandindexquotemessage(self):
        module = "siac/opra/output/siac_opra_output_v6_2.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Opra.Output.Obi.v6.2/LongEquityAndIndexQuoteMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_shortequityandindexquotemessage(self):
        module = "siac/opra/output/siac_opra_output_v6_2.spicy"
        for payload in payloads.of("omi-data-packets/Siac/Opra.Output.Obi.v6.2/ShortEquityAndIndexQuoteMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
