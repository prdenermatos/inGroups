# from requests import request
from flask import render_template, request
from src import app
from src.repository.elasticsearch_repository import ElasticsearchRepository


elasticsearchRepository = ElasticsearchRepository()

@app.route('/' , methods = ['GET','POST'])
def home():
    render_table = False
    estabelecimentos_list = []
    if request.method == 'POST':
        filter = {"termo": "cnpj_full", "value":""}
        filter_name_cnpj = request.form["search_by_name_or_cnpj"]
        try:
            filter_name_cnpj = int(filter_name_cnpj)
            if len(filter_name_cnpj) == 14:
                filter = {"termo": "cnpj_full", "value": filter_name_cnpj}
        except:
            filter = {"termo": "nome_fantasia", "value": filter_name_cnpj}


        render_table = True
        estabelecimentos_list = elasticsearchRepository.find_all(index="estabelecimentos", filter=filter)

    return render_template("index.html", estabelecimentos_list=estabelecimentos_list,
        render_table=render_table
    )

@app.route('/old')
def old():
    return render_template("index-old.html")