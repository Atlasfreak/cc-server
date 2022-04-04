from pydantic import BaseSettings


class ServerConfig(BaseSettings):
    host: str = '0.0.0.0'
    port: int = 5000
    remote_config_url: str = 'https://placede.github.io/pixel/pixel.json'
    canvas_update_interval: int = 10


def get_graphql_config():
    return {
        "id": "1",
        "type": "start",
        "payload": {
            "variables": {
                "input": {
                    "channel": {
                        "teamOwner": "AFD2022",
                        "category": "CONFIG",
                    }
                }
            },
            "extensions": {},
            "operationName": "configuration",
            "query": "subscription configuration($input: SubscribeInput!) {\n  subscribe(input: $input) {\n    id\n    ... on BasicMessage {\n      data {\n        __typename\n        ... on ConfigurationMessageData {\n          colorPalette {\n            colors {\n              hex\n              index\n              __typename\n            }\n            __typename\n          }\n          canvasConfigurations {\n            index\n            dx\n            dy\n            __typename\n          }\n          canvasWidth\n          canvasHeight\n          __typename\n        }\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
        },
    }