image chapter2 = "chapterUI/chap2.png"
image glitch = "images/glitch-bg.png"
# image bg candi = "images/bg-candi.png"
image bg semut = "images/bgsemut.png"
image viana = "images/viana.png"
# image wijaya = "images/wijaya.png"    
image black = "images/black.png"
image hutan = "meet & greet.png"
image chapter1 = "chapterUI/chap1.png"
image quiz = "images/quizBg.png"
image scene1 = "narasi/1.png"
image scene2 = "narasi/2.png"
image scene3 = "narasi/3.png"
image scene4 = "narasi/4.png"
image scene5 = "narasi/5.png"
image scene6 = "narasi/6.png"
image scenetambah = "narasi/masuk1.png"
image scenetambah1 = "narasi/masuk2.png"
image black = "images/black.png"
image jayaAttack = "images/jayaAttack.png"
image chap2op1 = "narasi/viana1.png"
image chap2op2 = "narasi/viana2.png"
image chap2op3 = "narasi/viana3.png"
image chap2op4 = "narasi/viana4.png"
image bacaBuku = "images/bacaBuku.png"
#image jayakatwang = "images/jayakatwang.png"
#image jayakatwang = "images/jayakatwang.png"
#image hurukbali = "images/hurukbali.png"

define opening = Character("")
define v = Character ("???")
define vn = Character ("Viana")
define j = Character ("Jayakatwang")
define h = Character ("Hurukbali")
define k = Character ("Prabu Kertanegara")
define w = Character ("??")
define rw = Character ("Raden Wijaya")
define l = Character ("Lembu Sora")
define a = Character ("Aria Wiraraja")
define an = Character ("Anindya")

label chapter2:
    hide windows
    scene chapter2 with fade
    pause

    scene black with fade

    hide windows
    scene chap2op1 with fade
    pause

    hide windows
    scene chap2op2 with fade
    pause

    scene black with fade
    
    show viana at left
    vn "Permisi Ibu Anindya......"
    an "Iyaa Viana, mau pinjem buku ibu ya? Ambil aja di tempat biasa yaa"
    vn "Mohon maaf ibu, bukunya boleh Viana pinjem untuk baca di rumah tidak bu?"
    an "Iyaa tentu saja, silahkan Viana"

    hide windows
    scene chap2op3 with fade
    pause

    scene black with fade

    hide windows
    scene chap2op3 with fade
    pause



default grid_width = 3
default grid_height = 3
define puzzle_field_size = 650
define puzzle_field_offset = 30
define puzzle_piece_size = 450
define grip_size = 75
define active_area_size = puzzle_piece_size - (grip_size * 2)


label buku:
    scene quiz with fade

    # put the puzzle in separate label to be able to call it several times in game
    
    # the puzzle loading takes some time, so let's warn the player
    # centered "Loading data...{nw}" # nw-tag is necessary for puzzle to actually start
    
    # let's set the puzzle variables
    $ grid_width = 3
    $ grid_height = 3
    $ chosen_img = "images/kitabPararaton.png"
    # and call puzzle label
    call puzzle
    $ persistent.pr = True
    
    hide windows
    scene bacaBuku with fade
    vn "APA INII?!!!"
    pause
    jump buku

    return