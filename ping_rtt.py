import subprocess
import re
import datetime
import csv
import socket

top_site = []
data = {}
keys = {}
public_ip = {}
raw = []
data["min"] = []
data["avg"] = []
data["max"] = []
data["mdev"] = []
data["packet loss"] = []
data["ip"] = []
data["bytes_of_data"] = []
data["time"] = []
data["site"] = []
hostname = socket.gethostname()

f = open("top_canada_site.txt", "r")
for x in f:
    top_site.append(x.strip('\n'))

f = open("ec2_public_ip.txt", "r")
for x in f:
    x = x.split()
    public_ip[x[0]] = x[1]

for location in ["canada", "west", "east", "tokyo", "london"]:
    for site in top_site:
        args = ["ssh", "-i", keys[location], public_ip[location], "ping", "-c", "2", site]
        if location == "canada":
            args = ["ping", "-c", "2", site]

        p = subprocess.Popen(args, stdout=subprocess.PIPE)

        strs = p.communicate()[0].split("\n")
        str_list = filter(None, strs)
        raw.append(str_list)

        data["min"].append(str_list[-1][23:].split('/')[0])
        data["avg"].append(str_list[-1][23:].split('/')[1])
        data["max"].append(str_list[-1][23:].split('/')[2])
        data["mdev"].append(str_list[-1][23:].strip('ms').split('/')[3])
        data["packet loss"].append(re.match(r".*received, (.*)%.*", str_list[-2], re.M|re.I).group(1))
        data["ip"].append(re.match(r"PING.*\((.*)\) 56\(84\) bytes of data", str_list[0], re.M|re.I).group(1))
        data["bytes_of_data"].append(re.match(r".*\) ([0-9]*)\(84\) bytes of data", str_list[0], re.M|re.I).group(1))
        data["time"].append(datetime.datetime.now())
        data["site"].append(re.match(r"PING (.*) \(.*", str_list[0], re.M|re.I).group(1))

        with open(hostname + '_dict.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in data.items():
                writer.writerow([key, value])

        print hostname
print(data['time'][0])

