import logging
import argparse
from pathlib import Path
import sys
from serialisation.deserialisers import CountryDeserialiser, CategoryDeserialiser, PoliceForceDeserialiser, OrganisationDeserialiser

parser = argparse.ArgumentParser()
parser.add_argument(
  '-v', '--verbose',
  help="Provides verbose output",
  action="store_const", dest="loglevel", const=logging.DEBUG,
  default=logging.INFO
)

parser.add_argument(
  '-i', '--input',
  metavar='/path/to/file',
  help="The path to the input CSV file",
  type=Path,
  required=True
)

args = parser.parse_args()

logging.basicConfig(level=args.loglevel, format='%(levelname)s: %(message)s')

csv_file = args.input
if not csv_file.is_file():
  logging.critical("Specified CSV file does not exist, quitting now.")
  sys.exit()

for ds in (CountryDeserialiser, CategoryDeserialiser, PoliceForceDeserialiser):
  d = ds()
  d.init()

od = OrganisationDeserialiser('./data/service_database_v1.csv')
od.init()