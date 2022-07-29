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

.. code-block:: console

  $ python main.py -i path/to/file.csv -o /path/to/directory