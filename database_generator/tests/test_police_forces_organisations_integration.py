import unittest
from factory import factory
from models.police_force import PoliceForce
from models.organisation import Organisation
from config import db

class PoliceForcesOrganisationsIntegrationTest(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    db.delete('delete from police_forces')
    db.delete('delete from organisations')

  def setUp(self):
    self.police_force = factory(PoliceForce).make()
    self.police_force.save()
    self.organisation = factory(Organisation).make()
    self.organisation.save()
    self.other_police_force = factory(PoliceForce).make()
    self.other_police_force.save()
  
  def tearDown(self):
    db.delete('delete from police_forces')
    db.delete('delete from organisations')

  def testAssociatePoliceForceWithOrganisation(self):
    self.assertTrue(self.organisation.police_forces().save(self.police_force), True)
    self.assertEqual(self.organisation.police_forces().count(), 1)

  def testOrganisationCanHaveMoreThanOneAssociatedPoliceForce(self):
    self.assertTrue(self.organisation.police_forces().save(self.police_force), True)
    self.assertTrue(self.organisation.police_forces().save(self.other_police_force), True)
    self.assertEqual(self.organisation.police_forces().count(), 2)

if __name__ == '__main__':
  unittest.main()