import csv
from models import LoseitFood, WeighIn
from datetime import datetime
from crud import scoped_session
import argparse


fieldnames_map = {
    'Date': 'raw_date',
    'Name': 'raw_name',
    'Type': 'raw_type',
    'Quantity': 'raw_quantity',
    'Units': 'raw_units',
    'Calories': 'raw_calories',
    'Fat (g)': 'raw_fat_g',
    'Protein (g)': 'raw_protein_g',
    'Carbohydrates (g)': 'raw_carbohydrates_g',
    'Saturated Fat (g)': 'raw_saturated_fat_g',
    'Sugars (g)': 'raw_sugars_g',
    'Fiber (g)': 'raw_fiber_g',
    'Cholesterol (mg)': 'raw_cholesterol_mg',
    'Sodium (mg)': 'raw_sodium_mg',
}


def read_loseit_export(filepath, filetype):
    if filetype == 'food':
        read_food_log(filepath)
    elif filetype == 'weight':
        read_weight_log(filepath)
    else:
        raise ValueError("Unsupported file type.")


def read_weight_log(filepath):
    with open(filepath) as csv_file:
        weight_reader = csv.DictReader(csv_file, delimiter=',', quotechar='"')
        weight_records = []
        for line in weight_reader:
            weight_record = read_weight_log_line(line)
            weight_records.append(weight_record)
        with scoped_session() as session:
            session.add_all(weight_records)


def read_weight_log_line(line_map):
    date = datetime.strptime(line_map['Date'], '%m/%d/%Y')
    weight = float(line_map['Weight'])
    weigh_in = WeighIn(
        date=date,
        weight_lbs=weight,
    )
    return weigh_in
 

def read_food_log(filepath):
    with open(filepath) as csv_file:
        food_reader = csv.DictReader(csv_file, delimiter=',', quotechar='"')
        food_records = []
        for line in food_reader:
            food_record = read_food_log_line(line)
            food_records.append(food_record)
        with scoped_session() as session:
            session.add_all(food_records)


def set_not_applicable_to_none(value):
    if value == "n/a":
        return None
    else:
        return value


def read_food_log_line(line_map):
    line_map = dict(zip(line_map, map(set_not_applicable_to_none, line_map.values())))
    calories = line_map['Calories']
    try:
        calories = int(calories)
    except ValueError:
        calories = ('').join(calories.strip().split(','))
        calories = int(calories)
    food = LoseitFood(
        raw_date=datetime.strptime(line_map['Date'], '%m/%d/%Y').date(),
        raw_name=line_map['Name'],
        raw_type=line_map['Type'],
        raw_quantity=float(line_map['Quantity']),
        raw_units=line_map['Units'],
        raw_calories=calories,
        raw_fat_g=line_map['Fat (g)'],
        raw_protein_g=line_map['Protein (g)'],
        raw_carbohydrates_g=line_map['Carbohydrates (g)'],
        raw_saturated_fat_g=line_map['Saturated Fat (g)'],
        raw_sugars_g=line_map['Sugars (g)'],
        raw_fiber_g=line_map['Fiber (g)'],
        raw_cholesterol_mg=line_map['Cholesterol (mg)'],
        raw_sodium_mg=line_map['Sodium (mg)'],
    )
    return food


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--filepath",
        help="Path to Loseit export csv file.",
        type=str,
    )
    parser.add_argument(
        "-t",
        "--filetype",
        help="Export type. 'food' for food log, 'weight' for weight log",
        type=str,
    )
    args = parser.parse_args()
    read_loseit_export(args.filepath, args.filetype)
