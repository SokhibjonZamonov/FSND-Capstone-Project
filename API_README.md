
# API Endpoints

   

    GET /
    

 - Renders to a welcome page template
 - No authorization is required

## Actors 

    GET /actors
 - Gets a list of data in actors table
 - Authorization is required
{ 
	  "actors": [
	  {
						    "id": 1,
						    "age": 55,
						    "first_name": "Robert",
						    "last_name": "Downey",
						    "gender": "Male"
						    },
							{
						    "id": 2,
						    "age": 45,
						    "first_name": "Leonardo",
						    "last_name": "DiCaprio",
						    "gender": "Male"
						    }
				]
}

 ```
GET /actors/<ind:id>
```

 - Returns a json object of an individual actor with a specified id
 - Authorization is required
 
 ```
DELETE /actors/<ind:id>
```

 - Deletes an actor with a specified id from the database
 - Authorization is required
 
 ```
PATCH /actors/<ind:id>
```

 - Updates actor information with a given id
 - Authorization is required
 
```
POST /actors
```

 - Adds a new actor to the database
 - Authorization is required
 
 ## Movies 

    GET /movies
 - Gets a list of  data in movies table
 - Authorization is required

{

"movies": [

{
"id": 1,
"title": "Casablanca",
"director": "Michael Curtiz",
"release_date": "Thu, 26 Nov 1942 00:00:00 GMT"
},
{
"id": 2,
"title": "The Dark Knight",
"director": "Christopher Nolan",
"release_date": "Mon, 14 Jul 2008 00:00:00 GMT"

}

 ```
GET /movies/<ind:id>
```

 - Returns a json object of an individual movie with a specified id
 - Authorization is required
 
 ```
DELETE /movies/<ind:id>
```

 - Deletes a movie with a specified id from the database
 - Authorization is required
 
 ```
PATCH /movies/<ind:id>
```

 - Updates movie information with a given id
 - Authorization is required
 
```
POST /movies
```

 - Adds a new movie to the database
 - Authorization is required