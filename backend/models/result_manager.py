class ResultManager:

    def __init__(self):

        self.result = {

            "scan_info": {},

            "discovery": {},

            "reconnaissance": {},

            "enumeration": {},

            "vulnerabilities": [],

            "findings": [],

            "evidence": [],

            "risk_summary": {},

            "report": {}

        }

    def add_discovery(self, module_name, data):

        self.result["discovery"][module_name] = data

    def get_result(self):

        return self.result