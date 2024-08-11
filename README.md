# Django Image Background Remover

## Overview

This project is a Django web application that allows users to upload an image, remove its background, and download the processed image. It uses the `rembg` library to remove backgrounds and `Pillow` for image processing.

## Features

- Upload an image in various formats (e.g., PNG, JPEG).
- Remove the background from the uploaded image.
- Display both the original and processed images.
- Download the processed image.
- Simple and user-friendly interface.

## Technologies Used

- **Django**: Web framework for building the web application.
- **Python**: Programming language used for the backend.
- **Pillow**: Python Imaging Library (PIL) for image processing.
- **rembg**: Library to remove backgrounds from images.

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Clone the Repository

```bash
git clone https://github.com/kavinandan18/image-background-remover.git
cd image-background-remover
```
### Create a Virtual Environment
```bash
python -m venv venv
```
Activate the Virtual Environment
```bash
    On Windows:
venv\Scripts\activate
```
```bash
On macOS/Linux:
source venv/bin/activate
```
Install Dependencies
```bash
pip install -r requirements.txt
```
### Run Migrations
```bash
python manage.py migrate
```
### Start the Development Server
```bash
python manage.py runserver
Open your browser and navigate to http://127.0.0.1:8000/ to access the application.
```
