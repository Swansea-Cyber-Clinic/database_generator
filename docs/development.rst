Development
===========

Orator
------

*database_generator* uses `Orator <https://orator-orm.com/>`_ as its :abbr:`ORM (Object-Relational Mapper)`. If you'd like to add functionality to *database_generator*, you'll need to do so through Orator. Validation of fields for models is handled through `orator-validator <https://pypi.org/project/orator-validator/>`_ and the observer functionality in Orator.

Adding a new model
^^^^^^^^^^^^^^^^^^

Use the Orator CLI tool to generate a model and associated migration (make sure you run it from the nested `database_generator` folder).

.. code-block:: console

  $ orator make:model MyModel -m

Add the fields you wish to generate to the generated migration file, changes made to the file are annotated below.

.. code-block:: python

  from orator.migrations import Migration


  class CreateMyClassTable(Migration):

      def up(self):
          """
          Run the migrations.
          """
          with self.schema.create('my_class') as table:
              table.increments('id')
              table.text('name').unique() # added
              table.text('description') # added
              table.timestamps()

      def down(self):
          """
          Revert the migrations.
          """
          self.schema.drop('my_class')


In the generated model file, define what fields you'd like to be added when using the `create()` or `new()` methods by adding them to either `__fillable__` or `__guarded__` — you'll probably want to guard `timestamps` and `id`, and allow all other fields to be fillable (below we have allowed any field to be fillable by setting `__guarded__` to an empty array).

For validation, import `orator_validator` and create a class for managing validation. You'll register this class by calling the `observe()` method on the model class (which is inherited from the generic `Model` class). You can add validation to any stage of the lifecycle of Orator models, in general it's probably easiest to define a `saving` method. The `orator-validator <https://pypi.org/project/orator-validator/>`_ documentation provides information on available lifecycle stages. In this case, as we have registered the `MyModelValidation` class by observing it, the code contained in the `saving` method will be run when a save operation is run (i.e. the `create` or `save` methods on `MyModel`).

.. code-block:: python

  from orator import Model
  from orator_validator import Validator

  class MyModel(Model, Validator):
    __guarded__ = []

  class MyModelValidation(object):
    def saving(self, my_model):
      my_model.validate('name', require=True, data_type=str)
      my_model.validate('description', require=True, data_type=str)
      my_model.errors()

  MyModel.observe(MyModelValidation())

Testing
-------

Testing is handled using Python's inbuilt `unittest` framework. Tests can be created in the `tests` directory. To run all tests, run the following (ensuring you are in the nested `database_generator` directory):

.. code-block:: console

  $ python -m unittest discover tests

Documentation
-------------

The documentation you are currently reading is created using `Sphinx <https://www.sphinx-doc.org/en/master/>`_. To generate documentation locally, run:

.. code-block:: console

  $ sphinx-build docs docs/_build/html

You can also autobuild documentation using `sphinx-autobuild <https://pypi.org/project/sphinx-autobuild/>`_ (for example, if you are making changes).

.. code-block:: 

  $ sphinx-autobuild docs docs/_build/html