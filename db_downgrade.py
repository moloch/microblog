from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI as uri, SQLALCHEMY_MIGRATE_REPO as repo

v = api.db_version(uri, repo)
api.downgrade(uri, repo, v-1)
v = api.db_version(uri, repo)
print('Current database version: ' + str(v))
