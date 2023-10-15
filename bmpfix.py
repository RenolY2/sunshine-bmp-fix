from struct import pack, unpack

def read_uint32(f):
    return unpack("I", f.read(4))[0]
def read_uint8(f):
    return unpack("B", f.read(1))[0]
    
def write_uint8(f, val):
    f.write(pack(">B", val))
    
def write_uint32(f, val):
    f.write(pack("I", val))
    
def fix_bmp(path):
    with open(path, "r+b") as f:
        f.seek(0x12)
        width = read_uint32(f)
        height = read_uint32(f)
        print("Image dimension:", width, "by", height)
        
        
        f.seek(0xA)
        dataoffset = read_uint32(f) 
        f.seek(dataoffset)
        pixeldata = f.read(width*height)
        f.seek(0x36)
        colortable = []
        
        for i in range(256):
            colortable.append(read_uint8(f))
            f.read(3)
        newoffset = f.tell()
        
        f.write(pixeldata)
        f.seek(newoffset)
            
        for i in range(width*height):
            pos = f.tell()
            index = read_uint8(f)
            color = colortable[index]
            f.seek(pos)
            write_uint8(f, color)
        
        f.seek(0x36)
        for i in range(256):
            write_uint8(f, i)
            write_uint8(f, i)
            write_uint8(f, i)
            write_uint8(f, 0xFF)
        
        f.seek(0xA)
        write_uint32(f, newoffset)
        
        f.seek(0x2E)
        write_uint32(f, 0)
        write_uint32(f, 0)
            
if __name__ == "__main__":
    import sys 
    if len(sys.argv) <= 1:
        print("Script for fixing 8-bit BMPs for use with Super Mario Sunshine.")
        print("Usage: python ./bmpfix.py <path to bmp>")
        print("Warning: The file will be fixed in-place.")
    else:
        in_file = sys.argv[1]
        if in_file.lower().endswith(".bmp"):
            fix_bmp(in_file)
            print("BMP palette fixed.")
        else:
            print("File must be BMP!")