import struct, binascii

class packet:
    def __init__(self, pt, pv, teuwh, tdms, giw, gidp):
        self.packet_type = pt
        self.packet_version = pv
        self.total_energy_used_watt_hours = teuwh
        self.time_drift_milli_seconds = tdms
        self.geyser_is_warm = giw
        self.geyser_is_drawing_power = gidp

    def __str__(self):
        s = "packet_type = "+str(self.packet_type)+"\npacket_version = "+str(self.packet_version)+"\ntotal_energy_used_watt_hours = "+str(self.total_energy_used_watt_hours)
        s = s+"\ntime_drift_milli_seconds = "+str(self.time_drift_milli_seconds)+"\ngeyser_is_warm = "+str(self.geyser_is_warm)+"\ngeyser_is_drawing_power = "+str(self.geyser_is_drawing_power)
        return s

def to_bool(x):
    if int(x) == 1:
        return True
    else:
        return False

def to_int(x):
    if x == 'True':
        return 1
    else:
        return False

def twos_complement(hexstr):
    b = bytes(hexstr, 'utf-8')
    ba = binascii.a2b_hex(b)
    return(int.from_bytes(ba, byteorder='little', signed=True))

def bin_to_int(binstr):
    num = 0
    for i in range(len(binstr)):
        if binstr[i]!='0':
            num = num+pow(2,int(binstr[i]))
    return num