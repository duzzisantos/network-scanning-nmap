import nmap3
from models.NmapModel import ScanArgs


def nmap_scan_advanced(item: ScanArgs):
    try:
        if item.hostname.__ne__(""):
            nmap = nmap3.Nmap()
            brute_result = nmap.nmap_dns_brute_script(item.hostname)

            # detect_firewall = nmap.nmap_detect_firewall(item.hostname)
            os_information = nmap.nmap_os_detection(item.hostname)
            listed_targets = nmap.nmap_list_scan(item.hostname)
            list_vulnerabilities = nmap.nmap_version_detection(
                item.hostname, args="--script vulners --script-args mincvss+5.0"
            )

            return dict(
                {
                    "dns_brute": brute_result,
                    # "detected_firewall": detect_firewall,
                    "operating_systems": os_information,
                    "listed_targets": listed_targets,
                    "list_vulnerabilities": list_vulnerabilities,
                }
            )
        else:
            return dict({"error_message": "Hostname was not found. Provide one."})
    except Exception as e:
        return e
