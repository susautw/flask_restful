import mongoengine as mg
from bson import json_util, ObjectId


class Model(mg.Document):
    meta = {
        'abstract': True,
    }

    def to_json(self, *args, **kwargs):
        use_db_field = kwargs.pop("use_db_field", True)
        result = self.to_mongo(use_db_field)
        for key, value in result.items():
            if isinstance(value, ObjectId):
                result[key] = str(value)
        result['id'] = result['_id']
        del result['_id']
        return json_util.dumps(result, *args, **kwargs)
