
from pathlib import Path

def test_file(ms):

    paths = Path(f'./{ms}').glob('*')
    return list(map(str, paths))
