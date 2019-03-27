import csv


def read_csv(filename):
    data = dict()
    data["t"] = []
    data["vin"] = []
    data["vout"] = []

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["x-axis"] != "second":
                data["t"].append(float(row["x-axis"]) )
                data["vout"].append(float(row["1"]) )
                data["vin"].append(float(row["3"]) )

    return data


def read_csv_bode(filename):
    data = dict()

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            for content in row.keys():
                if not content in data:
                    data[content] = []

                data[content].append(float(row[content]))
    return data

