import nmap
from utils.IPValidator import ip_validator
from models.NmapModel import ScanArgs


def nmap_port_states(item: ScanArgs):
    try:
        if item.hostname.__ne__(""):
            nm = nmap.PortScanner()

            host_information = []
            current_host = {}
            for host in nm.all_hosts():
                for proto in nm[host].all_protocols():
                    lport = nm[host][proto].keys()

                    for port in lport:
                        current_host["port"] = port
                        current_host["state"] = nm[host][proto][port]["state"]

                        host_information.append(current_host)
                    return current_host
                return host_information
            return dict({"results": host_information})

        else:
            return dict({"error_message": "You must provide IP Address and Port Range"})

    except Exception as e:
        return e
