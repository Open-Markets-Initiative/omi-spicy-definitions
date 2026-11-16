# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class SpectraFutinfoincrementalV800Tests(unittest.TestCase):

    def test_heartbeatmessage(self):
        module = "moex/spectra/futinfoincremental/spectra_futinfoincremental_v8_0_0.spicy"
        for payload in payloads.of("omi-data-packets/Moex/Spectra.FutInfoIncremental.Simba.v8.0.0/HeartbeatMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitygroupstatusmessage(self):
        module = "moex/spectra/futinfoincremental/spectra_futinfoincremental_v8_0_0.spicy"
        for payload in payloads.of("omi-data-packets/Moex/Spectra.FutInfoIncremental.Simba.v8.0.0/SecurityGroupStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitymassstatusmessage(self):
        module = "moex/spectra/futinfoincremental/spectra_futinfoincremental_v8_0_0.spicy"
        for payload in payloads.of("omi-data-packets/Moex/Spectra.FutInfoIncremental.Simba.v8.0.0/SecurityMassStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_tradingsessionstatusmessage(self):
        module = "moex/spectra/futinfoincremental/spectra_futinfoincremental_v8_0_0.spicy"
        for payload in payloads.of("omi-data-packets/Moex/Spectra.FutInfoIncremental.Simba.v8.0.0/TradingSessionStatusMessage.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
