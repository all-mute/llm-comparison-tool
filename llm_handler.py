import requests
import os
import json

LLM_DOCKER_ADDRESS = "http://studcamp.merkulov.ai"


def get_translation(model_name, promt):
    data_in = {}

    if "nllb-200" in model_name:
        data_in["mode"] = model_name.split('-')[-1]
    else:
        data_in["model_name"] = model_name

    if "nllb-200" in model_name:
        postfix = '/generate_text_big'
        data = json.dumps(
            {
                'mode': data_in['mode'],
                'prompt': promt,
            }
        )
    else:
        postfix = '/generate_text_mini'
        data = json.dumps(
            {
                'model_name': data_in['model_name'],
                'prompt': promt,
            }
        )

    address = LLM_DOCKER_ADDRESS + postfix

    response = requests.post(
        address,
        data=data,
    )

    print(response)
    print(response.text)

    data = response.json()

    return data


