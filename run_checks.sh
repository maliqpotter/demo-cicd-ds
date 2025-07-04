#!/bin/bash

# Script untuk menjalankan CI/CD checks secara lokal
# Run this script untuk memastikan code siap untuk push

echo "🚀 Starting local CI/CD checks..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print status
print_status() {
    if [ $1 -eq 0 ]; then
        echo -e "${GREEN}✅ $2 passed${NC}"
    else
        echo -e "${RED}❌ $2 failed${NC}"
        exit 1
    fi
}

# Install dependencies
echo -e "${YELLOW}📦 Installing dependencies...${NC}"
pip install -r requirements.txt
print_status $? "Dependencies installation"

# Run linting
echo -e "${YELLOW}🔍 Running flake8 linting...${NC}"
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
print_status $? "Critical linting checks"

flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
echo -e "${GREEN}📊 Linting report generated${NC}"

# Check formatting
echo -e "${YELLOW}🎨 Checking code formatting with black...${NC}"
black --check --diff .
print_status $? "Code formatting check"

# Run tests
echo -e "${YELLOW}🧪 Running unit tests...${NC}"
pytest test_app.py -v --cov=app --cov-report=term --cov-report=html
print_status $? "Unit tests"

# Build Docker image (optional)
echo -e "${YELLOW}🐳 Building Docker image...${NC}"
docker build -t demo-cicd-python:latest . > /dev/null 2>&1
print_status $? "Docker build"

echo -e "${GREEN}🎉 All checks passed! Ready to push.${NC}"
echo -e "${YELLOW}📊 Coverage report available in htmlcov/index.html${NC}"
