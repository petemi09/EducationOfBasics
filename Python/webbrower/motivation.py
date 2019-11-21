#Created by Mitchell Petellin
import webbrowser
import random
import os

video_list = ["https://www.youtube.com/watch?v=aDCGrINPGUQ","https://www.youtube.com/watch?v=FhzNSPiqO0M","https://www.youtube.com/watch?v=sEmZIi_0Kj8","https://www.youtube.com/watch?v=k9zTr2MAFRg","https://www.youtube.com/watch?v=tbnzAVRZ9Xc","https://www.youtube.com/watch?v=mgmVOuLgFB0","https://www.youtube.com/watch?v=W5tlGJwvmCQ","https://www.youtube.com/watch?v=zQ6ny-fROX8&t=98s"]

def video_choice(list1):
    # list1 = []
    count = 0
    same = False
    x = webbrowser.get(using='chrome')
    if len(list1) < 1:
        #print("test" + str(len(video_list)))
        vid = random.choice(video_list)
        list1.append(vid)
        x.open_new(vid)
        return(list1)
    else:
        while same != True:
            count += 1
            vid = random.choice(video_list)
            if vid in list1:
                #print("Yes, 'at' found in List : " , list1)
                vid = random.choice(video_list)
                if count >= len(video_list):
                    print()
                    print("thats all the video contained in the list")
                    print()
                    break
            if vid not in list1:  
                print("different video")
                list1.append(vid)  
                print("!! " +str(vid))
                x.open_new(vid)
                same = True
        return(list1)

def main():
    done = False
    vids = None
    start_for_empty_list = []
    count =  0
    while done != True:
        val = video_choice(start_for_empty_list)
        count += 1
        vids = input("do you want to play another video? (y/n): ")
        print()
        if vids == "n":
            done = True

main()
