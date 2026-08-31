# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class EurexT7EtiV61Tests(unittest.TestCase):

    def test_heartbeat(self):
        module = "eurex/eti/eurex_t7_eti_v6_1_server.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eti.Fbe.v6.1/Heartbeat.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_retransmitmemessagerequest(self):
        module = "eurex/eti/eurex_t7_eti_v6_1_server.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eti.Fbe.v6.1/RetransmitMeMessageRequest.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_userloginresponse(self):
        module = "eurex/eti/eurex_t7_eti_v6_1_server.spicy"
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eti.Fbe.v6.1/UserLoginResponse.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
