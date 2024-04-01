# from pytube import YouTube
# from sys import argv

# link = argv[1]
# yt = YouTube(link)

# # print("Title: ", yt.title)
# # print("Views: ", yt.views)

# yd = yt.streams.get_highest_resolution()

# yd.download('C:\\Users\\User\\OneDrive\\Desktop\\downloaded video\\using python')

# libraries ========================================================
# libraries ========================================================

from pytube import YouTube
import os

# download video using pytube
def download_video(url, output_path):
    try:
        yt = YouTube(url)
        yd = yt.streams.get_highest_resolution()

       # details on download 
        print("Downloading... ")
        print("========== Details ==========")
        print("Title: ", yt.title)
        print("Views: ", yt.views)
        print("Channel Name: ", yt.author)

        #download yt in output_path
        yd.download(output_path)

        print("Video has been downloaded successfully!")

    except Exception as e:
        print("Error: ", e)
        

# main function to run program
def main():
    url = input("Put the youtube URL: ")
    output_path = 'C:\\Users\\User\\OneDrive\\Desktop\\downloaded video\\using python'
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    download_video(url, output_path)

if __name__ == "__main__":
    main()
