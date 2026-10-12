from src.parser import parse_line


def test_parse_valid_line():
    line='192.168.1.10 - - [01/Oct/2026:00:00:42 +0000] "GET /login HTPP/1.1" 404 3127'
    entry=parse_line(line)
    assert entry is not None
    assert entry.ip == "192.168.1.10"
    assert entry.path== "/login"
    assert entry.status== 404
    assert entry.size ==3127
    
def test_parse_invalid_line_returns_none():
    assert parse_line("linie stricata") is None
    