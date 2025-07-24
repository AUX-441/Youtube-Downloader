import os
import subprocess


class YTDownloader:
    OUTPUT_DIR = "output"

    @staticmethod
    def download_video(url, cookies_files):

        os.makedirs(YTDownloader.OUTPUT_DIR, exist_ok=True)


        for cookie in cookies_files:
            print(f"Trying to download With : {url} == Cookies : {cookie}")
            try:
                result = subprocess.run(
                    [
                        "yt-dlp",
                        "--cookies", cookie,
                        "--format", "bestvideo[height<=480]+bestaudio/best[height<=480]",
                        "--merge-output-format", "mp4",
                        "--no-playlist",
                        "-o", os.path.join(YTDownloader.OUTPUT_DIR, "%(title)s", "%(title)s.%(ext)s"),

                        url
                    ],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )

                if result.returncode == 0:
                    print(f"Success: Downloaded with {cookie}")
                else:
                    print(f"Failed with {cookie}")

            except Exception as e:
                print(f"Error with {cookie}: {e}")
        print(f"all cookies failed for: {url}")


    @staticmethod
    def run():
        cookies_files = [
            # here will be your cookies.txt .
        ]

        video_urls = [
            "https://www.youtube.com/shorts/iT-_7hjEw6M"
        ]

        for url in video_urls:
            success = YTDownloader.download_video(url, cookies_files)
            if not success:
                print(f"Failed to Download : {url}")

YTDownloader.run()
