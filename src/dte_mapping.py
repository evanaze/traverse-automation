import datetime

phases = ("GRIT", "PERFORMANCE", "BUILD")
body_sections = ("Upper", "Lower", "Full")


def parse_date(instr: str) -> datetime.date:
    stripped_str = ",".join(instr.split(",")[1:]).strip()
    parsed_str = datetime.datetime.strptime(stripped_str, "%B %d, %Y")
    return parsed_str


def create_dtemap(length: int = 10) -> dict:
    dtemap = {}
    i = 0
    for start in range(length):
        start *= 9
        for phase in phases:
            for body_section in body_sections:
                i += 1
                dte = datetime.date(2025, 1, 1) + datetime.timedelta(start + i)
                dtemap[dte] = (phase, body_section)
    return dtemap
