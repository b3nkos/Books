from profile import build_profile


def test_profile_creation():
    profile = build_profile("jose", "martinez", location="Colombia", field="Software")

    assert profile["first"] == "Jose"
    assert profile["last"] == "Martinez"
    assert profile["location"] == "Colombia"
    assert profile["field"] == "Software"
