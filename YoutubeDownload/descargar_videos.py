import pytube

class GetYoutube:

    def __init__(self,url):
        self.url = url
        self.getUrl(self.url)

    def getUrl(self,url):
        youtube = pytube.YouTube(self.url)
        video = youtube.streams.first()#obtener el primer resultado de la consulta 
        return video
    #obtencion de la data

    def save(self):
        descarga =self.video.download(r'C:\Users\sergi\Videos')#descarga del video

