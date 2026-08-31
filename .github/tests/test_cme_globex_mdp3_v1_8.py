# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class CmeGlobexMdp3V18Tests(unittest.TestCase):

    def test_mdincrementalrefreshtradesummary(self):
        module = "cme/mdp3/cme_globex_mdp3_v1_8_udp.spicy"
        for payload in payloads.of("omi-data-packets/Cme/Globex.Mdp3.Sbe.v1.8/MdIncrementalRefreshTradeSummary.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
