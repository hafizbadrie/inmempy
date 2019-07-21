
class InmempyDb:
    tables = {}
    database = {}

    @classmethod
    def create_table(cls, table_name, schema, primary_key):
        if cls.table_exists(table_name):
            raise Exception("Table is already existed!")

        cls.tables[table_name] = {'schema': schema, 'primary_key': primary_key}
        cls.database[table_name] = []

    @classmethod
    def table_exists(cls, table_name):
        return table_name in cls.tables

    @classmethod
    def cleanup(cls):
        cls.tables = {}

    @classmethod
    def insert_to(cls, table_name, data):
        table_schema = cls.tables[table_name]['schema']
        primary_key = cls.tables[table_name]['primary_key']
        validated_data = cls.get_validated_data(table_schema, primary_key, data)
        cls.database[table_name].append(validated_data)

    @classmethod
    def get_validated_data(cls, table_schema, primary_key, data):
        validated_data = {}
        for key in table_schema.keys():
            validated_data[key] = data.get(key)

        if validated_data[primary_key] == None:
            raise Exception("Primary key is not provided in the data")

        return validated_data


    @classmethod
    def select_from(cls, table_name):
        return cls.database[table_name]

    @classmethod
    def select_one(cls, table_name, value):
        found = False
        data = cls.database[table_name]
        primary_key = cls.tables[table_name]['primary_key']
        rows = len(data)
        i = 0
        selected_data = None

        while not found and i<rows:
            if data[i][primary_key] == value:
                selected_data = data[i]
                found = True

            i += 1

        return selected_data
