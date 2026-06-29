import streamlit as st

from indicators import *
from analyzer import *
from risk_engine import *
from ollama_ai import *
from domain_analysis import *
from virustotal_analysis import *
from mitre_mapping import *
from report_generator import *
from ioc_export import *
from bec_detection import *
from wazuh_export import *

st.title(
    "AI Phishing Email Analyzer"
)

email = st.text_area(
    "Paste suspicious email",
    height=300
)

if st.button("Analyze"):

    ##################################################
    # BASIC ANALYSIS
    ##################################################

    urls = extract_urls(email)

    sender = extract_sender(email)

    attachments = detect_attachment(email)

    keywords = keyword_analysis(email)

    suspicious = suspicious_urls(urls)

    spoof = detect_spoof(sender)

    ##################################################
    # BEC
    ##################################################

    bec_result = detect_bec(email)

    bec = False

    if bec_result["score"] >= 30:
        bec = True

    ##################################################
    # DOMAIN
    ##################################################

    domain_results = []

    for url in urls:

        domain = extract_domain(url)

        if domain:

            age = get_domain_age(domain)

            domain_results.append({

                "domain": domain,

                "age": age
            })

    ##################################################
    # VIRUSTOTAL
    ##################################################

    vt_results = []

    for url in urls:

        result = check_url(url)

        vt_results.append({

            "url": url,

            "result": result
        })

    ##################################################
    # DOMAIN RISK
    ##################################################

    new_domain = False

    for d in domain_results:

        if d["age"] is not None:

            if d["age"] < 30:
                new_domain = True

    ##################################################
    # VT RISK
    ##################################################

    malicious = False

    for vt in vt_results:

        if vt["result"]:

            if vt["result"]["malicious"] > 0:
                malicious = True

    ##################################################
    # ANALYSIS OBJECT
    ##################################################

    analysis = {

        "suspicious_urls":
            suspicious,

        "keywords":
            keywords,

        "spoof":
            spoof,

        "attachments":
            attachments,

        "new_domain":
            new_domain,

        "malicious":
            malicious,

        "bec":
            bec
    }

    ##################################################
    # MITRE
    ##################################################

    mitre = map_attack(
        analysis
    )

    ##################################################
    # SCORE
    ##################################################

    score = calculate_score(
        analysis
    )

    severity = get_severity(
        score
    )

    ##################################################
    # AI
    ##################################################

    ai = explain(
        analysis
    )

    print("\n========== AI OUTPUT ==========")
    print(ai)
    print(type(ai))
    print("===============================\n")

    ##################################################
    # INDICATORS
    ##################################################

    indicators = []

    if suspicious:
        indicators.append(
            "Suspicious URL"
        )

    if spoof:
        indicators.append(
            "Sender Spoofing"
        )

    if keywords:
        indicators.append(
            "Credential Harvesting"
        )

    if attachments:
        indicators.append(
            "Attachment"
        )

    if bec:
        indicators.append(
            "Business Email Compromise"
        )

    ##################################################
    # PDF REPORT
    ##################################################

    report_data = {

        "score":
            score,

        "severity":
            severity,

        "sender":
            sender,

        "indicators":
            indicators,

        "mitre":
            mitre,

        "ai":
            ai
    }

    report = generate_report(
        report_data
    )

    ##################################################
    # IOC EXPORT
    ##################################################

    ioc = {

        "sender":
            sender,

        "urls":
            urls,

        "domains":
            domain_results,

        "keywords":
            keywords,

        "mitre":
            mitre,

        "score":
            score,

        "severity":
            severity,

        "bec":
            bec
    }

    json_file = export_json(
        ioc
    )

    csv_file = export_csv(
        ioc
    )

    ##################################################
    # WAZUH EXPORT
    ##################################################

    wazuh_data = {

        "sender":
            sender,

        "severity":
            severity,

        "score":
            score,

        "indicators":
            indicators,

        "mitre":
            mitre,

        "bec":
            bec
    }

    wazuh_file = export_wazuh(
        wazuh_data
    )

    ##################################################
    # RESULTS
    ##################################################

    st.header(
        "Results"
    )

    st.metric(
        "Risk Score",
        score
    )

    st.metric(
        "Severity",
        severity
    )

    ##################################################
    # SENDER
    ##################################################

    st.subheader(
        "Sender"
    )

    st.write(
        sender
    )

    ##################################################
    # BEC
    ##################################################

    st.subheader(
        "BEC Analysis"
    )

    for indicator in bec_result[
        "indicators"
    ]:

        st.write(
            f"• {indicator}"
        )

    if bec:

        st.error(
            "Business Email Compromise Detected"
        )

    else:

        st.success(
            "No BEC indicators"
        )

    ##################################################
    # DOMAIN
    ##################################################

    st.subheader(
        "Domain Age"
    )

    if len(domain_results) == 0:

        st.warning(
            "No domains found."
        )

    else:

        for d in domain_results:

            st.write(
                f"Domain: {d['domain']}"
            )

            if d["age"] is not None:

                st.write(
                    f"Age: {d['age']} days"
                )

            else:

                st.warning(
                    "WHOIS information unavailable"
                )

    ##################################################
    # VIRUSTOTAL
    ##################################################

    st.subheader(
        "VirusTotal Analysis"
    )

    for vt in vt_results:

        st.write(
            f"URL: {vt['url']}"
        )

        if vt["result"]:

            st.write(
                f"Malicious: {vt['result']['malicious']}"
            )

            st.write(
                f"Suspicious: {vt['result']['suspicious']}"
            )

            st.write(
                f"Harmless: {vt['result']['harmless']}"
            )

    ##################################################
    # MITRE
    ##################################################

    st.subheader(
        "MITRE ATT&CK"
    )

    for m in mitre:

        st.write(
            f"{m['id']} : {m['name']}"
        )

    ##################################################
    # AI
    ##################################################

    st.subheader(
        "AI Explanation"
    )

    st.write(
        ai
    )

    ##################################################
    # DOWNLOADS
    ##################################################

    st.subheader(
        "Downloads"
    )

    with open(
        report,
        "rb"
    ) as f:

        st.download_button(
            "Download PDF",
            f,
            file_name=
            "investigation_report.pdf"
        )

    with open(
        json_file,
        "rb"
    ) as f:

        st.download_button(
            "Download IOC JSON",
            f,
            file_name=
            "ioc_export.json"
        )

    with open(
        csv_file,
        "rb"
    ) as f:

        st.download_button(
            "Download IOC CSV",
            f,
            file_name=
            "ioc_export.csv"
        )

    with open(
        wazuh_file,
        "rb"
    ) as f:

        st.download_button(
            "Download Wazuh Alert",
            f,
            file_name=
            "wazuh_alert.json"
        )