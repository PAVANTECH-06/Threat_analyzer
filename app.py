import streamlit as st
from modules.log_Parser import parse_auth_log
from modules.vuln_scanner import check_vulnerabilities
from modules.visualizer import plot_failed_logins
from modules.report_gen import generate_report

st.title("🔐 Threat Analyzer Dashboard")

log_file = st.file_uploader("Upload Log File", type=["log", "txt"])

if log_file:
    df = parse_auth_log(log_file)
    st.subheader("Parsed Log Data")
    st.dataframe(df)

    alerts = check_vulnerabilities(df)
    st.subheader("Alerts")
    for alert in alerts:
        st.error(alert)

    st.subheader("Visualization")
    plot_failed_logins(df)

    if st.button("Generate Report"):
        filename = generate_report(alerts)

        # Read file in binary for download
        with open(filename, "rb") as f:
            pdf_bytes = f.read()

        st.success("✅ Report generated successfully!")
        st.download_button(
            label="📥 Download Threat Report",
            data=pdf_bytes,
            file_name=filename,
            mime="application/pdf"
        )
