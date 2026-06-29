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

    def add_reconnaissance(self, key, value):
    
        self.result["reconnaissance"][key] = value

    def add_enumeration(self, key, value):
    
        self.result["enumeration"][key] = value


    def add_vulnerability(self, vulnerability):
        self.result["vulnerabilities"].append(vulnerability)


    def add_finding(self, finding):
        self.result["findings"].append(finding)


    def add_evidence(self, evidence):
        self.result["evidence"].append(evidence)

    def get_result(self):

        return self.result