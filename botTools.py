import base64


def read_file(filename, encrypt=False):
    if encrypt:
        with open(filename, 'rb') as f:
            return base64.b64decode(f.read()).decode('utf-8')
    else:
        with open(filename, 'r') as f:
            return f.read()


def write_file(content, filename, encrypt=False):
    if encrypt:
        with open(filename, 'wb') as f:
            f.write(base64.b64encode(content.encode('utf-8')))
        return True
    else:
        with open(filename, 'w') as f:
            f.write(content)
        return True


def query_token(token_id=None):
    return read_file(f'token_{token_id}', True)
