Usage
=====

Installation
------------

To use *database_generator*, you'll first need to download the project from GitHub.

.. code-block:: console
  
  $ cd working_directory
  $ git clone https://github.com/Swansea-Cyber-Clinic/database_generator.git

*database_generator* makes use of ``pipenv`` for dependency management. This of course assumes that you have a working ``pip`` installation (if you use ``conda``, see instructions below).

Instructions for ``pip``
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

  $ pip install pipenv
  $ pipenv shell

``pipenv`` will automatically install dependencies based on the ``Pipfile`` and ``Pipfile.lock``.

Instructions for ``conda`` (*et al.*)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You (probably) won't be able to install dependencies using ``pipenv``. You'll have to manually install dependencies. It's best if you create a *Python environment* for *database_generator*, but it's not mandatory. You'll need the following:

Essential packages
""""""""""""""""""

- ``orator``
- ``orator-validator``
- ``pandas``

Development packages
""""""""""""""""""""

- ``faker``
- ``sphinx``
- ``sphinx-autobuild``

Instructions
------------

*database_generator* is managed through ``main.py``, a lá:

.. code-block:: console

  $ python main.py

You can add the ``-h`` flag for help with flags.

Creating a SQLite database
^^^^^^^^^^^^^^^^^^^^^^^^^^

This has changed from the service mapping tool. *database_generator* makes use of `Orator ORM <https://orator-orm.com/>`_, and therefore requires an initial database migration.

.. code-block:: console

  $ cd database_generator
  $ orator --config=config.py migrate

.. note:: 
  If you'd like to start from scratch (i.e. get the database into the state it was after you ran the above for the first time), you can do this by running ``orator --config=config.py migrate:refresh``.

After migrating the database, the script is run in much the same way that the previous tool was run.

.. code-block:: console

  $ python database_generator/main.py -i path/to/file.csv

The output database file is found at ``database_generator/mapping.db``.