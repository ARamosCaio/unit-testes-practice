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