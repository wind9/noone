from db.basic import metadata
from db.tables import *

if __name__ == '__main__':
    metadata.create_all()
