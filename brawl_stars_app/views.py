from django.shortcuts import render, redirect
from .models import *
import json
import requests

def index(request):
    url = "https://api.brawlstars.com/v1/brawlers"
    auth = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijc1ZjM4NDQ0LTIzNjYtNGExYy1iNDNmLWIzZGQ0ZmIyNjdiMSIsImlhdCI6MTYyNzE4NzI5NSwic3ViIjoiZGV2ZWxvcGVyLzIxMzA4MmVhLWZmYzktNWUyNi02Zjc3LTc1MDRhNzc1MDA3YyIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiNzMuMjIyLjE3Ny4xMDUiXSwidHlwZSI6ImNsaWVudCJ9XX0.-N8mGMdTubxasjirN-kYKszb4NG5ZedHCWOqPNl4IS-DiKMnPcCA0wKWkKxaWoMk6GtENP-Dsa0tb_UjW2_8wQ"
    auth2 = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjBhZGJhNzM4LTIzNDktNGJiMi05ZDUwLTUwZmNjYzIzMTQzMyIsImlhdCI6MTYyNzEwMjMyNSwic3ViIjoiZGV2ZWxvcGVyLzIxMzA4MmVhLWZmYzktNWUyNi02Zjc3LTc1MDRhNzc1MDA3YyIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiOC44LjguOCJdLCJ0eXBlIjoiY2xpZW50In1dfQ.wa575hsUnjfHxCMs0IHTP_jymwh9LxlHxFFcFT0kgcFEGKz1BQGSVS3dj1uEcgFxpveFnEaqdCmoJsBCbCts4Q"
    headers = {"authorization": "Bearer " + auth + ""}
    response = requests.get(url, headers=headers)
    bs = response.json()
    # print("BRAWLER LIST", bs)

    context = {
        'obj': bs['items'],
    }
    return render(request, 'index.html', context)

def profile(request):
    context = {

    }
    return render(request, 'profile.html', context)