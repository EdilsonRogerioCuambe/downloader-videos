import tkinter
import customtkinter
from pytube import YouTube

def iniciarDownload():
    try:
        url = url_var.get()
        yt = YouTube(url, on_progress_callback=on_progresso)
        video = yt.streams.get_highest_resolution()
        titulo.configure(text="Baixando: " + video.title, text_color="blue")
        terminado.configure(text="")
        video.download()
        terminado.configure(text="Download concluído com sucesso!", text_color="green")
    except Exception as e:
        terminado.configure(text="Erro ao baixar o vídeo!", text_color="red")


def on_progresso(stream, chunk, bytes_remaining):
    total_bytes = stream.filesize
    bytes_downloaded = total_bytes - bytes_remaining
    percent = (bytes_downloaded / total_bytes) * 100
    progeresso_text = str(int(percent))
    progeresso.configure(text=progeresso_text + "%")
    progeresso.update()

    barra_progresso.set(float(percent) / 100)

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("800x800")
app.title("YouTube Downloader")

titulo = customtkinter.CTkLabel(app, text="YouTube Downloader", font=("Arial", 20))
titulo.pack(
    padx=10,
    pady=10
)

url_var = tkinter.StringVar()
url = customtkinter.CTkEntry(app, height=40, width=350, textvariable=url_var)
url.pack()

terminado = customtkinter.CTkLabel(app, text="", font=("Arial", 20))
terminado.pack(
    padx=10,
    pady=10
)

progeresso = customtkinter.CTkLabel(app, text="0%", font=("Arial", 20))
progeresso.pack()

barra_progresso = customtkinter.CTkProgressBar(app, width=400)
barra_progresso.set(0)
barra_progresso.pack(
    padx=10,
    pady=10
)


baixar = customtkinter.CTkButton(app, text="Baixar", command=iniciarDownload)
baixar.pack(
    padx=10,
    pady=10
)

app.mainloop()