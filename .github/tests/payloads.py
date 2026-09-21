# Generated transport payload extraction for pcap captures

import dpkt


def of(path):
    result = []

    with open(path, "rb") as capture:
        # a capture may be classic pcap or pcapng, which its first four bytes tell apart
        magic = capture.read(4)
        capture.seek(0)
        reader = dpkt.pcapng.Reader(capture) if magic == b"\x0a\x0d\x0d\x0a" else dpkt.pcap.Reader(capture)

        for _, frame in reader:
            packet = linked(reader.datalink(), frame)
            ip = packet if isinstance(packet, dpkt.ip.IP) else packet.data

            if not isinstance(ip, dpkt.ip.IP):
                continue

            transport = ip.data

            if not isinstance(transport, (dpkt.udp.UDP, dpkt.tcp.TCP)):
                continue

            payload = bytes(transport.data)

            if payload:
                result.append(payload)

    return result


def linked(link, frame):
    """The frame as its link type reads it: ethernet unless the capture says linux cooked, loopback or raw ip."""
    if link == 113:
        return dpkt.sll.SLL(frame)
    if link == 276:
        return dpkt.sll2.SLL2(frame)
    if link == 0:
        return dpkt.loopback.Loopback(frame)
    if link == 101:
        return dpkt.ip.IP(frame)
    return dpkt.ethernet.Ethernet(frame)
