import ipaddress


def ip_validator(ip_address: str):
    return ipaddress.ip_address(ip_address, strict=True)
