import datetime

from serifan import comics_list


def test_comics_list(comic_list_response):
    res = comics_list.ComicsList(comic_list_response)
    assert len(res) == 2
    assert res[0].publisher == "IMAGE COMICS"
    assert res[1].title == "BITTER ROOT #15 CVR B CONLEY CURIEL (MR)"
    assert res[1].price == "$3.99"
    assert res[1].release_date == datetime.date(2021, 8, 11)
    assert res[1].diamond_id == "MAY210140"
