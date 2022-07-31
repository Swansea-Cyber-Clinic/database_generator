from orator.orm import Model
from orator.exceptions.orm import ModelNotFound
from abc import ABC, abstractmethod
import json
from models.country import Country
from models.category import Category
from models.police_force import PoliceForce
from models.organisation import Organisation
from config import db
from orator_validator import ValidatorError
import logging
import pandas as pd

class JsonDeserialiser(ABC):
  def __init__(self, model: Model, json_file_path: str):
    self.model = model
    with open(json_file_path) as f:
      self.dictionary = json.load(f)

  @abstractmethod
  def init(self):
    pass

  @abstractmethod
  def _deserialise(self):
    pass

  def _exception_handler(self, exception: Exception, record: str):
    if isinstance(exception, ValidatorError):
      logging.info(f"Problem processing {record}, error: {exception.body}")
      logging.warning("Data is malformed, read previous traceback, do not use output until you no longer see this error")
      pass
    pass

class CountryDeserialiser(JsonDeserialiser):
  def __init__(self):
    super().__init__(Country, "./data/country.json")

  def _deserialise(self):
    for item in self.dictionary:
      try:
        Country.create(name=item)
        logging.debug(f"Country with name={item} created")
      except ValidatorError as ve:
        super()._exception_handler(ve, f"country with name={item}")
        pass
  
  def init(self):
    db.delete('delete from countries')
    self._deserialise()

class CategoryDeserialiser(JsonDeserialiser):
  def __init__(self):
    super().__init__(Category, "./data/category.json")

  def _deserialise(self):
    for item in self.dictionary:
      try:
        Category.create(name=item['name'], description=item['description'])
        logging.debug(f"Category with name={item['name']}, description={item['description']} created")
      except ValidatorError as ve:
        super()._exception_handler(ve, f"category with name={item['name']}, description={item['description']}")
        pass

  def init(self):
    db.delete('delete from categories')
    self._deserialise()

class PoliceForceDeserialiser(JsonDeserialiser):
  def __init__(self):
    super().__init__(PoliceForce, "./data/police_force.json")

  def _deserialise(self):
    for item in self.dictionary:
      try:
          PoliceForce.create(name=item['name'], description=item['description'])
          logging.debug(f"Police Force with name={item['name']}, description={item['description']} created")
      except ValidatorError as ve:
        super()._exception_handler(ve, f"police force with name={item['name']}, description={item['description']}")
        pass

  def init(self):
    db.delete('delete from police_forces')
    self._deserialise()

class CsvDeserialiser(ABC):
  def __init__(self, model: Model, csv_file_path: str):
    self.model = model
    self.dataframe = pd.read_csv(csv_file_path, sep=',')

  @abstractmethod
  def _deserialise():
    pass

  @abstractmethod
  def init(self):
    pass

  def _exception_handler(self, exception: Exception, record: str):
    if isinstance(exception, ValidatorError):
      logging.info(f"Problem processing {record}, error: {exception.body}")
      pass
    elif isinstance(exception, ModelNotFound):
      logging.info(f"Invalid data ({record})")
      pass
    pass

class OrganisationDeserialiser(CsvDeserialiser):
  def __init__(self, csv_file_path: str):
    super().__init__(Organisation, csv_file_path)
    self.mapping = {
      'name': 'Organisation',
      'description': 'Description',
      'address_1': 'Address_1',
      'address_2': 'Address_2',
      'city': 'City',
      'postcode': 'Postcode',
      'email_office': 'Email_office',
      'email_help': 'Email_help',
      'tel_office': 'Tel_office',
      'tel_help': 'Tel_help',
      'web': 'Web'
    }
      
  def _get_key(self, val: str, dict: dict):
    for k, v in dict.items():
      if val == v:
        return k

  def _generate_category_mapping(self, organisation: Organisation, categories: str):
    if isinstance(categories, str):
      cat_array = categories.split(', ')
      for c in cat_array:
        try:
          cat = Category.where('name', '=', c).first_or_fail()
          organisation.categories().save(cat)
        except ModelNotFound as mnfe:
          super()._exception_handler(mnfe, f"specified category='{c}' for organisation={organisation.name}")
          pass

  def _generate_country_mapping(self, organisation: Organisation, countries: str):
    if isinstance(countries, str):
      cty_array = countries.split(', ')
      for c in cty_array:
        try:
          cty = Country.where('name', '=', c).first_or_fail()
          organisation.countries().save(cty)
        except ModelNotFound as mnfe:
          super()._exception_handler(mnfe, f"specified country='{c}' for organisation={organisation.name}")
          pass

  def _generate_police_force_mapping(self, organisation: Organisation, police_forces: str):
    if isinstance(police_forces, str):
      pfo_array = police_forces.split(', ')
      for p in pfo_array:
        try:
          pfo = PoliceForce.where('name', '=', p).first_or_fail()
          organisation.police_forces().save(pfo)
        except ModelNotFound as mnfe:
          super()._exception_handler(mnfe, f"specified police force='{p}' for organisation={organisation.name}")
          pass

  def _deserialise(self):
    for _, r in self.dataframe.iterrows():
      try:
        kwarg_dict = {}
        for val in self.mapping.values():
          # Validation checking for non-mandatory fields (not possible to add a validator)
          if r[val] != "" and isinstance(r[val], str):
            kwarg_name = self._get_key(val, self.mapping)
            kwarg_dict[kwarg_name] = r[val]
          else:
            logging.debug(f"Organisation with name={r['Organisation']} has a malformed or empty field ({val})")
        org = Organisation.create(kwarg_dict)
        self._generate_category_mapping(org, r['Service_cat'])
        self._generate_country_mapping(org, r['Coverage'])
        self._generate_police_force_mapping(org, r['Forces'])
        logging.debug(f"Organisation with name={r['Organisation']}, description={r['Description']} created")
      except ValidatorError as ve:
        super()._exception_handler(ve, f"organisation with name={r['Organisation']}, description={r['Description']}")
        pass

  def init(self):
    db.delete('delete from organisations')
    self._deserialise()