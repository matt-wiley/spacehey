
Open Library API call to get book data by ISBN number.

```sh
curl 'https://openlibrary.org/api/books?jscmd=data&bibkeys=ISBN:9780399563874&format=json' | jq
```