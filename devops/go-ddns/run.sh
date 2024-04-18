docker rm update-ddns;
docker run --name update-ddns -d -p 8000:8000/tcp -v "$(pwd)"/data:/updater/data qmcgaw/ddns-updater
