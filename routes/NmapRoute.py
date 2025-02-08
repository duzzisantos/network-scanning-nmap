from fastapi import APIRouter
from models.NmapModel import ScanArgs
from api.NmapScan import nmap_port_scan
from api.NmapPortStates import nmap_port_states
from api.NmapAdvanced import nmap_scan_advanced


nmap_scanning_router = APIRouter()


@nmap_scanning_router.post("/GetPortScanningDetails")
async def port_scanning(model: ScanArgs):
    return nmap_port_scan(model)


@nmap_scanning_router.post("/GetPortScanningState")
async def port_state(model: ScanArgs):
    return nmap_port_states(model)


@nmap_scanning_router.post("/GetAdvancedNmapScan")
async def advanced_scanning(model: ScanArgs):
    return nmap_scan_advanced(model)
