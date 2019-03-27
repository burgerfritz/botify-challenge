# Botify Challenge

Python/API Challenge

### Installing

Install requirements using pip...
```
pip install -r project/requirements.txt
```

Apply migrations to the database
```
python manage.py migrate
```

And run the server
```
python manage.py runserver localhost:8000
```

You can now access the API through the browser, by going to the URL `localhost:8000/towns/`

## Overview
Supports GET calls to list endpoints. 

In order to retrieve the number of towns for a given department code, call the URL below:
`localhost:8000/aggs.agg/?aggregate[count_towns]=dept&aggregate[dept_code]=1`

## Running the tests

In order to run the automated tests locally, run the command:
``` 
python manage.py test
```


## Documentation

Access the API documentation at `localhost:8000/docs/`
