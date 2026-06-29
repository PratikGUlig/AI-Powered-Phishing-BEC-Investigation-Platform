from reportlab.platypus import *

from reportlab.lib.styles import *

from datetime import datetime

import os


def generate_report(data):

    os.makedirs(
        "reports",
        exist_ok=True
    )

    filename = (
        "reports/"
        "investigation_report.pdf"
    )

    doc = SimpleDocTemplate(
        filename
    )

    styles = (
        getSampleStyleSheet()
    )

    story = []

    title = Paragraph(
        "<b><font size='18'>"
        "PHISHING "
        "INVESTIGATION "
        "REPORT"
        "</font></b>",
        styles["Title"]
    )

    story.append(title)

    story.append(
        Spacer(1,20)
    )

    story.append(
        Paragraph(
            f"Date: "
            f"{datetime.now()}",
            styles["Normal"]
        )
    )

    story.append(
        Spacer(1,10)
    )

    story.append(
        Paragraph(
            f"<b>Risk Score:</b> "
            f"{data['score']}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Severity:</b> "
            f"{data['severity']}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Sender:</b> "
            f"{data['sender']}",
            styles["Normal"]
        )
    )

    story.append(
        Spacer(1,20)
    )

    story.append(
        Paragraph(
            "<b>Indicators</b>",
            styles["Heading2"]
        )
    )

    for i in data["indicators"]:

        story.append(
            Paragraph(
                f"• {i}",
                styles["Normal"]
            )
        )

    story.append(
        Spacer(1,20)
    )

    story.append(
        Paragraph(
            "<b>MITRE "
            "ATT&CK</b>",
            styles["Heading2"]
        )
    )

    for m in data["mitre"]:

        story.append(
            Paragraph(
                f"{m['id']} : "
                f"{m['name']}",
                styles["Normal"]
            )
        )

    story.append(
        Spacer(1,20)
    )

    story.append(
        Paragraph(
            "<b>AI "
            "Investigation</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            data["ai"],
            styles["Normal"]
        )
    )

    doc.build(story)

    return filename