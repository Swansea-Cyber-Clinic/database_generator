from orator.migrations import Migration


class CreateOrganisationsPoliceForcesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('organisations_police_forces') as table:
            table.increments('id')
            table.integer('police_force_id')
            table.integer('organisation_id')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('organisations_police_forces')
