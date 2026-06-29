import json
import csv
import os


def export_json(data):

    os.makedirs(
        "reports",
        exist_ok=True
    )

    filename = (
        "reports/"
        "ioc_export.json"
    )

    with open(

        filename,

        "w",

        encoding="utf-8"

    ) as file:

        json.dump(

            data,

            file,

            indent=4,

            default=str
        )

    return filename


def export_csv(data):

    os.makedirs(
        "reports",
        exist_ok=True
    )

    filename = (
        "reports/"
        "ioc_export.csv"
    )

    with open(

        filename,

        "w",

        newline="",

        encoding="utf-8"

    ) as file:

        writer = csv.writer(
            file
        )

        writer.writerow(
            [
                "Indicator",
                "Value"
            ]
        )

        for key, value in data.items():

            writer.writerow(
                [
                    key,
                    str(value)
                ]
            )

    return filename