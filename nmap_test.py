import nmapthon as nm
scanner = nm.NmapScanner('192.168.1.0/24', ports='22,53,443', arguments='-A -T4')
scanner.run()
# for every host scanned
for host in scanner.scanned_hosts():
# for every protocol scanned for each host
for proto in scanner.all_protocols(host):
# for each scanned port
for port in scanner.scanned_ports(host, proto):
# Get service object
service = scanner.service(host, proto, port)
if service is not None:
    print("Service name: {}".format(service.name))
    print("Service product: {}".format(service.product))
    for cpe in service.all_cpes():
        print("CPE: {}".format(cpe))
    for name, output in service.all_scripts():
        print("Script: {}\nOutput: {}".format(name, output))
    # You could also do print(str(service))
    # You could also know if 'ssh-keys' script was launched and print the
    ˓→output
    if 'ssh-keys' in service:
        print("{}".format(service['ssh-keys']))
