import os
import json
from datetime import datetime
from jinja2 import Environment, FileSystemLoader, Template

from collectors.cpu_mem import get_cpu_mem_info
from collectors.disk import get_disk_info
from collectors.folders import get_top_folders

REPORTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "reports"))
os.makedirs(REPORTS_DIR, exist_ok=True)

reports_file = fr"{REPORTS_DIR}\reports.json"

cpu_info = get_cpu_mem_info()
disk_info = get_disk_info()
top_folders = get_top_folders()

snapshot = {
    "generated_at": datetime.now().isoformat(timespec="seconds"),
    "cpu_ram": cpu_info,
    "disks": disk_info,
    "folders": top_folders
}

with open(reports_file, "w", encoding="utf-8") as f:
    json.dump(snapshot,f,indent=2,ensure_ascii=False)

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "report")
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
template = env.get_template("template.html")

html_output = template.render(data=snapshot)
html_path = os.path.join(REPORTS_DIR, "system_report.html")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_output)

print(f"[OK] HTML report generated: {html_path}")