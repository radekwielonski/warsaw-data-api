from .session_factory import SessionFactory


DEFAULT_SESSION = None


def setup_default_session(**kwargs):
    global DEFAULT_SESSION
    DEFAULT_SESSION = SessionFactory(**kwargs)


def _get_default_session():
    if DEFAULT_SESSION is None:
        setup_default_session()

    return DEFAULT_SESSION


def client(*args, **kwargs):
    return _get_default_session().client(*args, **kwargs)
