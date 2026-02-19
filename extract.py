"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neos = []
    with open(neo_csv_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            neos.append(NearEarthObject(
                designation=row['pdes'],
                name=row['name'] or None,
                diameter=row['diameter'] if row['diameter'].strip() else float('nan'),
                hazardous=row['pha'],
            ))
    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    approaches = []
    with open(cad_json_path) as f:
        contents = json.load(f)
    fields = contents['fields']
    des_idx = fields.index('des')
    cd_idx = fields.index('cd')
    dist_idx = fields.index('dist')
    v_rel_idx = fields.index('v_rel')
    for record in contents['data']:
        approaches.append(CloseApproach(
            designation=record[des_idx],
            time=record[cd_idx],
            distance=float(record[dist_idx]),
            velocity=float(record[v_rel_idx]),
        ))
    return approaches