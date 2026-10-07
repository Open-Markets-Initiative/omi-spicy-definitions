# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class CmeGlobexMdp3V112Tests(unittest.TestCase):

    def test_marketdatarequest(self):
        module = "cme/globex/mdp3/cme_globex_mdp3_v1_12_clienttcp.spicy"
        for payload in payloads.of("omi-data-packets/Cme/Globex.Mdp3.Sbe.v1.12/MarketDataRequest.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_mdincrementalrefreshbooklongqty(self):
        module = "cme/globex/mdp3/cme_globex_mdp3_v1_12_clienttcp.spicy"
        for payload in payloads.of("omi-data-packets/Cme/Globex.Mdp3.Sbe.v1.12/MdIncrementalRefreshBookLongQty.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_mdincrementalrefreshtradesummarylongqty(self):
        module = "cme/globex/mdp3/cme_globex_mdp3_v1_12_clienttcp.spicy"
        for payload in payloads.of("omi-data-packets/Cme/Globex.Mdp3.Sbe.v1.12/MdIncrementalRefreshTradeSummaryLongQty.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_mdinstrumentdefinitionfx(self):
        module = "cme/globex/mdp3/cme_globex_mdp3_v1_12_clienttcp.spicy"
        for payload in payloads.of("omi-data-packets/Cme/Globex.Mdp3.Sbe.v1.12/MdInstrumentDefinitionFx.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_requestack(self):
        module = "cme/globex/mdp3/cme_globex_mdp3_v1_12_clienttcp.spicy"
        for payload in payloads.of("omi-data-packets/Cme/Globex.Mdp3.Sbe.v1.12/RequestAck.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitylistrequest(self):
        module = "cme/globex/mdp3/cme_globex_mdp3_v1_12_clienttcp.spicy"
        for payload in payloads.of("omi-data-packets/Cme/Globex.Mdp3.Sbe.v1.12/SecurityListRequest.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitystatus(self):
        module = "cme/globex/mdp3/cme_globex_mdp3_v1_12_clienttcp.spicy"
        for payload in payloads.of("omi-data-packets/Cme/Globex.Mdp3.Sbe.v1.12/SecurityStatus.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitystatusrequest(self):
        module = "cme/globex/mdp3/cme_globex_mdp3_v1_12_clienttcp.spicy"
        for payload in payloads.of("omi-data-packets/Cme/Globex.Mdp3.Sbe.v1.12/SecurityStatusRequest.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_snapshotfullrefreshtcplongqty(self):
        module = "cme/globex/mdp3/cme_globex_mdp3_v1_12_clienttcp.spicy"
        for payload in payloads.of("omi-data-packets/Cme/Globex.Mdp3.Sbe.v1.12/SnapshotFullRefreshTcpLongQty.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_subscriberheartbeat(self):
        module = "cme/globex/mdp3/cme_globex_mdp3_v1_12_clienttcp.spicy"
        for payload in payloads.of("omi-data-packets/Cme/Globex.Mdp3.Sbe.v1.12/SubscriberHeartbeat.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
