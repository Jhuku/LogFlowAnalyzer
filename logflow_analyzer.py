import os
import sys

TAG_MAP = {}

protomap = {
    0: "HOPOPT",
    1: "ICMP",
    2: "IGMP",
    3: "GGP",
    4: "IPv",
    5: "ST",
    6: "TCP",
    7: "CBT",
    8: "EGP",
    9: "IGP",
    10: "BBN",
    11: "NVP",
    12: "PUP",
    13: "ARGUS",
    14: "EMCON",
    15: "XNET",
    16: "CHAOS",
    17: "UDP",
    18: "MUX",
    19: "DCN",
    20: "HMP",
    21: "PRM",
    22: "XNS",
    23: "TRUNK",
    24: "TRUNK",
    25: "LEAF-1",
    26: "LEAF-2",
    27: "RDP",
    28: "IRTP",
    29: "ISO",
    30: "NETBLT",
    31: "MFE",
    32: "MERIT",
    33: "DCCP",
    34: "3PC",
    35: "IDPR",
    36: "XTP",
    37: "DDP",
    38: "IDPR",
    39: "TP",
    40: "IL",
    41: "IPv",
    42: "SDRP",
    43: "IPv",
    44: "IPv",
    45: "IDRP",
    46: "RSVP",
    47: "GRE",
    48: "DSR",
    49: "BNA",
    50: "ESP",
    51: "AH",
    52: "I-NLSP",
    53: "SWIPE",
    54: "NARP",
    55: "Min",
    56: "TLSP",
    57: "SKIP",
    58: "IPv",
    59: "IPv",
    60: "IPv",
    62: "CFTP",
    64: "SAT",
    65: "KRYPTOLAN",
    66: "RVD",
    67: "IPPC",
    69: "SAT",
    70: "VISA",
    71: "IPCV",
    72: "CPNX",
    73: "CPHB",
    74: "WSN",
    75: "PVP",
    76: "BR",
    77: "SUN",
    78: "WB",
    79: "WB",
    80: "ISO",
    81: "VMTP",
    82: "SECURE",
    83: "VINES",
    84: "IPTM",
    85: "NSFNET",
    86: "DGP",
    87: "TCF",
    88: "EIGRP",
    89: "OSPFIGP",
    90: "Sprite",
    91: "LARP",
    92: "MTP",
    93: "AX",
    94: "IPIP",
    95: "MICP",
    96: "SCC",
    97: "ETHERIP",
    98: "ENCAP",
    100: "GMTP",
    101: "IFMP",
    102: "PNNI",
    103: "PIM",
    104: "ARIS",
    105: "SCPS",
    106: "QNX",
    107: "A/N",
    108: "IPComp",
    109: "SNP",
    110: "Compaq",
    111: "IPX",
    112: "VRRP",
    113: "PGM",
    115: "L2TP",
    116: "DDX",
    117: "IATP",
    118: "STP",
    119: "SRP",
    120: "UTI",
    121: "SMP",
    122: "SM",
    123: "PTP",
    124: "ISIS",
    125: "FIRE",
    126: "CRTP",
    127: "CRUDP",
    128: "SSCOPMCE",
    129: "IPLT",
    130: "SPS",
    131: "PIPE",
    132: "SCTP",
    133: "FC",
    134: "RSVP",
    135: "Mobility",
    136: "UDPLite",
    137: "MPLS",
    138: "manet",
    139: "HIP",
    140: "Shim",
    141: "WESP",
    142: "ROHC",
    143: "Ethernet",
    144: "AGGFRAG",
    145: "NSH",
    255: "Reserved",
}


# create a map of portno-protocol -> tag by reading the lookup file
def parseLookupcsv(path):
    with open(path, "r") as p:
        lines = p.read()
        # Use method splitlines to split the lines
        # of data at the newline delimiters
        lines = lines.splitlines()

    linesNoNewlines = [x for x in lines if x != ""]
    for item in linesNoNewlines:
        TAG_MAP[
            str(item.split(",")[0]).lower().strip()
            + "-"
            + str(item.split(",")[1]).lower().strip()
        ] = (str(item.split(",")[2]).lower().strip())


if __name__ == "__main__":
    categoryFreq = {}
    portProtoFreq = {}
    portProtocolList = []

    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )

    if len(sys.argv) > 1:
        logPath = sys.argv[1]
        lookupfilePath = sys.argv[2]
    else:
        logPath = os.path.join(__location__, "logs.txt")
        lookupfilePath = os.path.join(__location__, "lookup.csv")

    parseLookupcsv(lookupfilePath)

    with open(logPath, "r") as p:
        lines = p.read()

        # Use method splitlines to split the lines
        # of data at the newline delimiters
        lines = lines.splitlines()

    # remove any extra new lines
    linesNoNewlines = [x for x in lines if x != ""]

    for item in linesNoNewlines:
        entry = item.split(" ")
        port = str(entry[7])
        protocolNumber = str(entry[8])
        protocolName = protomap.get(int(protocolNumber)).lower()
        portProto = port + "," + protocolName

        if portProto not in portProtoFreq:
            portProtoFreq[portProto] = 1
        else:
            portProtoFreq[portProto] += 1

        # category for the log entry
        category = TAG_MAP.get(str(port) + "-" + str(protocolName), "Untagged")

        if category not in categoryFreq:
            categoryFreq[category] = 1
        else:
            categoryFreq[category] += 1

    # write the tag count file
    fileContent = ""
    for category_item in categoryFreq:
        fileContent += (
            str(category_item) + "," + str(categoryFreq[category_item]) + "\n"
        )

    with open(os.path.join(__location__, "tagcount.csv"), "w+") as f:
        f.write(fileContent)

    # write the port proto name count file
    fileContent = ""
    for portproto_item in portProtoFreq:
        fileContent += (
            str(portproto_item) + "," + str(portProtoFreq[portproto_item]) + "\n"
        )

    with open(os.path.join(__location__, "portprotocount.csv"), "w+") as f:
        f.write(fileContent)