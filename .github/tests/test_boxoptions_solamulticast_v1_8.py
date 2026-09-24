# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class BoxoptionsSolamulticastV18Tests(unittest.TestCase):

    def test_optionquotemessage(self):
        module = "box/boxoptions/solamulticast/boxoptions_solamulticast_v1_8.spicy"
        for payload in payloads.of("omi-data-packets/Box/BoxOptions.SolaMulticast.Hsvf.v1.8/OptionQuoteMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
