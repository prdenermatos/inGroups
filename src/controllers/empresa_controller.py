from flask import make_response, jsonify, request
from elasticsearch7.exceptions import NotFoundError
from src import app
from src.repository import elasticsearch_repository
from src.repository.elasticsearch_repository import ElasticsearchRepository

ESTABELECIMENTOS_INDEX = "estabelecimentos"

elasticsearch_repository = ElasticsearchRepository()


@app.route("/empresas", methods=["POST"])
# @cross_origin()
def find_all():
    request_body = request.json

    filter = _create_filter(request_body)

    result = elasticsearch_repository.find_all(
        index=ESTABELECIMENTOS_INDEX, filter=filter)

    return make_response(result)


def _create_filter(request_body: dict) -> dict:
    filter = {
        "query": {
            "query_string": {
                "query": ""
            }
        }
    }
    if request_body['filter'].get('nome_fantasia_or_cnpj'):
        value = request_body['filter'].get('nome_fantasia_or_cnpj')

        try:
            value = int(value)
            if len(str(value)) == 14:
                filter['query']['query_string']["query"] = f"(cnpj_full:${value})"    
        except Exception as e:
            filter['query']['query_string']["query"] = f"(nome_fantasia:${value})"
    return filter


@app.route("/empresa/<id>", methods=["GET"])
def find_by_id(id: str):
    try:
        result = elasticsearch_repository.find_document_by_id(
            index=ESTABELECIMENTOS_INDEX, id=id)
        return make_response(jsonify(result))
    except NotFoundError as e:
        print(e)
        return make_response(jsonify({
            "bad_request": f"Não foram encontrados dados para o ID {id}"
        }))
