# JD Search

## Introduction
   `JD Search`is a product recommendation system. Apply Django for web program, Bootstrap for the front end, beautiful soup for parse the html, and this system includes two recommendation version:
1) calculate cosine similarity of word vectors. 2) elasticsearch.

### How to start the program?

- Clone this program to local path
- `python manage.py migrate` #apply the models.py to database
- Run the `/data/django_web_productmessage.sql` in local database
- `python manage.py runserver` # run server in default port 8000
- Access Link:[http://127.0.0.1:8000/index](http://127.0.0.1:8000/index)


### Program Structure

``` 
recommend_web
├── .gitignore
├── JD_Spider                --spider for joybuy.com
│   └── spider.py
├── README.md                --README.md
├── db.sqlite3
├── django_web               --a django app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py            --app's model
│   ├── selectModel          --first version (cosine similarity of word vectors)
│   │   ├── JD.csv
│   │   ├── select.py
│   │   ├── word2vec.py
│   │   └── wordTrain.py
│   ├── es_search            --second version (es search)
│   │   └── es_search.py
│   ├── tests.py
│   └── views.py             --data require function
├── manage.py                --entrance
├── recommend_web
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt         --require environment
├── static                   --static resource
│   ├── css
│   ├── img
│   └── js
└── templates                --html
    └── index.html
```

## points can be improved
- add keyword association in the input box. For example, when users type in "clothing", association can be "clothing men" or "clothing women".
- add hot search list.

## demo
demo：attachment