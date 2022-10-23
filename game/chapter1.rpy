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


label chapter1:

    # window hide
    # show bg candi
    # pause
    # window show
    # show black
    # call screen ourScreen()

    hide windows
    scene chapter1 with fade
    pause
    # hide scene
    scene black with dissolve
    j "Kerajaan Singasari akan berakhir di tangan ku."
    h "Apa perlu kanda? Prabu kertanegara adalah besan kita sekaligus saudara saya."
    j " Dinda, aku akan tetap melaksanakan niatku sejak awal. Jika dulu Ken Arok dapat mendirikan wangsa baru setelah meruntuhkan kediri, maka begitu juga aku. "
    j "Aku akan meruntuhkan Singasari dan membangun darmawangsa baru. Akan ku kembalikan kejayaan kediri."


    hide windows
    scene scene1 with fade
    pause

    scene black with dissolve
    # opening "Singasari yang dipimpin prabu  kertanegara, mendapat kabar dari Senopati sekaligus menantunya, Raden Wijaya."
    # opening "Raden Wijaya mendapat kabar bahwa pasukan Jayakatwang sudah berjaga untuk melakukan pemberontakan, tapi Prabu Kertanegara meremehkan Jayakatwang. "
    # opening "Ia sesumbar bahwa tak ada satupun kerajaan yang dapat mengalahkan Singasari."
    
    k "Tidak mungkin ada yang berani melawan aku, apalagi Jayakatwang. TIDAK MUNGKIN."
    rw " Ampun ayahanda prabu, intel hamba melihat sendiri pasukan jayakatwang mendirikan perkemahan di perbatasan, artinya mereka sengaja unjuk kekuatan"
    k "Siapa yang berani menyerang Singasari? Yang kekuatannya sudah tersohor hingga penjuru negeri, apalagi Cuma Gelanggelang."

    hide windows
    scene scene2 with fade
    pause

    hide windows
    scene scene3 with fade
    pause
    scene black with fade

    hide windows
    scene jayaAttack with fade
    $ persistent.jyt = True
    pause

    scene black with dissolve
    k "Siapa yang menyuruhmu untuk menarik mundur pasukanya?"
    rw "Ampun Ayahanda Prabu, hamba harus mempersiapkan pertahanan untuk melindungi kerajaan."
    k "Pertahanan paling kuat adalah menyerang. Setiap penyerbuan yang terjadi, pasukanku menang karena menyerang, bukan bertahan!"
    rw "Lantas apa yang harus hamba lakukan sekarang Ayahanda Prabu?"
    k "Serbu mereka sekarang juga!"

    # opening "Raden Wijaya beserta pasukan pun melaksanakan perintah Prabu Kertanegara, mereka berangkat ke medan tempur untuk menghadapi pasukan Gelanggelang."
    # opening "Sekali lagi, pasukan Singasari berhasil menekan mundur Pasukan Gelanggelang."

    # opening "Namun ternyata kekalahan pasukan gelanggelang merupakan siasat dari prabu jayakatwang."

    hide windows
    scene scenetambah with fade
    pause
    hide windows
    scene scenetambah1 with fade
    pause

    scene jayaAttack with fade
    j "Semua akan kita balas malam ini, pasukan kita pura pura kalah dan mengepung kota raja."

    hide windows
    scene scene4 with fade
    pause
    # hide scene4
    scene black with fade

    # opening "Siasat Jayakatwang ini tak disadari oleh Prabu Kertanegara dan Senopati Raden Wijaya."
    # opening "Pasukan Jayakatwang menyerang pada malam hari dan berhasil menembus benteng pertahanan Singasari."
    # opening "Satu persatu prajurit gugur  dan Pasukan Jayakatwang berhasil masuk ke kedaton dan berhadapan dengan kertanegara."
    # opening "Tak disangka ternyata Prabu Kertanegara gugur di tangan Jayakatwang."
    # opening "Raden Wijaya, istrinya Putri Tribhuwana dan pengikut setianya termasuk Rangga Lawe, putra Aria Wiraraja terpaksa mundur dan melarikan diri ke sumenep untuk menemui Adipati Aria Wiraraja."

    # opening "Aria Wiraraja awalnya adalah seorang penasihat di Kerajaan Singasari, nama aslinya adalah Banyak Wide"
    # opening "Namun karena perbedaan pendapat dengan Prabu Kertanegara, ia kemudian dipindahkan ke Sumenep dan diberi gelar Aria Wiraraja yang jika diartikan berarti Sang Pemberani."
    # opening "Beliaulah yang menjadi tokoh dibalik berhasilnya pemberontakan Jayakatwang, dan beliau juglah yang nantinya akan menjadi tokoh dibalik berdirinya Majapahit."

    # opening "Di sumenep, Raden Wijaya dan rombongan tidak langsung menemui Adipati Aria Wiraraja."
    # opening "Ia terlebih dahulu mengutus salah satu pengikutnya, Lembu Sora terlebih dahulu untuk meminta izin kepada Adipati Aria Wiraraja."
    # opening "Hal ini karena keraguan Raden Wijaya akan penerimaan Adipati Aria Wiraraja karena konfliknya dengan Prabu Kertanegara."
    # opening "Namun ternyata kekhawatiran Raden Wijaya tidaklah benar, dengan besar hati Aria Wiraraja menerima dengan terbuka kedatangan Raden Wijaya."

    hide windows
    scene scene5 with fade
    pause

    scene black with fade
    a "Tidak mungkin aku menyimpan dendam kepada sang Prabu, apalagi menolak kedatangan Raden Wijaya."
    a "Bagaimanapun, aku adalah abdi negara, dipindahkannya aku ke sumenep adalah sebuah keuntungan bagiku, dijauhi dari orang - orang penjilat di istana."
    a "Orang - orang itu hanya mengiya-kan apa yang dikatakan Prabu, mereka kelihatannya setia dengan prabu."
    a "Tapi yang mereka lakukan adalah menjerumuskan mereka"

    l "Lantas bagaimana hubungan kakang dengan sang Jayakatwang, aku dengar kakang bekerja sama dengannya untuk menyerang Singasari?"

    a "Jayakatwang hanya datang kepadaku, ia datang untuk meminta saran akan ketidakpuasannya sebagai raja bawahan yang seringkali tak dianggap."
    a "Selain itu ia juga ingin membalas dendam leluhurnya"
    a "Aku hanya memberinya saran, bahwa saat itu adalah waktu yang tepat jika ingin menyerang Singasari yang sedang lemah."

    l "Itu artinya kakang membela mereka?"
    a "Aku hanya memberi saran, siapapun yang bertanya kepadaku selalu aku beri saran."
    a "Jayakatwang mendengarkan saran yang ku berikan, sedangkan Prabu Kertanegara menolak saranku, hingga aku dipindahkan ke sini, ke sumenep."
    a "Lantas kenapa pula aku menolak memberi saran kepada Jayakatwang?"


    l "Itu artinya bukan bersekongkol?"
    a "Tentu saja bukan"
    l "Jadi kakang bisa menerima Raden Wijaya di sini?"
    a "Kenapa tidak? Aku kenal baik beliau, keturunan orang besar, Ken Arok Pendiri Singasari."

    # show bg
    v "Agh…. apa yang sudah terjadi?"
    w "Akhirnya kamu sadar juga"
    scene hutan with fade
    $ persistent.hutan = True
    v "Dimana aku sekarang?"
    w "Sekarang kamu berada di perbatasan  Sumenep dan Singasari"
    v "Siapa kamu?!"
    rw "Aku adalah Sanggramawijaya, putra dari Rakyan Jayadarma"
    $ persistent.rw = True
    v "(Tunggu sebentar, aku seperti pernah mendengar namanya"
    v "..........."
    rw "Apakah kamu baik baik saja?"
    v "(Kaget)"
    vn "Maaf paman, namaku adalah Viana"
    $ persistent.vn = True
    rw "Ah nama yang bagus, darimana asalmu?"
    jump asal

    label asal:
        menu:
            "Aku bukan berasal dari sini":
                jump choice1
            
            "Aku tidak mengingatnya":
                jump choice2
    

    label choice1:
        rw "Apakah kamu baik baik saja sepertinya omonganmu mulai melantur?"
        vn "celaka!!! tidak seharusnya aku mengatakan itu"
        rw "Sepertinya kamu masih butuh banyak Istirahat"
        vn "Agh sepertinya begitu"
        rw "apa kepalamu baik baik saja?"
        vn "aku baik baik saja … hanya kepalaku sedikit pusing saja"
        jump mainStory

    
    label choice2:
        vn "(Maaf kan aku paman.. aku harus berbohong kepadamu!!)"
        rw "setidaknya apakah kamu mengingat kamu datang dari arah mana?"
        vn "Yang ku ingat terakhir kali aku berlari dan terjatuh. selanjutnya aku membuka mata dan melihatmu"  
        rw "Untuk sekarang sepertinya kamu perlu istirahat dulu"
        vn "Humm... sepertinya begitu "
        jump mainStory
    
    label mainStory:
        rw "Apakah ini milikmu? aku menemukan ini di dekatmu"
        rw "(Memberikan selembaran itu ke Viana)"
        vn "Sepertinya karena potongan kertas itu.."
        vn "Ah, terima kasih paman"
        rw "..........."
        rw "Tapi, aku tidak bisa berlama lama disini"
        rw "Ikutlah dengan rombongan ku menuju ke sumenep"
        rw "Tidak mungkin aku meninggalkanmu di daerah terbuka seperti ini dengan kondisimu yang buruk"
        rw "Setidaknya sampai keadaanmu sudah membaik kamu boleh pergi.. untuk sekarang rombonganku akan menjagamu"
        vn "(Tidak ada alasan juga untuk menolak tawarannya … setidaknya keamanan ku terjamin, sampai aku menemukan cara untuk keluar dari situasi ini)"
        vn "Haiklah aku akan ikut dengan mu"
        vn "Hore, kamu telah sampai di akhir chapter 1, yuk jawab quiz di sini buat melanjutkan petualanganmu bersamaku di chapter selanjutnya"
        jump chap1question1

    label chap1question1:
        scene quiz with dissolve
        menu:
            vn "Siapa pemimpin pemberontakan Singasari?"

            "Jayakatung":
                jump salah1
            "Jayakatwang":
                jump chap1question2
            "Lembu Sora":
                jump salah1

    label salah1:
        vn "Maaf kamu salah, yuk coba lagi"
        jump chap1question1

    label chap1question2:
        vn "Selamat, kamu berhasil menjawab pertanyaan pertama dengan benar! Yuk jawab pertanyaan kedua"
        menu:
            vn "Siapa nama asli Raden Wijaya?"

            "Sanggrama Wijaya":
                jump chap1question3
            "Gadjah Mada":
                jump salah2
            "Hurukbali":
                jump salah2

    label salah2:
        vn "Maaf kamu salah, yuk coba lagi"
        jump chap1question2

    label chap1question3:
        vn "Selamat, kamu berhasil menjawab pertanyaan kedua dengan benar! Ini pertanyaan terakhir, aku yakin kamu bisa!"
        menu:
            vn "Siapa yang menjabat sebagai senopati sekaligus menantu dari prabu kertanegara pada saat pemberontakan Jayakatwang?"

            "Raden Wijaya":
                jump selamatChap1
            "Rangga Lawe":
                jump salah3
            "Lembu Sora":
                jump salah3
    
    label selamatChap1:
        vn "Yeayyy, kamu keren banget"
        vn "Kamu berhasil menjawab semua pertanyaannya dengan benar, sampai jumpa di Chapter 2 yaa!"
        $ persistent.ch1 = True
        jump chapter2


    label salah3:
        vn "Maaf kamu salah, yuk coba lagi"
        jump chap1question3

        return
    

        # jump question

        # label question:
        #     $ renpy.show_screen(poin)
        #     menu:
        #         "Kamu telah sampai di akhir chapter. Dan kita akan "
        #         "Siapa nama istri jayakatwang?"

        #         "Hurukbali":
        #             $ nilai = True
        #             $ poin += 10

        #         "Dewi":
        #             $ nilai = False
        #             $ poin -= 5
                
        #     return

#     show glitch
    

#     # show viana at  Position(xpos = 1, xanchor = 1, ypos = 0.4, yanchor = 0.4)

#     opening "Berdirinya Kerajaan Majapahit tak lepas dari runtuhnya Kerajaan Singasari."
#     opening "Runtuhnya kerajaan singasari berawal dari pemberontakan Prabu Jayakatwang."
#     opening "Penyerangan ini dipimpin oleh prabu jayakatwang bupati Gelanggelang, salah satu wilayah Kerajaan Kediri (taklukan kerajaan singasari)."
#     j "Kerajaan Singasari akan berakhir di tangan ku."
#     h "Apa perlu kanda? Prabu kertanegara adalah besan kita sekaligus saudara saya."
#     j " Dinda, aku akan tetap melaksanakan niatku sejak awal. Jika dulu Ken Arok dapat mendirikan wangsa baru setelah meruntuhkan kediri, maka begitu juga aku. "
#     j "Aku akan meruntuhkan Singasari dan membangun darmawangsa baru. Akan ku kembalikan kejayaan kediri."
    
#     opening "Singasari yang dipimpin prabu  kertanegara, mendapat kabar dari Senopati sekaligus menantunya, Raden Wijaya."
#     opening "Raden Wijaya mendapat kabar bahwa pasukan Jayakatwang sudah berjaga untuk melakukan pemberontakan, tapi Prabu Kertanegara meremehkan Jayakatwang. "
#     opening "Ia sesumbar bahwa tak ada satupun kerajaan yang dapat mengalahkan Singasari."
   
#     k "Tidak mungkin ada yang berani melawan aku, apalagi Jayakatwang. TIDAK MUNGKIN."
#     w " Ampun ayahanda prabu, intel hamba melihat sendiri pasukan jayakatwang mendirikan perkemahan di perbatasan, artinya mereka sengaja unjuk kekuatan"
#     k "Siapa yang berani menyerang Singasari? Yang kekuatannya sudah tersohor hingga penjuru negeri, apalagi Cuma Gelanggelang."

#     opening "Mendengar tanggapan dari Prabu Kertanegara, Senopati Raden Wijaya tetap mempersiapkan pasukannya."
#     opening "Hal ini ternyata tidak sia – sia, ternyata pemberontakan yang dilakukan Jayakatwang benar adanya, pasukan Jayakatwang mengepung Singasari dari 3 penjuru mata angin,"
#     opening "peperangan pun tak dapat terelakkan Pasukan Singasari yang dipimpin Raden Wijaya pada awalnya berhasil menahan dan mengalahkan gempuran pertama dari pasukan Jayakatwang berkat."
#     opening "Pasukan Jayakatwang pun kembali untuk menyusun rencana."
#     opening "Serupa dengan pasukan Jayakatwang, pasukan Singasari pun ditarik mundur oleh Raden Wijaya untuk menyiapkan pertahanan."
#     opening "Mendengar berita itu, Prabu Kertanegara marah dan memanggil Raden Wijaya menghadapnya."

#     k "Siapa yang menyuruhmu untuk menarik mundur pasukanya?"
#     show bg candi
#     show wijaya at right
#     w "Ampun Ayahanda Prabu, hamba harus mempersiapkan pertahanan untuk melindungi kerajaan."
#     k "Pertahanan paling kuat adalah menyerang. Setiap penyerbuan yang terjadi, pasukanku menang karena menyerang, bukan bertahan!"
#     w "Lantas apa yang harus hamba lakukan sekarang Ayahanda Prabu?"
#     k "Serbu mereka sekarang juga!"

#     opening "Raden Wijaya beserta pasukan pun melaksanakan perintah Prabu Kertanegara, mereka berangkat ke medan tempur untuk menghadapi pasukan Gelanggelang."
#     opening "Sekali lagi, pasukan Singasari berhasil menekan mundur Pasukan Gelanggelang."

#     opening "Namun ternyata kekalahan pasukan gelanggelang merupakan siasat dari prabu jayakatwang."

#     j "Semua akan kita balas malam ini, pasukan kita pura pura kalah dan mengepung kota raja."

#     opening "Siasat Jayakatwang ini tak disadari oleh Prabu Kertanegara dan Senopati Raden Wijaya."
#     opening "Pasukan Jayakatwang menyerang pada malam hari dan berhasil menembus benteng pertahanan Singasari."
#     opening "Satu persatu prajurit gugur  dan Pasukan Jayakatwang berhasil masuk ke kedaton dan berhadapan dengan kertanegara."
#     opening "Tak disangka ternyata Prabu Kertanegara gugur di tangan Jayakatwang."
#     opening "Raden Wijaya, istrinya Putri Tribhuwana dan pengikut setianya termasuk Rangga Lawe, putra Aria Wiraraja terpaksa mundur dan melarikan diri ke sumenep untuk menemui Adipati Aria Wiraraja."

#     opening "Aria Wiraraja awalnya adalah seorang penasihat di Kerajaan Singasari, nama aslinya adalah Banyak Wide"
#     opening "Namun karena perbedaan pendapat dengan Prabu Kertanegara, ia kemudian dipindahkan ke Sumenep dan diberi gelar Aria Wiraraja yang jika diartikan berarti Sang Pemberani."
#     opening "Beliaulah yang menjadi tokoh dibalik berhasilnya pemberontakan Jayakatwang, dan beliau juglah yang nantinya akan menjadi tokoh dibalik berdirinya Majapahit."

#     opening "Di sumenep, Raden Wijaya dan rombongan tidak langsung menemui Adipati Aria Wiraraja."
#     opening "Ia terlebih dahulu mengutus salah satu pengikutnya, Lembu Sora terlebih dahulu untuk meminta izin kepada Adipati Aria Wiraraja."
#     opening "Hal ini karena keraguan Raden Wijaya akan penerimaan Adipati Aria Wiraraja karena konfliknya dengan Prabu Kertanegara."
#     opening "Namun ternyata kekhawatiran Raden Wijaya tidaklah benar, dengan besar hati Aria Wiraraja menerima dengan terbuka kedatangan Raden Wijaya."

#     opening "Tidak mungkin aku menyimpan dendam kepada sang Prabu, apalagi menolak kedatangan Raden Wijaya."
#     opening "Bagaimanapun, aku adalah abdi negara, dipindahkannya aku ke sumenep adalah sebuah keuntungan bagiku, dijauhi dari orang - orang penjilat di istana."
#     opening "Orang - orang itu hanya mengiya-kan apa yang dikatakan Prabu, mereka kelihatannya setia dengan prabu."
#     opening "Tapi yang mereka lakukan adalah menjerumuskan mereka"

#     l "Lantas bagaimana hubungan kakang dengan sang Jayakatwang, aku dengar kakang bekerja sama dengannya untuk menyerang Singasari?"

#     a "Jayakatwang hanya datang kepadaku, ia datang untuk meminta saran akan ketidakpuasannya sebagai raja bawahan yang seringkali tak dianggap."
#     a "Selain itu ia juga ingin membalas dendam leluhurnya"
#     a "Aku hanya memberinya saran, bahwa saat itu adalah waktu yang tepat jika ingin menyerang Singasari yang sedang lemah."

#     l "Itu artinya kakang membela mereka?"
#     a "Aku hanya memberi saran, siapapun yang bertanya kepadaku selalu aku beri saran."
#     a "Jayakatwang mendengarkan saran yang ku berikan, sedangkan Prabu Kertanegara menolak saranku, hingga aku dipindahkan ke sini, ke sumenep."
#     a "Lantas kenapa pula aku menolak memberi saran kepada Jayakatwang?"


#     l "Itu artinya bukan bersekongkol?"
#     a "Tentu saja bukan"
#     l "Jadi kakang bisa menerima Raden Wijaya di sini?"
#     a "Kenapa tidak? Aku kenal baik beliau, keturunan orang besar, Ken Arok Pendiri Singasari."
#     # jump question

# # label question:
# #     $ renpy.show_screen(poin)
# #     menu:
# #         "Kamu telah sampai di akhir chapter. Dan kita akan "
# #         "Siapa nama istri jayakatwang?"

# #         "Hurukbali":
# #             $ nilai = True
# #             $ poin += 10

# #         "Dewi":
# #             $ nilai = False
# #             $ poin -= 5
        
# #     return