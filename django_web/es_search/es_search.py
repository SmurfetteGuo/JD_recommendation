# coding=utf-8

# How to start es server?
# 1.download and unzip elasticsearch-6.0.0.zip
# 2.`cd [elasticsearch local path]/bin`
# 3.`./elasticsearch-plugin install https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v6.0.0/elasticsearch-analysis-ik-6.0.0.zip`
# 4. `./elasticsearch`  #run es server
# 5. execute `create_index(jd_index)` and `fil_in_data()` to stuff data (only execute one time)
# 6. call `search()` to search

import pymysql

from elasticsearch import Elasticsearch

# index non.
jd_index = "jd_index"

# mysql connection
db_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'JDProducts',
    'charset':'utf8'
}

es = Elasticsearch()

index_mappings = {
    "mappings": {
        "record": {
            "properties": {
                "title": {
                    "type": "text",
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_max_word"
                },
                "img_url": {
                    "type": "text",
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_max_word"
                },
                "id": {
                    "type": "integer"
                }
            }
        },
    }
}


def delete_index(index):
    es.indices.delete(index=index)


def create_index(index):
    index = jd_index
    if es.indices.exists(index=index) is not True:
        print("create jd_index")
        es.indices.create(index=index, body=index_mappings)
    else:
        print("jd_index exists")


def get_record():
    connection = pymysql.connect(**db_config)
    with connection.cursor() as cursor:
        sql = "select title, img_url, id from django_web_productmessage"
        cursor.execute(sql)
        connection.commit()

    for row in cursor:
        # print(row)
        yield row

    connection.close()


def fil_in_data():
    for i, record in enumerate(get_record()):
        doc = {
            "id": record[2],
            "title": record[0],
            "img_url": record[1],
        }

        es.index(index=jd_index, doc_type="record", id=record[2], body=doc)
        # print(res)
        if i % 1000 == 0:
            print(i)


def search(query):
    print("searching:  {s}".format(s=query))
    query_contains = {
        'query': {
            'multi_match': {
                'query': query,
                "fields": ["title"]
            }
        },
        "highlight": {
            "fields": {
                "title": {}
            }
        }
    }
    es = Elasticsearch()
    searched = es.search(jd_index, doc_type="record", body=query_contains, size=10)

    return searched


if __name__ == '__main__':
    # delete_index('jd_index')

    # The following two lines of code are used to import the ES data, only execute one time.
    create_index(jd_index)
    fil_in_data()
