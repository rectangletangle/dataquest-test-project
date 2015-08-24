Dataquest test-project
=====

##Static Server
Regarding the static content, I separated out the files I could. It's
non-trivial (but possible) to separate out the HTML dynamically generated with
Jinja, requiring refactoring a significant portion of the front-end into a more
AJAX/RESTful oriented style.

The static content server image can be built with
`docker build -t rodeo-static .`. It can then be ran with
`docker run -p 8000:8000 rodeo-static`.

Having a separate static content server helps keep the application more
modular. Making it straightforward to replace this portion of the application
with something like S3.

##Dynamic Server
To build the rodeo docker image run `docker build -t rodeo .`. Then run the
container with `docker run -p 5000:5000 rodeo`. The dynamically generated half
of Rodeo should be visible at `http://localhost:5000`.
