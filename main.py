import Token

Token.load_env()
obtain_token = Token.get_token()
header_token = Token.get_auth_header(obtain_token)
