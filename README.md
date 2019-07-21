# inmem.py

This is an in-memory database written in python.
The goal of this project is as a playground to practice my python skills.

# Capabilities

1. It should be able to insert data
2. It should be able to delete data
3. It should be able to select data. Select all or only by primary key
4. It should be able to upsert data. Only by primary key

# Limitations

1. It doesn't have any persistence layer. Meaning when the program is killed, then data are gone
2. It doesn't have any data versioning. Meaning when data are deleted or updated, it doesn't keep the previous version so that the program can roll back
