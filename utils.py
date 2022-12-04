def load_txt(path: str) -> Optional[list]:
    with open(path, 'r') as f:
        # strip for deleting "\n" if you want to preserve this use: lines = f.readlines()
        lines = [line.strip() for line in f]
    return lines