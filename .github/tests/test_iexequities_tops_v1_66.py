# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class IexequitiesTopsV166Tests(unittest.TestCase):

    def test_quoteupdatemessage(self):
        module = "iex/iexequities/tops/iexequities_tops_v1_66.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.Tops.IexTp.v1.64/QuoteUpdateMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
