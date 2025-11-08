# Step 1: Use official Python image
FROM python:3.10-slim

# Step 2: Set working directory
WORKDIR /app

# Step 3: Install required system dependencies
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    pkg-config \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Step 4: Copy dependency file and install Python libs
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy project code
COPY . .

# Step 6: Expose Django port
EXPOSE 8000

# Step 7: Start Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

