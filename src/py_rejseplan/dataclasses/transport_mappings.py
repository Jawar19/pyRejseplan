from py_rejseplan.enums import TransportClass

# Mapping from string keys to TransportClass enum values
DEPARTURE_TYPE_TO_CLASS = {
    "ic": TransportClass.IC,
    "icl": TransportClass.ICL,
    "re": TransportClass.RE,
    "tog": TransportClass.TOG,
    "s_tog": TransportClass.S_TOG,
    "bus": TransportClass.BUS,
    "express_bus": TransportClass.EXPRESS_BUS,
    "night_bus": TransportClass.NIGHT_BUS,
    "flexible_bus": TransportClass.FLEXIBLE_BUS,
    "ferry": TransportClass.FERRY,
    "metro": TransportClass.METRO,
    "letbane": TransportClass.LETBANE,
    "flight": TransportClass.FLIGHT,
}

CATOUT_TO_CLASS = {
    # IC Group (cls=1)
    "IC": TransportClass.IC,
    "IB": TransportClass.IC,
    # ICL Group (cls=2)
    "ICL": TransportClass.ICL,
    "ICL-X": TransportClass.ICL,
    "IL": TransportClass.ICL,  # ICL+
    # Regional trains (cls=4)
    "Re": TransportClass.RE,
    "RA": TransportClass.RE,
    "RX": TransportClass.RE,
    # Long distance trains (cls=8)
    "EC": TransportClass.TOG,
    "IR": TransportClass.TOG,
    "IP": TransportClass.TOG,
    "ICE": TransportClass.TOG,
    "SJ": TransportClass.TOG,
    "EN": TransportClass.TOG,
    "ICN": TransportClass.TOG,
    "Pågatog": TransportClass.TOG,
    "NAT": TransportClass.TOG,  # Night trains
    "L": TransportClass.TOG,  # Local trains
    "SKOLE": TransportClass.TOG,
    "MTOG": TransportClass.TOG,
    "E-Tog": TransportClass.TOG,
    "R-netTog": TransportClass.TOG,
    # S-trains (cls=16)
    "S-Tog": TransportClass.S_TOG,
    # Regular buses (cls=32)
    "Bus": TransportClass.BUS,
    "Bybus": TransportClass.BUS,
    "E-Bus": TransportClass.BUS,
    "ServiceB": TransportClass.BUS,
    "R-net": TransportClass.BUS,
    "C-Bus": TransportClass.BUS,
    "TraktBus": TransportClass.BUS,
    "Taxa": TransportClass.BUS,
    # Express buses (cls=64)
    "X Bus": TransportClass.EXPRESS_BUS,
    "Ekspresb": TransportClass.EXPRESS_BUS,
    "Fjernbus": TransportClass.EXPRESS_BUS,
    # Night and special buses (cls=128)
    "Natbus": TransportClass.NIGHT_BUS,
    "Havnebus": TransportClass.NIGHT_BUS,
    "Flybus": TransportClass.NIGHT_BUS,
    "Sightseeing bus": TransportClass.NIGHT_BUS,
    "HV-bus": TransportClass.NIGHT_BUS,
    "Si-bus": TransportClass.NIGHT_BUS,
    # Flexible transport (cls=256)
    "Flexbus": TransportClass.FLEXIBLE_BUS,
    "Flextur": TransportClass.FLEXIBLE_BUS,
    "TELEBUS": TransportClass.FLEXIBLE_BUS,
    "Nærbus": TransportClass.FLEXIBLE_BUS,
    # Ferry (cls=512)
    "Færge": TransportClass.FERRY,
    "HF": TransportClass.FERRY,  # Fast ferry
    # Metro (cls=1024)
    "MET": TransportClass.METRO,
    # Light rail (cls=2048)
    "Letbane": TransportClass.LETBANE,
    "LTBUS": TransportClass.LETBANE,
    # Flight (cls=4096)
    "Fly": TransportClass.FLIGHT,
}