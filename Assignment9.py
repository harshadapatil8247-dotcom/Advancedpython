import csv
import json
import os
from pathlib import Path


def read_csv(file_path):
    """Read CSV file and return a list of dictionaries."""

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            raise ValueError("CSV file does not contain a header row.")

        data = list(reader)

    return data


def convert_data_types(data):
    """Convert numeric-looking values into integers or floats."""

    for row in data:
        for key, value in row.items():

            if value is None:
                continue

            value = value.strip()

            try:
                if value.isdigit():
                    row[key] = int(value)

                elif "." in value:
                    row[key] = float(value)

                else:
                    row[key] = value

            except ValueError:
                row[key] = value

    return data


def write_json(data, output_path):
    """Write Python data into a formatted JSON file."""

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


def convert_csv_to_json(input_file, output_file):
    """Complete CSV to JSON conversion process."""

    print("\nReading CSV file...")

    data = read_csv(input_file)

    print(f"Records found: {len(data)}")

    data = convert_data_types(data)

    write_json(data, output_file)

    print("Conversion completed successfully!")
    print(f"JSON file created: {output_file}")


def display_json(file_path):
    """Display the generated JSON file."""

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    print("\nGenerated JSON:")
    print(json.dumps(data, indent=4, ensure_ascii=False))


# Main program
if __name__ == "__main__":

    input_file = Path("students.csv")
    output_file = Path("students.json")

    try:
        convert_csv_to_json(input_file, output_file)
        display_json(output_file)

    except FileNotFoundError as error:
        print(f"Error: {error}")

    except ValueError as error:
        print(f"Invalid data: {error}")

    except Exception as error:
        print(f"Unexpected error: {error}")