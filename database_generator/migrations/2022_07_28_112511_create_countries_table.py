from orator.migrations import Migration


class CreateCountriesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('countries') as table:
            table.increments('id')
            table.text('name').unique()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('countries')
