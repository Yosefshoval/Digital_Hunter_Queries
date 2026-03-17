# Digital_Hunter_Queries


Digital_Hunter_Queries is a Python service that allow you to query the MySQL database of inteligens signals.


First, you need the Docker Desktop installed on your computer.

If you still don`t have Docker Desktop, you can install it from [here](https://docs.docker.com/desktop/setup/install/windows-install/).

## Usage

Go to the root path of this project ``` /Digital_Hunter_Queries/```

Run the fallowing command:

```
docker compose -f docker compose -f docker-compose.db.yml up -d
```

## interface
Go to ```http://localhost:8085/docs``` in your browser (or another swagger that you prefer).

