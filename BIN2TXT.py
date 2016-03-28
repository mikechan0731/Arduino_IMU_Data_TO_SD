import binascii as ba

"""
def byte_from_file(file_name, chunksize = 1000 * 20):
    with open(file_name, 'rb') as f:
        while True:
            chunk = f.read(chunksize)
            if chunk:
                for b in chunk:
                    yield b
            else:
                break
"""



fn = raw_input("Enter file name: ")
if len(fn) < 1 : fn = "IMU_LOG.bin"

f = open(fn, 'rb')




count = 0

all_data = []
line20_unsort = []

for b in f.read():

    line20_unsort.append(ba.b2a_hex(b))

    count +=1

    if count % 20 == 0:

        line20_sorted = []

        line20_sorted = [
        line20_unsort[3] + line20_unsort[2] + line20_unsort[1] + line20_unsort[0],
        line20_unsort[7] + line20_unsort[6] + line20_unsort[5] + line20_unsort[4],
        line20_unsort[9] + line20_unsort[8],
        line20_unsort[11] + line20_unsort[10],
        line20_unsort[13] + line20_unsort[12],
        line20_unsort[15] + line20_unsort[14],
        line20_unsort[17] + line20_unsort[16],
        line20_unsort[19] + line20_unsort[18] ]


        data_not_ok = []
        data_ok = []

        for hx in line20_sorted:
            dc = int(hx, 16)
            data_not_ok.append(dc)

        for n in range(len(data_not_ok)):
            if n <= 1 :
                data_ok.append(data_not_ok[n])
            else:
                if data_not_ok[n] > 30000:
                    data_ok.append(str(int(data_not_ok[n])-65536))
                else:
                    data_ok.append(data_not_ok[n])

        print data_ok
        all_data.append(data_ok)
        line20_unsort = []


fw = open("IMU_LOG_ascii.txt", 'w')

for eline in all_data:
    edate = ""
    for e in range(len(eline)):
        if e < 7 :
            edate = edate + str(eline[e]) + "\t"
        elif e == 7:
            edate = edate + str(eline[e])
        else:
            print 'error'

    print >> fw, edate

fw.close()

f.close()
