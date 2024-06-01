from ..runner import run_code_in_docker


def test_generic_code():
    result = run_code_in_docker("print('hello world!')")

    assert result.status == "success"
    assert result.stdout == "hello world!\n"
    assert result.stderr == ""


def test_change_files():
    code = """
with open("example.txt", "w") as file:
    file.write('Hello, this is a sample text written to the file.')
    """
    result = run_code_in_docker(code)
    assert result.status == "error"
    assert result.stderr is not None and "Read-only file system" in result.stderr


def test_network():
    code = (
        "import urllib.request\nurllib.request.urlretrieve('https://www.google.com/')"
    )
    result = run_code_in_docker(code)
    assert result.status == "error"
    assert (
        result.stderr is not None
        and "socket.gaierror: [Errno -3] Temporary failure in name resolution"
        in result.stderr
    )
