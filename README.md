# 🎬 YTDownloader - YouTube Video Downloader Using Cookies

YTDownloader is a simple Python-based tool to download YouTube videos (including Shorts) using multiple `cookies.txt` files for access, leveraging the powerful `yt-dlp` backend. This is especially useful for downloading private or region-locked content that requires authentication.

## ✨ Features

- Supports authenticated video downloads using cookies
- Automatically tries multiple cookie files
- Downloads in 480p (best available <= 480p)
- Merges video and audio into MP4
- Creates output folders per video title
- Supports YouTube Shorts

## ⚙️ Requirements

- [Python 3.7+](https://www.python.org/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- `cookies.txt` file(s) exported from your browser

## 🛠 Installation

Install `yt-dlp` if not already available:

```bash
pip install -U yt-dlp
