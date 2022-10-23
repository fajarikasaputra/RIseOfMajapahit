image pararaton = ("galleryUI/paratonDetail.png")
image profViana = ("galleryUI/profilViana.png")
image profRaden = ("galleryUI/profilRaden.png")
image profJaya = ("galleryUI/profilJayakatwang.png")
image profIstri = ("galleryUI/profilIstri.png")
image jayaAttack = ("images/jayaAttack.png")
image met = ("images/meet & greet.png")
image baca = ("images/bacaBuku.png")

screen gallery():
    
    add ("images/bg-candi.png")
    imagebutton:
        idle "galleryUI/charOff.png" 
        hover ("galleryUI/charOn.png") 
        xpos 120 
        ypos 200
        action Start("char")
    imagebutton: 
        idle "galleryUI/artefakOff.png" 
        hover "galleryUI/artefakOn.png"
        xpos 1030 
        ypos 200
        action Start("art")
    imagebutton: 
        idle "galleryUI/sceneOff.png" 
        hover "galleryUI/sceneOn.png"
        xpos 575
        ypos 650
        action Start("sin")

    vbox:
        # style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.03
        xalign -0.13
        imagebutton:
            idle "settingUI/back.png"
            hover "settingUI/onback.png"
            action Return()

screen art():
    add ("images/bg-candi.png")
    # tag menu
    # default ta = Tooltip(None)
    # default td = Tooltip(None)
    # default te = Tooltip(None)
    # default tf = Tooltip(None)

    style_prefix "chapter_menu"
    imagebutton:
        idle "galleryUI/paratonOff.png" 
        hover ("galleryUI/paratonOn.png") 
        xpos 120 
        ypos 160 
        action Start("kitab")
        sensitive persistent.pr == True
    imagebutton: 
        idle "galleryUI/negarakertagamaOff.png" 
        hover "galleryUI/negarakertagamaOn.png"
        xpos 1030 
        ypos 160
        action Start("negarakertagama")
        sensitive persistent.ng == True
    imagebutton:
        idle "galleryUI/sutasomaOff.png" 
        hover "galleryUI/sutasomaOn.png"
        xpos 120 
        ypos 600 
        action Start("sutasoma")
        sensitive persistent.sts == True
    # imagebutton:
    #     idle "chapterUI/chapterEmpatOff.png" 
    #     hover "chapterUI/chapterEmpatOn.png" 
    #     xpos 1030 
    #     ypos 600  
    #     action Start("chapter4")
    #     sensitive persistent.ch1 == True and persistent.ch2 == True and persistent.ch3 == True

    vbox:
        # style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.03
        xalign -0.13
        imagebutton:
            idle "settingUI/back.png"
            hover "settingUI/onback.png"
            action Return()



label art:
    call screen art

screen char():
    add ("images/bg-candi.png")
    style_prefix "chapter_menu"
    imagebutton:
        idle "galleryUI/vianaOff.png" 
        hover ("galleryUI/vianaOn.png") 
        xpos 120 
        ypos 160 
        action Start("viana")
        sensitive persistent.vn == True
    imagebutton: 
        idle "galleryUI/radenOff.png" 
        hover "galleryUI/radenOn.png"
        xpos 1030 
        ypos 160
        action Start("wijaya")
        sensitive persistent.rw == True
    imagebutton:
        idle "galleryUI/istriOff.png" 
        hover "galleryUI/istriOn.png"
        xpos 120 
        ypos 600 
        action Start("istri")
        sensitive persistent.is3 == True
    imagebutton:
        idle "galleryUI/jayakatwangOff.png" 
        hover "galleryUI/jayakatwangOn.png" 
        xpos 1030 
        ypos 600  
        action Start("jaya")
        sensitive persistent.jyk == True

    vbox:
        # style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.03
        xalign -0.13
        imagebutton:
            idle "settingUI/back.png"
            hover "settingUI/onback.png"
            action Return()

label char:
    call screen char

screen sin():
    add ("images/bg-candi.png")
    style_prefix "chapter_menu"
    imagebutton:
        idle "galleryUI/pertemuanOff.png" 
        hover "galleryUI/pertemuanOn.png"
        xpos 120 
        ypos 600 
        action Start("met")
        sensitive persistent.hutan == True
    imagebutton:
        idle "galleryUI/garisdarimasadepanOff.png" 
        hover ("galleryUI/garisdarimasadepanOn.png") 
        xpos 120 
        ypos 160 
        action Start("bacabuku")
        sensitive persistent.mg == True
    imagebutton: 
        idle "galleryUI/runtuhnyaSingasariOff.png" 
        hover "galleryUI/runtuhnyaSingasariOn.png"
        xpos 1030 
        ypos 160
        action Start("berontak")
        sensitive persistent.jyt == True


    vbox:
        # style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.03
        xalign -0.13
        imagebutton:
            idle "settingUI/back.png"
            hover "settingUI/onback.png"
            action Return()

label sin:
    call screen sin

screen chapter():
    add ("images/bg-candi.png")
    # tag menu
    # default ta = Tooltip(None)
    # default td = Tooltip(None)
    # default te = Tooltip(None)
    # default tf = Tooltip(None)

    style_prefix "chapter_menu"
    imagebutton:
        idle "chapterUI/chapterSatuOff.png" 
        hover ("chapterUI/chapterSatuOn.png") 
        xpos 120 
        ypos 160 
        action Start("chapter1")
    imagebutton: 
        idle "chapterUI/chapterDuaOff.png" 
        hover "chapterUI/chapterDuaOn.png"
        xpos 1030 
        ypos 160
        action Start("chapter2")
        sensitive persistent.ch1 == True
    imagebutton:
        idle "chapterUI/chapterTigaOff.png" 
        hover "chapterUI/chapterTigaOn.png"
        xpos 120 
        ypos 600 
        action Start("chapter3")
        sensitive persistent.ch1 == True and persistent.ch2 == True  # variable value
    imagebutton:
        idle "chapterUI/chapterEmpatOff.png" 
        hover "chapterUI/chapterEmpatOn.png" 
        xpos 1030 
        ypos 600  
        action Start("chapter4")
        sensitive persistent.ch1 == True and persistent.ch2 == True and persistent.ch3 == True

    vbox:
        # style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.03
        xalign -0.13
        imagebutton:
            idle "settingUI/back.png"
            hover "settingUI/onback.png"
            action Return()

label met:
    hide windows
    scene met with fade
    pause

    jump sin

label bacabuku:
    hide windows
    scene baca with fade
    pause 

    jump sin

label berontak:
    hide windows
    scene jayaAttack with fade
    pause

    jump chapter1

label kitab:
    hide windows
    scene pararaton with fade
    pause

    jump art


label viana:
    hide windows
    scene profViana
    pause

    jump char

label wijaya:
    hide windows
    scene profRaden
    pause

    jump char
    
label istri:
    hide windows
    scene profIstri
    pause

    jump char

label jaya:
    hide windows
    scene profJaya
    pause

    jump char
