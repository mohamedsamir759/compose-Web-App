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
- Run Docker compose
  docker compose up -d

- Use trivy for scanning my image from vulnerabilities
  trivy image image-name
![trivy-web-app image](https://github.com/user-attachments/assets/9840153f-06be-4c2f-a0df-0428764b9932)
