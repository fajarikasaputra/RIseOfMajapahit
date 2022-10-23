image pararaton = ("galleryUI/paratonDetail.png")
image profViana = ("galleryUI/profilViana.png")
image profRaden = ("galleryUI/profilRaden.png")
image profJaya = ("galleryUI/profilJayakatwang.png")
image profIstri = ("galleryUI/profilIstri.png")
image jayaAttack = ("images/jayaAttack.png")
image met = ("images/meet & greet.png")
image baca = ("images/bacaBuku.png")

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

    jump sin

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
