def build_payload(interface_name):
    return {
        "ietf-interfaces:interface": {
            "name": interface_name,
            "type": "iana-if-type:ethernetCsmacd",
            "enabled": true,
            "ietf-ip:ipv4": {},
            "ietf-ip:ipv6": {}
        }
    }
