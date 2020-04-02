import json


def dumpData(file_name, data):
    """
    to write the data into a json file, data is a string as an input
    abd gets wriiten into the file as a dictionary python object.
    """
    try:
        file = open(file_name, 'w')
        # convert to a dictionary then write it into the file.
        json.dump(data, file)
        file.close()

    except Exception as e:
        raise e


def loadData(file_name):
    """
    to load the data a json file, the returned object is as a dictionary,
    object, the mode is only read.
    """
    try:
        file = open(file_name, "r")
        data = json.load(file)
        file.close()

        return data

    except Exception as e:
        raise e
