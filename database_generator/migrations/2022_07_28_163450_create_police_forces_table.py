from orator.migrations import Migration


class CreatePoliceForcesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('police_forces') as table:
            table.increments('id')
            table.text('name').unique()
            table.text('description')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('police_forces')
