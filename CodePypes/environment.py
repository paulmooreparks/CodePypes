import os
import yaml
from pathlib import Path

endpoint = "api.codepipes.io"
auth_token = ""

home_directory = os.path.expanduser( '~' )
cp_state_file = ".codepipes_state.yaml"
cp_state_path_fmt = "{home}/{file}"
cp_state_path = cp_state_path_fmt.format(home=home_directory,file=cp_state_file)

config = yaml.safe_load(Path(cp_state_path).read_text())

# auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJkNGNmMGYxMS1mYzE0LTQ3YjktYjgzYy1lMzJhZWJiY2IyYmEiLCJlbWFpbCI6InBhdWwucGFya3NAY2xkY3ZyLmNvbSIsInByb3ZpZGVyVG9rZW4iOiJleUpoYkdjaU9pSkJNalUyUjBOTlMxY2lMQ0psYm1NaU9pSkJNVEk0UjBOTklpd2lhWFlpT2lJelowdFViVkZPY2pkcFZHSkRTWFF5SWl3aWRHRm5Jam9pYTFWUE9IQlZTMk5ETkVSV1JFWkpMVjkxYUVGVVp5SXNJbnBwY0NJNklrUkZSaUo5Lkw5WEVwa2dHNmR3OXlFZUp1S25YbGcuT25JY2RLS1JVWG44OXplcy5GRklWZTg3eFNqMk5ROGh2anJwYjNLME5ESDBqa0F5MUR2Tm1FbkhlSDRTNDkwMmk2Q2xyNmtxZGJpbG1jSG1DbEZnZnNISS1KYkRCVm1iNTRHbkFMbTdhTHRMRkVjUjF3R1IwUnphb0FMNmIzNUhiZUVGT0JCYjA5N2ZUVUNnNGx1NTB0MjJHLUFxMWFxUTIzRHgzRnFxS2pUeHJ3SWJoS09VOFM3SWtFdW4wY1pUV2pPV01rQ0hoTlR1c0hVN2NRUzlkOE1TcE5DZTZyZmFMVlpBc2ZFWkRrSjF3SXZhVlFuRy1TNTlKbTl4Qjh5MllwQmZ3RlVrdVN1VmhuZnRLU1lsM1d3LlNWeTVpVThmeXY2ZW9obEFSalpXN0EiLCJnY1Rva2VuIjoibHh6ekhjZGVXZmU1MGc5QkFFTld1ajYwRkxBaHpaZHctV25MUllxUjJiS09lSVJjM3VDcExqSlR2d2ZtQUYydWE0U0txOW9JUEV4VExBUG54VzRxbWc9PSIsImV4cCI6MTY2NTc4MzQzOCwiaWF0IjoxNjY1NzQwMjM4LCJpc3MiOiJnb29nbGUifQ.LCItRG3WksOZjq66-hb7-QjDKq5NNzPirXPnDnSQh2w"
endpoint_fmt = "https://{endpoint}"
endpoint_url = endpoint_fmt.format(endpoint=endpoint)
api_fmt = "{url}/{api}/{version}/{method}"

endpoint = config['connected_endpoint']
auth_token = config['auth_token']
version = "v0"

def api_url(api, method):
    return api_fmt.format(url=endpoint_url, version=version, api=api, method=method)


