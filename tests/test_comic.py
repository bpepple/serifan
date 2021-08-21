import datetime

from serifan import api, comics_list, session, utils


def test_comics_list(comic_list_response):
    res = comics_list.ComicsList(comic_list_response)
    comic_iter = iter(res)
    assert next(comic_iter).title == "BITTER ROOT #15 CVR A GREENE (MR)"
    assert next(comic_iter).title == "BITTER ROOT #15 CVR B CONLEY CURIEL (MR)"
    assert len(res) == 2
    assert res[0].publisher == "IMAGE COMICS"
    assert res[1].title == "BITTER ROOT #15 CVR B CONLEY CURIEL (MR)"
    assert res[1].price == "$3.99"
    assert res[1].release_date == datetime.date(2021, 8, 11)
    assert res[1].diamond_id == "MAY210140"


def test_available_dates(sb_cleaned_dates, mocker):
    mocker.patch.object(
        session.Session, "available_release_dates", return_value=sb_cleaned_dates
    )
    sb = api()
    result = sb.available_release_dates()
    assert len(result) == 4
    assert result[0] == datetime.date(2021, 8, 4)


def test_list_string_to_date(sb_dates_response):
    results = utils.list_strings_to_dates(sb_dates_response)
    assert len(results) == 5
    assert results[0] == datetime.date(2021, 7, 29)
