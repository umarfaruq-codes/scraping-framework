import csv


def save_csv(data: list[dict], filepath : str, fieldnames: list | None=None):
    with open(filepath, "w", newline="", encoding="utf-8") as file:

        if fieldnames is None and data:
            fieldnames = data[0].keys()

        if not fieldnames:
            raise ValueError("Field names must be provided when data is empty")
        
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)
        
