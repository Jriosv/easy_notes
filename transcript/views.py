from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        mp3_file = request.FILES['mp3-file']
        print(f'file: {mp3_file}')
        
        """
        -Toda la logica del whiper aquí y el resultado lo guardan en la variable whisper_result
        
        -Otra alternativa es tener el archivo .py dentro de este directorio o afuera en general en el proyecto
         en una carpeta llamada utils o helpers e importan la funcionalidad de transcribir aquí, por ejemplo:
         
         from ..helpers.whisper import whisper_transcript_method
         
         whisper_result = whisper_transcript_method()"""
         
        
        whisper_result = "Este es el resultado de la transcripción..."
        
        return render(request, 'transcript/success.html',context={'message': whisper_result})
    else:
        context = {}
        return render(request, 'transcript/base.html')
   



