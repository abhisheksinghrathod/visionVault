from django.shortcuts import render
from .forms import VideoForm
from .tasks import process_video

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            process_video.delay(video.id)  # Asynchronously process the video
            return render(request, 'upload_success.html', {'video': video})
    else:
        form = VideoForm()
    return render(request, 'upload_video.html', {'form': form})
