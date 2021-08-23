from serifan import api, session


def test_api():
    sb = None
    try:
        sb = api()
    except Exception as exc:
        print("serifan.api() raised {} unexpectedly!".format(exc))

    assert sb.__class__.__name__ == session.Session.__name__
