__version__ = "0.1.2"

from serifan import session


def api():
    """
    Entry function for access to the Shortboxed api.
    """
    return session.Session()
