from firmware import packet, to_bool, twos_complement, bin_to_int, to_int
import struct

#Choose P for packet input and H for hex input
user_input = input("Press 'H' for hex input and 'P' for packet input\n")

if user_input=='H':
    try:
        hex = input("Please enter a hex number?")
        #accepts the string of hex digits
        bin = str(bin(int(hex[20:22], base=16)))
        #converts flags to a string of binary
        p = packet(int(hex[0:2], base=16), int(hex[2:4], base=16), twos_complement(hex[4:12]), twos_complement(hex[12:20]), to_bool(bin[3]), to_bool(bin[2]))
        #creates a packet object with all relevent information
        print(p)
        #prints the packet object
    except:
        print("Incorrect format of input!")

elif user_input=="P":

    try:
        pt = input("packet_type:")
        pv = input("packet_version:")
        teuwh = input("total_energy_used_watt_hours:")
        tdms = input("time_drift_milli_seconds:")
        giw = input("geyser_is_warm (True/False):")
        gidp = input("geyser_is_drawing_power (True/False):")
        #user input, if incorrect will throw an error

        pt = struct.pack('B',int(pt))
        s = pt.hex()
        pv = struct.pack('B', int(pv))
        s = s+pv.hex()
        teuwh = struct.pack('I', int(teuwh))
        s = s+(teuwh.hex())
        tdms = struct.pack('i', int(tdms))
        s = s+(tdms.hex())
        giw = struct.pack('?', to_int(giw))
        gidp = struct.pack('?', to_int(gidp))
        #use "struct pack" feature to format strings for packing data

        flags = (gidp+giw).hex()
        #combines flags and converts to hex
        s = s+'0'+str(bin_to_int(flags))
        #converts the binary to integer
        print(s)
    except:
        print("Incorrect format of input!")
