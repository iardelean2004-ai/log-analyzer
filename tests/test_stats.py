from src.stats import top_ips, error_rate
LINES = (
    '1.1.1.1 - - [01/Oct/2026:00:00:01 +0000] "GET / HTTP/1.1" 200 100\n'
    '1.1.1.1 - - [01/Oct/2026:00:00:02 +0000] "GET / HTTP/1.1" 404 100\n'
    '2.2.2.2 - - [01/Oct/2026:01:00:03 +0000] "GET / HTTP/1.1" 500 100\n'
    '1.1.1.1 - - [01/Oct/2026:01:00:04 +0000] "GET / HTTP/1.1" 200 100\n'
)

def make_log(tmp_path, content=LINES):
    f =tmp_path / "test.log"
    f.write_text(content)
    return str(f)


def test_top_ips(tmp_path):
    path= make_log(tmp_path)
    assert top_ips(path, 1)== [("1.1.1.1", 3)]
    
    
def test_error_rate_empty_file(tmp_path):
    path= make_log(tmp_path)
    assert error_rate(path) == 0.5
    