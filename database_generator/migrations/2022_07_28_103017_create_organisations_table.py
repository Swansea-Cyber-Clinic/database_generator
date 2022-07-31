from orator.migrations import Migration


class CreateOrganisationsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('organisations') as table:
            table.increments('id')
            table.text('name').unique()
            table.text('description')
            table.text('address_1').nullable()
            table.text('address_2').nullable()
            table.text('city').nullable()
            table.text('postcode').nullable()
            table.text('email_office').nullable()
            table.text('tel_office').nullable()
            table.text('email_help').nullable()
            table.text('tel_help').nullable()
            table.text('web').nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('organisations')
