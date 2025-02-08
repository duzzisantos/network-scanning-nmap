import nmap3
from models.NmapModel import ScanArgs


def nmap_port_scan(item: ScanArgs):
    try:
        if item.hostname.__ne__(""):

            ## Initialize port scanner if IP address and port range are provided
            nm = nmap3.Nmap()
            nmap_sync = nmap3.NmapScanTechniques()
            results = nm.scan_top_ports(item.hostname)
            sync_results = nmap_sync.nmap_syn_scan(item.hostname, args="--privileged")

            return dict(
                {
                    "hostname": item.hostname,
                    "host_details": results,
                    "sync_results": sync_results,
                }
            )
        else:
            return dict(
                {
                    "error_message": "Error occured. You must provide network scanning details."
                }
            )

    except Exception as e:
        return e
