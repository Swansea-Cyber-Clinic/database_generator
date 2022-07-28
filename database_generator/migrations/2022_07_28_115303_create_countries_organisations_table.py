from orator.migrations import Migration


class CreateCountriesOrganisationsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('countries_organisations') as table:
            table.increments('id')
            table.integer('country_id')
            table.integer('organisation_id')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('countries_organisations')
