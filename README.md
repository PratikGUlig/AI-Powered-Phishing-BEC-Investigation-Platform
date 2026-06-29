# 🛡️ AI-Powered Phishing & Business Email Compromise (BEC) Investigation Platform

An enterprise-style cybersecurity investigation platform designed to automate phishing and Business Email Compromise (BEC) investigations using Artificial Intelligence, Threat Intelligence, MITRE ATT&CK, and SIEM integration.

---

# 📌 Overview

This project simulates a real-world Security Operations Center (SOC) workflow by analyzing suspicious emails, extracting Indicators of Compromise (IOCs), performing threat intelligence enrichment, detecting phishing and Business Email Compromise (BEC) attacks, mapping adversary techniques to the MITRE ATT&CK framework, and generating automated investigation reports.

The platform integrates Local AI using **Ollama + Mistral LLM** to provide human-readable investigation summaries and security recommendations.

---

# 🚀 Features

## ✉️ Email Analysis

* Sender extraction
* URL extraction
* Attachment detection
* Phishing keyword analysis
* Sender spoofing detection
* Credential harvesting detection

---

## 🎯 Phishing Detection

* Suspicious URL detection
* Domain reputation analysis
* Domain age analysis
* Lookalike domain detection
* Brand impersonation detection

---

## 🏢 Business Email Compromise (BEC) Detection

* Urgency detection
* Authority impersonation detection
* Financial request detection
* Secrecy indicator analysis
* Executive impersonation detection

---

## 🌐 Threat Intelligence

* WHOIS integration
* Domain age analysis
* VirusTotal integration
* IOC extraction and enrichment

---

## 🗺️ MITRE ATT&CK Mapping

| Technique | Description              |
| --------- | ------------------------ |
| T1566     | Phishing                 |
| T1566.001 | Spearphishing Attachment |
| T1566.002 | Spearphishing Link       |
| T1056     | Input Capture            |
| T1583     | Acquire Infrastructure   |
| T1656     | Impersonation            |

---

## 🤖 AI Investigation Engine

Powered by:

* Ollama
* Mistral LLM

Capabilities:

* AI investigation summaries
* Risk explanations
* Security recommendations
* Human-readable incident analysis

---

## 📊 Reporting & SIEM Integration

* PDF incident reports
* IOC JSON export
* IOC CSV export
* Wazuh alert generation
* Risk scoring
* Severity classification

---

# 🛠️ Technology Stack

| Category            | Technologies     |
| ------------------- | ---------------- |
| Language            | Python           |
| Frontend            | Streamlit        |
| AI                  | Ollama + Mistral |
| Threat Intelligence | VirusTotal API   |
| Domain Analysis     | WHOIS            |
| Security Framework  | MITRE ATT&CK     |
| SIEM                | Wazuh            |
| Reporting           | ReportLab        |
| Data Export         | JSON, CSV        |

---

# 🏗️ Project Architecture

![Architecture](screenshots/architecture.png)

---

# 📷 Screenshots

## Dashboard

![Dashboard](screenshots/01_dashboard.png)

---

## Investigation Results

![Results](screenshots/02_results_dashboard.png)

---

## MITRE ATT&CK Mapping

![MITRE](screenshots/03_mitre_mapping.png)

---

## AI Investigation

![AI Investigation](screenshots/04_ai_investigation.png)

---

# 🔍 Example Investigation

## Sample Phishing Email

```text
From: security@paypa1.com

Subject: Verify Account

Dear Customer,

Your account has been suspended.

Please verify immediately:

http://paypal-security-login.xyz

invoice.docm

Click here immediately.

Regards,
PayPal Security Team
```

---

## Detection Result

```text
Risk Score: 85

Severity: HIGH

Indicators:
✓ Suspicious URL
✓ Sender Spoofing
✓ Credential Harvesting
✓ Business Email Compromise

MITRE ATT&CK:
T1566.002
T1566.001
T1056
T1583
T1656
```

---

# 📁 Project Structure

```text
AI-Powered-Phishing-BEC-Investigation-Platform/

app.py

analyzer.py
indicators.py
risk_engine.py
bec_detection.py
domain_analysis.py
virustotal_analysis.py
mitre_mapping.py
ollama_ai.py
report_generator.py
ioc_export.py
wazuh_export.py

sample_emails/
examples/
screenshots/

requirements.txt
README.md
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/PratikGUlig/AI-Powered-Phishing-BEC-Investigation-Platform.git

cd AI-Powered-Phishing-BEC-Investigation-Platform
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🤖 Install Ollama

Download Ollama:

https://ollama.com/download

Install Mistral:

```bash
ollama pull mistral
```

Verify:

```bash
ollama list
```

---

# ▶️ Run Project

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

# 🧪 Test Cases

Included test cases:

* PayPal Phishing
* Amazon Phishing
* Google Verification
* Attachment-based Phishing
* Banking Fraud
* Legitimate Email
* CEO Fraud/BEC
* Cryptocurrency Phishing

---

# 🎯 Skills Demonstrated

* Python
* Streamlit
* Cyber Threat Intelligence
* VirusTotal
* WHOIS
* MITRE ATT&CK
* Business Email Compromise
* Incident Response
* Security Operations Center (SOC)
* Detection Engineering
* IOC Analysis
* Threat Hunting
* AI Security
* Ollama
* SIEM Integration
* Wazuh

---

# 🔮 Future Improvements

* SPF/DKIM/DMARC validation
* Attachment sandboxing
* YARA rule integration
* URL sandbox analysis
* Threat feed enrichment
* Docker deployment
* Multi-user authentication
* SOC dashboard analytics

---

# 👨‍💻 Author

### Pratik Gulig

Cybersecurity Analyst | SOC | VAPT | Threat Detection | AI Security

GitHub:
https://github.com/PratikGUlig

---

# ⭐ If you found this project useful, please consider giving it a star.
