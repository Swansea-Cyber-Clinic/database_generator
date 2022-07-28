from orator.migrations import Migration


class CreateCategoriesOrganisationsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('categories_organisations') as table:
            table.increments('id')
            table.integer('category_id')
            table.integer('organisation_id')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('categories_organisations')
