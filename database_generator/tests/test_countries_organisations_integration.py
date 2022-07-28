import unittest
from factory import factory
from models.country import Country
from models.organisation import Organisation
from config import db

class CountriesOrganisationsIntegrationTest(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    db.delete('delete from countries')
    db.delete('delete from organisations')

  def setUp(self):
    self.country = factory(Country).make()
    self.country.save()
    self.organisation = factory(Organisation).make()
    self.organisation.save()
    self.other_country = factory(Country).make()
    self.other_country.save()
  
  def tearDown(self):
    db.delete('delete from countries')
    db.delete('delete from organisations')

  def testAssociateCountryWithOrganisation(self):
    self.assertTrue(self.organisation.countries().save(self.country), True)
    self.assertEqual(self.organisation.countries().count(), 1)

  def testOrganisationCanHaveMoreThanOneAssociatedCountry(self):
    self.assertTrue(self.organisation.countries().save(self.country), True)
    self.assertTrue(self.organisation.countries().save(self.other_country), True)
    self.assertEqual(self.organisation.countries().count(), 2)

if __name__ == '__main__':
  unittest.main()