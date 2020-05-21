# JSON serialization
# __json_serializable__
import json


class Foo:
    def __json_serializable__(self):
        return {'a': 1, 'b': 2}


def main():
    foo = Foo()
    print(json.dumps(foo))


if __name__ == '__main__':
    main()
