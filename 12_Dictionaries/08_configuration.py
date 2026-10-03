# Configuration settings

config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "mydb",
        "user": "admin",
        "password": "secret"
    },
    "server": {
        "host": "0.0.0.0",
        "port": 8000,
        "debug": True
    },
    "features": {
        "logging": True,
        "cache": False,
        "api_rate_limit": 1000
    }
}

db_host = config["database"]["host"]
server_port = config["server"]["port"]

print(f"Database: {db_host}, Server Port: {server_port}")

config["server"]["debug"] = False
config["features"]["cache"] = True

print(config)
