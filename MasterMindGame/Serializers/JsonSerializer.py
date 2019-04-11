import json


class JsonSerializer(object):

    @classmethod
    def SerializeObject(self, player_stat):
        s = json.dumps(player_stat.__dict__)
        return s

    @classmethod
    def DeserializeJson(self, json_string, object_to_serialize):
        object_to_serialize.__dict__ = json.loads(json_string)
        return object_to_serialize