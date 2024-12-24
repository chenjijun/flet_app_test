import flet as ft
import requests
import random
import re

sample_media = []
url = 'http://chenjj.ddns.net:8084/test/'
respones = requests.get(url)
print(respones.text)
for line in respones.text.splitlines():
    if '.mp4' in line or '.avi' in line:
        sample_media.append(ft.VideoMedia(
            url + re.findall('>(.+)</a>',line)[0]
        ))

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "TheEthicalVideo"
    page.window.always_on_top = True
    page.spacing = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    def handle_next(e):
        video.next()
        print("Video.next()")

    def handle_previous(e):
        video.previous()
        print("Video.previous()")

   

    page.add(
        video := ft.Video(
            expand=True,
            playlist=sample_media,
            playlist_mode=ft.PlaylistMode.LOOP,
            fill_color=ft.Colors.BLUE_400,
            aspect_ratio=16/9,
            volume=100,
            autoplay=True,
            filter_quality=ft.FilterQuality.HIGH,
            muted=False,
            show_controls=True,
            shuffle_playlist=True,
        ),
        ft.Row(
            wrap=True,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Button(
                    "上一个视频",
                    on_click=handle_previous
                ),
                ft.Button(
                    "下一个视频",
                    on_click=handle_next
                ),
            ],
        ),
)


ft.app(target=main)
