from pathlib import Path

# Project Root
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Database
DATABASE_PATH = BASE_DIR / "knowledgebase" / "sqlite" / "knowledgebase.db"

# Reports
REPORTS_PATH = BASE_DIR / "reports"

# Evidence
EVIDENCE_PATH = BASE_DIR / "evidence"

# Logs
LOGS_PATH = BASE_DIR / "backend" / "logs"

# Scanner Version
SCANNER_NAME = "WebAppSec Scanner"
VERSION = "0.1.0"