# DevOps Portfolio App

A simple FastAPI application deployed on Google Kubernetes Engine (GKE).

## Features
- FastAPI backend
- Dockerized application
- Kubernetes deployment
- Health check endpoint

## Endpoints
- `/` - Main endpoint
- `/health` - Health check

## Run locally

```bash
docker build -t app .
docker run -p 8000:8000 app
