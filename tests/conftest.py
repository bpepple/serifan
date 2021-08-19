import pytest


@pytest.fixture()
def comic_list_response():
    return {
        "comics": [
            {
                "publisher": "IMAGE COMICS",
                "description": '"LEGACY," Part Five-The third arc of the Eisner Award-winning BITTER ROOT comes to an epic conclusion that will decide the fate of humanity. For the Sangerye family, it means making another sacrifice while searching for hope during hopeless times.',
                "title": "BITTER ROOT #15 CVR A GREENE (MR)",
                "price": "$3.99",
                "creators": "(W) David Walker, Chuck Brown (A/CA) Sanford Greene",
                "release_date": "2021-08-11",
                "diamond_id": "MAY210139",
            },
            {
                "publisher": "IMAGE COMICS",
                "description": '"LEGACY," Part Five-The third arc of the Eisner Award-winning BITTER ROOT comes to an epic conclusion that will decide the fate of humanity. For the Sangerye family, it means making another sacrifice while searching for hope during hopeless times.',
                "title": "BITTER ROOT #15 CVR B CONLEY CURIEL (MR)",
                "price": "$3.99",
                "creators": "(W) David Walker, Chuck Brown (A) Sanford Greene (CA) Chase Conley, Charissa Curiel",
                "release_date": "2021-08-11",
                "diamond_id": "MAY210140",
            },
        ]
    }
