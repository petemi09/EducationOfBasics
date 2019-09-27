#Created by Mitchell Petellin
import webbrowser
import random
import os

video_list = ["https://www.youtube.com/watch?v=aDCGrINPGUQ","https://www.youtube.com/watch?v=FhzNSPiqO0M","https://www.youtube.com/watch?v=sEmZIi_0Kj8","https://www.youtube.com/watch?v=k9zTr2MAFRg","https://www.youtube.com/watch?v=tbnzAVRZ9Xc","https://www.youtube.com/watch?v=eWJVvNptHZ4&t","https://www.youtube.com/watch?v=mgmVOuLgFB0","https://www.youtube.com/watch?v=W5tlGJwvmCQ","https://www.youtube.com/watch?v=zQ6ny-fROX8&t=98s"]

def video_choice():
    x = webbrowser.get(using='chrome')
    vid = random.choice(video_list)
    x.open_new(vid)

def main():
    video_choice()

main()
