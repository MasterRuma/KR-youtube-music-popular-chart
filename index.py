from pytubefix import Playlist 
import csv
import math
import datetime

yt = Playlist("https://music.youtube.com/playlist?list=PL4fGSI1pDJn6jXS_Tv_N9B8Z0HTRVJE0m")
a = 0

with open(f"{datetime.date.today()}_database.csv", 'a', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['순위','제목', '채널', '길이', '조회수' ,'링크'])

    for video in yt.videos:
        a += 1
        print(f'{a}. {video.title} \n {video.author} \n {video.length} \n {video.video_id} \n {video.views}')
        
        total_second = video.length
        minute = math.floor(total_second / 60)
        second = total_second % 60

        if minute < 10:
            minute = "0" + str(minute)
        if second < 10:
            second = "0" + str(second)

        length= f"{minute}:{second}"

        address = f"https://www.youtube.com/watch?v={video.video_id}"

        writer.writerow([a, video.title, video.author, length, video.views, address])
