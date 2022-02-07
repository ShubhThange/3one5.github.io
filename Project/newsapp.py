import requests
import tkinter as tk

def getNews():
    api_key ="88d46c250e444f0dbaf903fd04079801"
    url = "https://newsapi.org/v2/top-headlines?country=ind&category=business&apiKey="+api_key
    news = requests.get(url).json()
canvas = tk.tk()
canvas.geometry("900x600")
canvas.title("News App")

button = tk.Button(canvas, font =24, text = "Reload", command = getNews)
button.pack(pady =20)

lable = tk.lable(canvas, font = 28, justify ="left")
lable.pack(pady =20)

canvas.mainloop()