import pytest

from modules.citation import Citation


@pytest.fixture
def no_charge_citation():
    return Citation()


@pytest.fixture
def charged_citation():
    return Citation(50)


def test_no_charge_citation_constructor(no_charge_citation):
    assert no_charge_citation.fine == 0
    assert no_charge_citation.balance == 0
    assert no_charge_citation.status == "no charge"


def test_charged_citation_constructor(charged_citation):
    assert charged_citation.fine == 50
    assert charged_citation.balance == 50
    assert charged_citation.status == "unpaid"


def test_charged_citation_partial_payment(charged_citation):
    charged_citation.pay(30)
    assert charged_citation.fine == 50
    assert charged_citation.balance == 20
    assert charged_citation.status == "partially paid"


def test_charged_citation_full_payment(charged_citation):
    charged_citation.pay(50)
    assert charged_citation.fine == 50
    assert charged_citation.balance == 0
    assert charged_citation.status == "paid"


def test_overpaying_citation(charged_citation):
    try:
        charged_citation.pay(60)
    except Exception, e:
        assert str(e) == "NO"
