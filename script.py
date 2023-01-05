from moviepy.editor import VideoFileClip
from moviepy.editor import VideoFileClip
import imageio
import moviepy.editor as mp

# video cutter 
def video_cutter(video_to_cut, start_time, end_time, name_of_the_new_video):
    clip = VideoFileClip("{}.mp4".format(video_to_cut))
    video_clipped = clip.subclip(start_time, end_time)
    video_clipped.write_videofile("{}.mp4".format(name_of_the_new_video))

# gif maker
def gif_maker(video, width, height, name_of_the_gif):
    clip = VideoFileClip("{}.mp4".format(video))
    resized_clip = clip.resize((width, height)) 
    resized_clip.write_gif("{}.gif".format(name_of_the_gif))

# Editeur audio video (rendre silencieux ou créer un mp3)

def audio_editor(video_to_edit, name_of_the_edit, silence=False):
    if silence:
        video = mp.VideoFileClip("{}.mp4".format(video_to_edit))
        video_without_audio = video.without_audio()
        video_without_audio.write_videofile("{}.mp4".format(name_of_the_edit))
    elif not silence :
        video = mp.VideoFileClip("{}.mp4".format(video_to_edit))
        start_time = int(input("Choisissez le début : "))
        end_time = int(input("Choisissez la fin : "))
        audio = video.subclip(start_time, end_time).audio
        audio.write_audiofile("{}.mp3".format(name_of_the_edit))

print("Bienvenue dans le vidéo editeur !")

print("Voici vos différentes options. \n 1 - Le video cutter. \n 2 - Le gif maker. \n 3 - L'éditeur audio")

choice = int(input("Quel est votre choix ? "))

if choice == 1 :
    video = input("Veillez choisir la video à couper : ")
    start = input("Veillez choisir le début de la vidéo : ")
    end = input("Veillez choisir le début de la vidéo : ")
    new_name = input("Veillez choisir le nom de la vidéo après l'édition : ")

    try :
        video_cutter(video, start, end, new_name)
    except :
        print("Vous n'avez pas donné les bonnes informations")    

elif choice == 2 :
    video = input("Veillez choisir la video à editer : ")
    width = int(input("Veillez choisir la longeur : "))
    height = int(input("Veillez choisir la largeur : "))
    new_name = input("Veillez choisir le nom de la vidéo après l'édition : ")

    try :
        gif_maker(video, width, height, new_name)
    except :
        print("Vous n'avez pas donné les bonnes informations") 

elif choice == 3 :
    video = input("Veillez choisir la video à editer : ")
    new_name = input("Veillez choisir le nom de la vidéo après l'édition : ")
    silence = input("Voulez-vous supprimer l'audio ? (Y/N) ")
    if silence == 'Y' :
        try :
            audio_editor(video, new_name, True)
        except :
            print("Vous n'avez pas donné les bonnes informations") 
    elif silence == 'N' :
        try :
            audio_editor(video, new_name)
        except : 
            print("Vous n'avez pas donné les bonnes informations") 
    else :
        print("Vous n'avez pas donné les bonnes informations") 
else :
    print("Vous n'avez pas donné les bonnes informations") 
