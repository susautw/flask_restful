def hold(method):
    value = {}
    initialized = set()
    method_id = id(method)

    def inner(self, *args, **kwargs):
        # TODO id will repeat, instead inject a dict to self
        _self = id(self)
        method_for_instance = (_self, method_id)
        print(method_for_instance, method_for_instance in initialized)
        if method_for_instance in initialized:
            return value[method_for_instance]

        value[method_for_instance] = method(self, *args, **kwargs)
        initialized.add(method_for_instance)
        return value[method_for_instance]

    return method  # TODO change it to inner if the issue above complete.
