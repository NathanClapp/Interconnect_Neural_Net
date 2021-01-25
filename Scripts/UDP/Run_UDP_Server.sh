python3 /home/nathan/Documents/Code/Interconnect_Neural_Net/Scripts/UDP_Demo/UDP_Demo_Server.py | \
while IFS= read -r line
do
 echo $line
 $line >> /home/nathan/Documents/Code/Interconnect_Neural_Net/Scripts/StdIO_Stuff/outfile.txt
done
