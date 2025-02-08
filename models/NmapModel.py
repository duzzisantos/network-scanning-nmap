from pydantic import BaseModel
from typing import List, Dict


class NmapResultModel(BaseModel):
    current_ip_address: str
    scan_information: Dict
    scan_hosts: List[str]
    get_host_name: str
    get_protocols: List[str]
    has_tcp: bool
    tcp_details: Dict


class ScanArgs(BaseModel):
    ip_address: str
    port_range: str
