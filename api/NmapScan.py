import nmap
from utils.IPValidator import ip_validator
from models.NmapModel import ScanArgs


def nmap_port_scan(item: ScanArgs):
    try:
        is_valid = ip_validator(item.ip_address)
        if item.ip_address.__ne__("") and item.port_range.__ne__("") and is_valid:

            ## Initialize port scanner if IP address and port range are provided
            nm = nmap.PortScanner()
            nm.scan(item.ip_address, item.port_range)

            ## Response body
            scan_information = nm.scaninfo()
            scan_hosts = nm.all_hosts()
            get_host_name = nm[item.ip_address].hostname()
            get_protocols = nm[item.ip_address].all_protocols()
            has_tcp = nm[item.ip_address].has_tcp()
            tcp_details = nm[item.ip_address].tcp(22)

            scan_results = {
                "current_ip_address": item.ip_address,
                "scan_information": scan_information,
                "scan_hosts": scan_hosts,
                "get_host_name": get_host_name,
                "get_protocols": get_protocols,
                "has_tcp": has_tcp,
                "tcp_details": tcp_details,
            }

            return dict(scan_results)
        else:
            return {"Error occured. You must provide network scanning details."}

    except Exception as e:
        return e

    except ConnectionError as ce:
        return ce
