import json

def check_vulnerabilities(df, config_path="config/rules.json"):
    with open(config_path, "r") as f:
        rules = json.load(f)

    alerts = []
    for ip, count in df['ip'].value_counts().items():
        if count > rules["failed_login_threshold"]:
            alerts.append(f"⚠️ IP {ip} exceeded login attempts: {count}")
        if ip in rules["suspicious_ips"]:
            alerts.append(f"🚨 IP {ip} is blacklisted!")

    return alerts
