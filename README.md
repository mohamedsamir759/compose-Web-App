
# Production-Ready FastAPI App with Docker
## Features
- FastAPI application     
- PostgreSQL database     
- Redis caching          
- Dockerized with Compose
- Nginx reverse proxy
- trivy-compatible for security scanning
  
📌 Architecture Overview
[client] --> [Nginx] --> [FastAPI App] --> [Redis]
                |   ---> [PostgreSQL]
_ use trivy for scanning my image


