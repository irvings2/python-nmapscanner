import nmap

scanner = nmap.PortScanner()

target = input("Ingrese el host o hosts: ")
ports = input("Ingrese el puerto o rango de puertos: ")
options = input("Ingrese los argumentos: ")
aux = input("Desea ejecutar el comando como superusuario? (s/n) ")

if aux == 's' or 'S':
    scanner.scan(target, ports=ports, arguments=options, sudo=True)
else:
    scanner.scan(target, ports=ports, arguments=options)

print("")
for host in scanner.all_hosts():
    print("Host: ", host)
    print("State: ", scanner[host].state())
    for proto in scanner[host].all_protocols():
        print("Protocol: ", proto)
        ports = scanner[host][proto].keys()
        for port in ports:
            print(f"Port:\t{port}")
            print(f"State:\t{scanner[host][proto][port]['state']}")
            print(f"Name:\t{scanner[host][proto][port]['name']}")
            if 'product' in scanner[host][proto][port]:
                print(f"Product: {scanner[host][proto][port]['product']}")
            if 'extrainfo' in scanner[host][proto][port]:
                print(f"Extrainfo: {scanner[host][proto][port]['extrainfo']}")
            print("")
