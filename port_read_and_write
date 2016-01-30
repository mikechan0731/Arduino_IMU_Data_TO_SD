import serial
import time

print("Today is " +str (time.strftime("%Y/%m/%d")))
print("\n")
print("Start Time: " + str(time.strftime("%H:%M:%S")))
print("\n")



## read port setting ##
ser = serial.Serial(
    port = 'COM4',\
    baudrate = 38400,\
    parity = serial.PARITY_NONE,\
    stopbits = serial.STOPBITS_ONE,\
    bytesize = serial.EIGHTBITS,\
    timeout = 10)
print("conntected to: " + ser.portstr)



## global varible here ##
count = 1
a = []
record_nums = 500


## print status ##
print("\n")
print("Data receiving...You could stop anytime by press Crtl+C ")



## start timer here ##
t0 = time.clock()



## read and append data to list ##
while True:
    
    try:
        data_get = str(ser.readline())
        data_seri_num = "No." +str(count) +"\t"
        data_time = time.clock()- t0 

        data_all = data_seri_num + str(data_time) + "\t" + data_get

        #print data_all
    
        a.append(data_all)
        count +=1
    except KeyboardInterrupt:
        print 'Processing Stop.'
        break
      
    if count>record_nums: break

## detect used time here ##
used_time = time.clock() - t0



## print status again. ##
print("\n")
print("End Time: " + str(time.strftime("%H:%M:%S")))
print("\n")
print("Collect " + str(len(a)) + " datas.")



## print end time ##
print("\n")
print used_time, " sec used."


## caculate data per sec ##
print("\n")
print("Average data/sec is " + str(len(a)/float(used_time)) )



## ask for print out ##
print("\n")
b = raw_input('Would you wanna print data out? It will take some time... Y/N ')

if b == 'y' or b =='Y' or b == 'Yes':
    for k in a:
        print k
else:
    pass



## ask for write to file ##
c= raw_input('Would you wanna save it (txt)? Y/N ')

if c == 'y' or b =='Y' or b == 'Yes':
    save_txt = open(str(time.strftime("%Y%m%d_")) + 'IMU_LOG.txt', 'wb+')
    for k in a:
        save_txt.write(k)
        #print(k) 
    save_txt.close()
    print("\n")
    print("Data saved.")
else:
    print("\n")
    print("Data not saved.")


## port close ##
ser.close()
print("\n")
print("Port: " + ser.portstr + " closed.")

