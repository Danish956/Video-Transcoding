#======================================= Import all Modules and Libraries ====================================================
from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect,HttpResponse
from Alpha_intern_LMS_app.models.customuser import*
from Internship_app.models import*
import subprocess
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Internship_Topic, Internship_Data
from moviepy.editor import VideoFileClip
from django.core.files import File
from django.conf import settings
import os



def upload_internship_video(request):
    if request.method == 'POST':
        lesson_id = request.POST.get('lesson_id')
        title = request.POST.get('title')
        video_thumbnail = request.FILES.get('video_thumbnail')
        video = request.FILES.get('video')

        get_internship_data = Internship_Lesson.objects.get(id=lesson_id)

        internship_topic = Internship_Topic(
            lesson=get_internship_data,
            title=title,
            video_thumbnail=video_thumbnail,
            video=video
        )
        internship_topic.save()

        # Transcode the video
        video_path = internship_topic.video.path
        transcode_video(video_path, internship_topic.id)

        messages.success(request, 'Form successfully submitted!')
        return redirect('upload_internship_video')

    lessons = Internship_Lesson.objects.all()
    return render(request, 'internship/pages/upload_internship_video.html', {'lessons': lessons})



def transcode_video(video_path, topic_id):
    resolutions = {
        '360p': (640, 360),
        '480p': (854, 480),
        '720p': (1280, 720),
        '1080p': (1920, 1080)
    }

    base_dir = os.path.dirname(video_path)
    base_filename = os.path.basename(video_path).rsplit('.', 1)[0]
    ext = os.path.splitext(video_path)[1]

    internship_topic = Internship_Topic.objects.get(id=topic_id)

    for res, (width, height) in resolutions.items():
        output_filename = f"{base_filename}_{res}{ext}"
        output_dir = os.path.join(settings.MEDIA_ROOT, 'image', 'download', 'uploads', 'internship_video', 'original', res)
        output_path = os.path.join(output_dir, output_filename)

        # Ensure directory exists
        os.makedirs(output_dir, exist_ok=True)

        try:
            clip = VideoFileClip(video_path)
            clip_resized = clip.resize(newsize=(width, height))
            clip_resized.write_videofile(output_path, codec='libx264')

            # Save the transcoded video path to the model
            relative_output_path = os.path.relpath(output_path, settings.MEDIA_ROOT)
            with open(output_path, 'rb') as f:
                file_field = File(f)
                getattr(internship_topic, f'video_{res}').save(output_filename, file_field)
                internship_topic.save()

            clip.close()
        except Exception as e:
            print(f"Error transcoding video to {res}: {e}")
            continue



