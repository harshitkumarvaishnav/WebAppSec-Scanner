from backend.models.result_manager import ResultManager

rm = ResultManager()

rm.add_discovery(
    "dns",
    {
        "ip": "8.8.8.8"
    }
)

rm.add_discovery(
    "http",
    {
        "status": 200
    }
)

print(rm.get_result())