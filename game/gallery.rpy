# screen char():
#     imagebutton:
#         idle "chapterUI/chapterSatuOff.png" 
#         hover ("chapterUI/chapterSatuOn.png") 
#         xpos 120 
#         ypos 160 
#         action Start("chapter1")
#     imagebutton: 
#         idle "chapterUI/chapterDuaOff.png" 
#         hover "chapterUI/chapterDuaOn.png"
#         xpos 1030 
#         ypos 160
#         action Start("chapter2")
#         sensitive persistent.ch1 == True
#     imagebutton:
#         idle "chapterUI/chapterTigaOff.png" 
#         hover "chapterUI/chapterTigaOn.png"
#         xpos 120 
#         ypos 600 
#         action Start("chapter3")
#         sensitive persistent.ch1 == True and persistent.ch2 == True  # variable value
#     imagebutton:
#         idle "chapterUI/chapterEmpatOff.png" 
#         hover "chapterUI/chapterEmpatOn.png" 
#         xpos 1030 
#         ypos 600  
#         action Start("chapter4")
#         sensitive persistent.ch1 == True and persistent.ch2 == True and persistent.ch3 == True

#     vbox:
#         # style_prefix "navigation"
#         xpos gui.navigation_xpos
#         yalign 0.03
#         xalign -0.13
#         imagebutton:
#             idle "settingUI/back.png"
#             hover "settingUI/onback.png"
#             action Return()