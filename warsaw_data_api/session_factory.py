from .ztm import ZtmSession


class SessionFactory:
    def client(self, service_name: str = None, apikey: str = None):
        if service_name == "ztm":
            return ZtmSession(apikey=apikey)
        elif service_name == "city":
            raise NotImplementedError()
        else:
            raise AttributeError(f"Wrong service_name: {service_name}")
