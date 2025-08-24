import re
import pandas as pd

def parse_auth_log(file):
    lines = file.readlines()
    failed_logins = []
    for line in lines:
        line = line.decode("utf-8")  # for Streamlit upload
        if "Failed password" in line:
            match = re.search(r'(\w{3} \d+ \d+:\d+:\d+).*Failed password for .* from (\d+\.\d+\.\d+\.\d+)', line)
            if match:
                failed_logins.append({
                    "timestamp": match.group(1),
                    "ip": match.group(2)
                })
    return pd.DataFrame(failed_logins)
