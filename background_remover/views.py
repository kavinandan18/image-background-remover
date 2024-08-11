from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from rembg import remove
from PIL import Image
import io
from django.core.exceptions import ValidationError

def is_image(file):
    try:
        Image.open(file)
        return True
    except (IOError, SyntaxError) as e:
        return False

def index(request):
    return render(request, 'background_remover/index.html')

def upload_image(request):
    if request.method == 'POST' and 'image' in request.FILES:
        image_file = request.FILES['image']

        # Ensure the file is not empty
        if image_file.size == 0:
            return render(request, 'background_remover/index.html', {'error': 'Empty file'})

        # Read and process the image file
        try:
            image_data = image_file.read()
            image = Image.open(io.BytesIO(image_data))
            image = image.convert('RGBA')  # Convert to RGBA to ensure compatibility
        except Exception as e:
            return render(request, 'background_remover/index.html', {'error': f'Failed to open image: {str(e)}'})

        # Process the image
        output = io.BytesIO()
        try:
            output_image = remove(image)
            output_image.save(output, format='PNG')
            output.seek(0)
        except Exception as e:
            return render(request, 'background_remover/index.html', {'error': f'Failed to process image: {str(e)}'})

        # Save the processed image
        fs = FileSystemStorage()
        filename = fs.save('processed_' + image_file.name, output)
        processed_file_url = fs.url(filename)

        return render(request, 'background_remover/result.html', {
             'uploaded_file_url': image_file,
            'processed_file_url': processed_file_url
        })
    return redirect('index')
