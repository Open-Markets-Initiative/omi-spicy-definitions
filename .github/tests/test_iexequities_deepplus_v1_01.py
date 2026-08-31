# Generated Spicy definition tests: spicy-driver parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SPICY_DRIVER = os.environ.get("SPICY_DRIVER", "spicy-driver")


class IexequitiesDeepplusV101Tests(unittest.TestCase):

    def test_a_addorder(self):
        module = "iex/iexequities/deepplus/iexequities_deepplus_v1_01.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.DeepPlus.IexTp.v1.0.2/a_AddOrder.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_all_message_types(self):
        module = "iex/iexequities/deepplus/iexequities_deepplus_v1_01.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.DeepPlus.IexTp.v1.0.2/all_message_types.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_b_tradebreak(self):
        module = "iex/iexequities/deepplus/iexequities_deepplus_v1_01.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.DeepPlus.IexTp.v1.0.2/B_TradeBreak.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_d_securitydirectory(self):
        module = "iex/iexequities/deepplus/iexequities_deepplus_v1_01.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.DeepPlus.IexTp.v1.0.2/D_SecurityDirectory.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_e_securityevent(self):
        module = "iex/iexequities/deepplus/iexequities_deepplus_v1_01.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.DeepPlus.IexTp.v1.0.2/E_SecurityEvent.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_h_tradingstatus(self):
        module = "iex/iexequities/deepplus/iexequities_deepplus_v1_01.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.DeepPlus.IexTp.v1.0.2/H_TradingStatus.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_i_retailliquidityindicator(self):
        module = "iex/iexequities/deepplus/iexequities_deepplus_v1_01.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.DeepPlus.IexTp.v1.0.2/I_RetailLiquidityIndicator.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_l_orderexecuted(self):
        module = "iex/iexequities/deepplus/iexequities_deepplus_v1_01.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.DeepPlus.IexTp.v1.0.2/L_OrderExecuted.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_m_ordermodify(self):
        module = "iex/iexequities/deepplus/iexequities_deepplus_v1_01.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.DeepPlus.IexTp.v1.0.2/M_OrderModify.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_o_operationalhaltstatus(self):
        module = "iex/iexequities/deepplus/iexequities_deepplus_v1_01.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.DeepPlus.IexTp.v1.0.2/O_OperationalHaltStatus.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_p_shortsalepriceteststatus(self):
        module = "iex/iexequities/deepplus/iexequities_deepplus_v1_01.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.DeepPlus.IexTp.v1.0.2/P_ShortSalePriceTestStatus.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_r_orderdelete(self):
        module = "iex/iexequities/deepplus/iexequities_deepplus_v1_01.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.DeepPlus.IexTp.v1.0.2/R_OrderDelete.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_s_systemevent(self):
        module = "iex/iexequities/deepplus/iexequities_deepplus_v1_01.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.DeepPlus.IexTp.v1.0.2/S_SystemEvent.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_t_trade(self):
        module = "iex/iexequities/deepplus/iexequities_deepplus_v1_01.spicy"
        for payload in payloads.of("omi-data-packets/Iex/IexEquities.DeepPlus.IexTp.v1.0.2/T_Trade.pcap"):
            result = subprocess.run([SPICY_DRIVER, module], input=payload, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
