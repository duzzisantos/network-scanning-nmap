from fastapi import APIRouter
from models.NmapModel import NmapResultModel, ScanArgs
from api.NmapScan import nmap_port_scan
from api.NmapPortStates import nmap_port_states

nmap_scanning_router = APIRouter()


@nmap_scanning_router.post("/GetPortScanningDetails")
async def port_scanning(model: ScanArgs):
    return nmap_port_scan(model)


@nmap_scanning_router.post("/GetPortScanningState")
async def port_state(model: ScanArgs):
    return nmap_port_states(model)
