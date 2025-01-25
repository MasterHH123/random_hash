import hello

def test_random_hash():
    result = hello.random_hash()
    if result:
        assert result[0] == '0' and result[1] == '0', "Hash does not start with 00."
    else:
        assert result is None, "No hash should be returned if none match."
