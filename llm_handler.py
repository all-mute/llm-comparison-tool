import requests
import os
import json

LLM_DOCKER_ADDRESS = os.environ.get("LLM_DOCKER_ADDRESS")


def get_translation(modelname, mode, promt):
    if mode:
        postfix = '/generate_text_big'
        data = json.dumps(
            {
                'mode': mode,
                'promt': promt,
            }
        )
    else:
        postfix = '/generate_text_mini'
        data = json.dumps(
            {
                'model_name': modelname,
                'promt': promt,
            }
        )

    address = LLM_DOCKER_ADDRESS + postfix

    response = requests.post(
        address,
        json=data,
    )

    data = response.json()

    return data


