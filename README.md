# Pond5 - Cláudia Correia

## Run Locally
To run this code locally clone the repository


Run in the terminal:
```bash
python app.py
```


Open browser -> http://localhost:8080

## Run with Docker

Run it using:
```bash
docker run -p 8080:8080 claudiacor/app.py
```


### When running, these APIs can be accessed with:

localhost:8080/ping -> ping Pond5 website

localhost:8080/system -> returns service version and system information

localhost:8080/mediainfo/<id> -> returns an image filename, size, dimensions and title


