import struct

def IEEE(number):
    pack_32 = struct.pack("!f", number)
    unpack_32 = struct.unpack("!I", pack_32)[0]
    bin_32 = f"{unpack_32:032b}"

    sign_32 = bin_32[0]
    exp_32 = bin_32[1:9]
    mantissa = bin_32[9:]

    print(f"for Number = {number}\n32 bit = {bin_32}\nsign = {sign_32}\nexponent = {exp_32}\nmantissa = {mantissa}\n\n")

    pack_64 = struct.pack("!d", number)
    unpack_64= struct.unpack("!Q", pack_64)[0]
    bin_64 = f"{unpack_64:064b}"
    
    sign_64 = bin_64[0]
    exp_64 = bin_64[1:12]
    mantissa = bin_64[12:]
    
    print(f"for Number = {number}\n64 bit = {bin_64}\nsign = {sign_64}\nexponent = {exp_64}\nmantissa = {mantissa}")


IEEE(12)