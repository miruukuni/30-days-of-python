# # # # age = 100
# # # # personheight = 1.75
# # # # cnumber = (1 + 2j)


# # # # base = input("Enter the base: ")
# # # # height = input("Enter the height: ")

# # # # if base.isdigit() and height.isdigit():
# # # #     base = int(base)
# # # #     height = int(height)
# # # #     area = 0.5 * base * height
# # # #     print(f"The area of the triangle is: {area}")
# # # # elif base.isdigit() and not height.isdigit():
# # # #     print('youre stupid, enter a number for the height')
# # # # elif not base.isdigit() and height.isdigit():
# # # #     print('youre stupid, enter a number for the base')
# # # # else:
# # # #     print('why are you so stupid, enter a number for both the base and height')

# # # # # y=2x - 2
# # # # slope = 2
# # # # base = -2

# # # # xintercept = -base / slope
# # # # print(xintercept)

# # # # # m=y2-y1/x2-x1 (2,2) (6,10)
# # # # y2, y1, x2, x1 = 10, 2, 6, 2
# # # # slope = (y2 - y1) / (x2 - x1)
# # # # print(slope)


# # # a, b = 5, 10
# # # is_less = a < b
# # # is_greater = a > b
# # # is_equal = a == b
# # # print(is_less)

# # print('on' not in ['what in the world', 'is going on', 'what is this'])

# print(len('python') > len('dragon'))

# print(f"{float(len('python')):.9f}")

# print('10' is 10)

# print('10' == 10)

# print(int(float('9.8')) == 10)
# print(int(float('9.8')) is 10)

# print(int(float('9.8')))


# number = 21

# if number % 2 == 0:
#     print(True)
# else:
#     print(False)




# question_answered = False

# while question_answered == False:
#     hours = input('how many hours')
#     entry = input('how much per hour')

#     if hours.isdigit() and entry.isdigit():
#         print(f"you got this much money: {int(hours) * int(entry)}")
#         question_answered = True
#     else:
#         print('you\'re stupid, enter a number for both the hours and the entry')


# years_lived = input('how many years have you lived')
# years_to_seconds = 100 * 365 * 24 * 60 * 60
# if years_lived.isdigit():
#     print(f"you have lived for {years_to_seconds * int(years_lived)} seconds")
# else:
#     print('you\'re stupid, enter a number for the years lived')   
# print(type(123.45))

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