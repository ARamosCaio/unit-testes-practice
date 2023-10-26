import pytest
# pytest will search for files with the tag "test"
# run "pytest . -v" to run all tests with more verbose messages

def test_our_first_test() -> None:
    # sourcery skip: equality-identity, remove-assert-true
    assert 1==1

#Skip a test that we don't want to erase
@pytest.mark.skip #Skip a test that we don't want to erase
def test_should_be_skipped() -> None:
    assert 1==2

#Skip a test if the condition passed is True
@pytest.mark.skipif(4 > 1, reason = "Skipped because 4 > 1")
def test_should_be_skipped_if() -> None:
    assert 1==1

#Xfail is for tests that we don't mind failing
@pytest.mark.xfail
def test_dont_care_if_fails() -> None:
    assert 1==1

# Run "pytest . -v -p no:warnings" to run the custom mark created without raising warnings

@pytest.mark.slow
def test_with_custom_mark1() -> None:
    pass

# Run "pytest . -v -p no:warnings -m slow" to run only the slow tests (tagged as slow)
# Or Run "pytest . -v -p no:warnings -m not slow" to run all tests that aren't slow

class Company:
    def __init__(self, name: str, stock_symbol: str):
        self.name = name
        self.stock_symbol = stock_symbol

    def __str__(self):
        return f"{self.name}: {self.stock_symbol}"

# A fixture is a function that might be called before and/or after running test functions
@pytest.fixture 
def company() -> Company:
    return Company(name="Fiver", stock_symbol="FVRR") 

def test_with_fixture(company: Company) -> None:
    print(f"Printing {company} from fixture")

# Run "pytest . -v -p no:warnings -s" to show what we printed

# Parametrized tests are used to run the tests multiple times with different parameters
@pytest.mark.parametrize(
    "company_name",
    ["Tik Tok", "Facebook", "Instagram"],
    ids = ["TIK TOK TEST", "FACEBOOK TEST", "INSTAGRAM TEST"],
)

def test_parametrized(company_name: str) -> None:
    print(f"\nTest with {company_name}")

# Test that asserts if its raising an exception
def raise_covid19_exception() -> None:
    raise ValueError("CoronaVirus Exception")

def test_raise_covid19_exception_should_pass() -> None:
    with pytest.raises(ValueError) as e:
        raise_covid19_exception()
    assert "CoronaVirus Exception" == str(e.value)