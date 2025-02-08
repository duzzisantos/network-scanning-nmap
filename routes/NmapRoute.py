from fastapi import APIRouter
from models.NmapModel import NmapResultModel, ScanArgs
from api.NmapScan import nmap_port_scan

nmap_scanning_router = APIRouter()


@nmap_scanning_router.post("/GetPortScanningResults")
def port_scanning():
    return nmap_port_scan(ScanArgs)
