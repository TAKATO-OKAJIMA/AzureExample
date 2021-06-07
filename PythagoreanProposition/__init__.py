import math
import json
import logging

import azure.functions as func

SIDE_A = 'a'
SIDE_B = 'b'
SIDE_C = 'c'

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    side_a = int(req.params.get(SIDE_A))
    side_b = int(req.params.get(SIDE_B))

    if not (side_a and side_b):
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            side_a = req_body.get(SIDE_A)
            side_b = req_body.get(SIDE_B)

    if side_a and side_b:
        side_c = math.sqrt(side_a * side_a + side_b * side_b)
        response = {SIDE_A:side_a, SIDE_B:side_b, SIDE_C:side_c}
        return func.HttpResponse(json.dumps(response))

    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
