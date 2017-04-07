from pydub import AudioSegment
AudioSegment.converter = "path/to/ffmpeg"
song = AudioSegment.from_mp3("C:\\Users\\felipe.simao\\Documents\\GitHub\\AlertManager\\alarme1.mp3")
