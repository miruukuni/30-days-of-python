import math

fight = 'world'

print(f"something{math.pi:.200f} what in the {fight} world")

language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto


text = '''Yes, this exact concept exists and is widely used across both commercial applications and open-source software. The specific workflow
you described—OCR/Text Extraction $\rightarrow$ Machine Translation $\rightarrow$ Custom Voice Clone/TTS Synthesis—is the backbone of 
modern AI voiceover and localized dubbing pipelines.Popular Applications & ToolspyVideoTrans (Open Source): A desktop application 
specifically built to scan text/subtitles or recognizespoken video audio, translate it into a target language, and generate voiceover
using imported custom voice models or local engines (like F5-TTS, Coqui XTTS, or Fish Speech).  Speechify: Offers camera and document OCR 
scanning. It translates the extracted text into target languages and reads it back using AI voice models.  ElevenLabs / HeyGen AI Dubbing:
End-to-end video localization tools. They extract speech/text from media, translate the script, and  clone the original speaker's voice 
(or an imported reference audio model) to render the new voiceover. Owll Translator: Focuses on real-time speech translation that clones 
and preserves your imported voice identity while outputting translated audio.  '''
print(text.count('io', 5, len(text) - 200))
print(text.find('io', 5, len(text) - 200))