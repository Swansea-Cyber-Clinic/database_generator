from orator import DatabaseManager, Model

DATABASES = {
  'default': 'production',
  'production': {
    'driver': 'sqlite',
    'database': './mapping.db'
  },
  'testing': {
    'driver': 'sqlite',
    'database': './testing.db'
  }
}

db = DatabaseManager(DATABASES)
Model.set_connection_resolver(db)