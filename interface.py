from firmware import packet, to_bool, twos_complement
import struct

user_input = input("Press 'H' for hex input and 'P' for packet input\n")

if user_input=='H':
    hex = input("Please enter a hex number?")

    bin = str(bin(int(hex[20:22], base=16)))

    p = packet(int(hex[0:2], base=16), int(hex[2:4], base=16), twos_complement(hex[4:12]), twos_complement(hex[12:20]), to_bool(bin[3]), to_bool(bin[2]))
    print(p)

elif user_input=="P":
    """
    pt = input("packet_type:")
    pv = input("packet_version:")
    teuwh = input("total_energy_used_watt_hours:")
    tdms = input("time_drift_milli_seconds:")
    giw = input("geyser_is_warm:")
    gidp = input("geyser_is_drawing_power:")
    """
    pt = 1
    pv = 0
    teuwh = 4552
    tdms = 2003
    giw = False
    gidp = True
    pt = struct.pack('b',pt)
    s = pt.hex()
    pv = struct.pack('b', pv)
    s = s+pv.hex()
    teuwh = struct.pack('I', teuwh)
    s = s+(teuwh.hex())
    tdms = struct.pack('i', tdms)
    s = s+(tdms.hex())
    giw = struct.pack('b', giw)
    gidp = struct.pack('b', gidp)
    flags = (gidp+giw).hex()
    print(flags)
    print(s)