import nmap
from utils.IPValidator import ip_validator
from models.NmapModel import ScanArgs


def nmap_port_states(item: ScanArgs):
    try:
        if item.ip_address.__ne__("") and item.port_range.__ne__(""):
            nm = nmap.PortScanner()

            if len(nm.all_hosts()) > 0:
                host_information = []
                current_host = {}
                for host in nm.all_hosts():
                    for proto in nm[host].all_protocols():
                        lport = nm[host][proto].keys()

                        for port in lport:
                            current_host["port"] = port
                            current_host["state"] = nm[host][proto][port]["state"]

                            host_information.append(current_host)
                        return host_information

            else:
                return {"You do not have any hosts on this network"}

        else:
            return {"You must provide IP Address and Port Range"}

    except Exception as e:
        return e
