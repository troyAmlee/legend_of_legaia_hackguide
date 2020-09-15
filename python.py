# legend_of_legaia_hackguide

#Legend of Legaia (c) Contrail, 1999
#
#Save State Hacking Guide
#Copyright 2009 Carlos Eugenio
#
#******************************************************************************
#   This guide is licensed under the Creative Commons Attribution-Sharealike,
#avaiable here http://creativecommons.org/licenses/by-sa/2.0/legalcode. 
#Simplifying the legalese, that means that you are free to copy, print, 
#distribute, and otherwise use this guide any way you want as long as you don't
#violate the license i.e. give credit where it is due! :)
#   Derivative works of this guide are allowed provided that you credit me for
#the original work *AND* release it under this same license or other free, 
#copyleft license compatible with Creative Commons Attribution-Sharealike. If
#you indeed produce a derivate, kindly inform me after it's done so I can enjoy
#it too and maybe even improve this guide (you will be credited for it too of
#course!)
#******************************************************************************
#
#Version History
#------------------------------------
#2009 October 4: v. 0.9
#        -First Version of this guide. Still a lot to do, but hey!
#2009 October 6: v. 0.99
#        -Added the money offsets
#        -Tested the save states with the Windows version of ePSXe (it worked)
#        -Corrected inventory starting offset, it was off by 5 positions
#        -Completed ALL lists (items, weapons, etc) 
#        -Added some stuff in section 1.1 Chars Stats Offsets that were missing
#        -"Corrected" my name in the beggining (not everyone uses ISO-8859-1 or
#         Unicode after all)
#        -Changed license terms, this work now licensed under a open license,
#         check it out right above. 
#------------------------------------
#
#        This is a save state hacking guide for Legend of Legaia, a classic 
#PSX RPG by Contrail. Why I bothered writing this stuff for this game you ask.
#I love this game and wanted to play it again but... couldn't bear the thought
#of grinding for hours to level up... and to finally USE Juggernaut!! (must be
#lv 99 to unlock it, talk about GRIND!!). So I loaded my favorite hexeditor, a 
#diff tool, some save states and now I want to share it with you, my dear lazy
#classic RPG gamer. Enjoy :)
#
#PS: This guide won't teach you hex editing. There are plenty of other guides 
#who'll teach you better than me.
#
#PS2: I used ePSXe. State hacking with ePSXe is a bit tricky but I'll explain
#it in detail on section 1.0.
#
#PS3: Use this guide with moderation! You can ruin your fun if you go overboard
#and max out everything. In fact, I recommend that you beat the game first
#without cheating, and in subsequent replays hexedit away. 
#
#And, before anyone bug me with annoying accusations, I played on a emulator
#yes, but I DO OWN a copy of this game!
#
#Well, on to the guide...
#
#
#
#Index
#1.0 Save state?
#1.1 Chars stats offsets
#   1.1.1 Vahn
#   1.1.2 Noa
#   1.1.3 Gala
#1.2 Money
#1.3 Items
#1.4 Lists
#   1.4.1 Items
#   1.4.2 Weapons
#      1.4.2.1 Ra-Seru Weapons (?!) 
#      1.4.2.2 "Normal" Weapons
#   1.4.3 Armors
#   1.4.4 Helmets
#   1.4.5 Boots
#   1.4.6 Relics
#   1.4.7 Miscellaneous
#1.5 Thanks & contact info
#
#
#1.0 Save state?
#        Save state is a file with a snapshot of the game progress on a given
#instant. More specifically, its the CPU & Memory data on a given instant. This
#guide was made and tested on ePSXe for Linux (stated above, before the index).
#I guess that the files structure are the same on Linux and Windows but I cannot
#be certain, since I can't and won't install Windows EVER AGAIN :P
#EDIT: in fact the save states works in both versions. Just tested the Windows
#version using wine. (and, surprise! running the Windows version via wine is way
#better than playing the native Linux version. Go figure...)
#
#        As I said earlier it takes some effort to hack the states. First thing,
#ePSXe save states are compressed using gzip, so before you edit anything at all
#you must decompress it (used gunzip but I guess 7-Zip, WinRAR, etc should do the
#trick on Windows). Then you load the file on your hexeditor, edit whatever you
#want, then recompress the file. Remember to remove any file extension that gets 
#added to the recompressed file, if any. Now you can load the save state on the 
#emulator. A word of warning, it seems that ePSXe somehow keeps the save state 
#in memory, so to edit it you must close it before. Phew! I said it was tricky :)
#It would be a lot easier to edit the memory card if I found out how the game
#calculates the CRC of the saved game, if anyone find this out mail me please!
#
#So, to be clearer, that's how I do it myself:
#$ mv SCUS_942.54.001 SCUS_942.54.001.gz
#$ gunzip SCUS_942.54.001.gz             #decompressing the file
#$ bless SCUS_942.54.001                 #loading on the hexeditor
#$ gzip SCUS_942.54.001                  #done editing, recompressing it
#$ mv SCUS_942.54.001.gz SCUS_942.54.001 #removing file extension
#$ cd ..
#$ ./epsxe                               #play away
#
#        BACKUP YOUR FILES before you edit them to save yourself a lot of grief
#in case something goes wrong! Saving in two or more slots and editing one does
#the trick neatly.
#
#1.1 Chars stats offsets
#
#        All stats values are reversed (i.e second offset is the 'start'). 
#Suppose you want to set Vahn's Max HP to 500 (0x1F4). Then, you need to fill 
#'F4' in offset 0x849C6 and '01' in offset 0x849C7. Got it?
#
#1.1.1. Vahn
#name (starting offset): 0x84B69
#Level: 0x849F2
#EXP: 0x
#AP: 0x
#HP  (max/current):        0x849C6 - 0x849C7   /   0x849C8 - 0x849C9
#HP  (unequipped value):   0x849DE - 0x849DF
#MP  (max/current):        0x849CA - 0x849CB   /   0x849CC - 0x849CD
#MP  (unequipped value):   0x849E0 - 0x849E1
#AGL (current/unequipped): 0x849D2 - 0x849D3   /   0x849E4 - 0x849E5
#ATK (current/unequipped): 0x849D4 - 0x849D5   /   0x849E6 - 0x849E7
#UDF (current/unequipped): 0x849D6 - 0x849D7   /   0x849E8 - 0x849E9
#LDF (current/unequipped): 0x849D8 - 0x849D9   /   0x849EA - 0x849EB
#SPD (current/unequipped): 0x849DA - 0x849DB   /   0x849EC - 0x849ED
#INT (current/unequipped): 0x849DC - 0x849DD   /   0x849EE - 0x849EF
#
#Magic
#<TODO I kinda found the offsets but I'm lazy right now, when I figure out how 
#to edit them I will update the guide. C'mon you can live without it :P hehe>
#
#Moves 
## of moves learned: 0x84A47 
#Insert the moves you want right after the move counter offset. The game will 
#show them in the order you put them in the list! Neat, huh? Rearrange them
#the way you want!
#To have all insert this: 01020304050607080900A0B0C0D0E0F
#Miracle Arts seems to be activated after story event and won't show on the list
#until then (maybe I'm mistaken since its been so long I played the game, email
#me if you find this out).
#
#Hyper Elbow:    0x0E         Charging Scorch:0x0D
#Somersault:     0x0C         Slash Kick:     0x0B
#Power Punch:    0x0A         Cross-Kick:     0x09
#Pyro Pummel:    0x08         Spin Combo:     0x07
#PK Combo:       0x06         Hurricane:      0x05
#Cyclone:        0x04         Tornado Flame:  0x03
#Fire Blow:      0x02         Burning Flare:  0x01
#
#1.1.2 Noa
#name (starting offset): 0x84F7D
#Level: 0x84E06
#EXP: 0x
#AP: 0x
#HP  (max/current):        0x84DDA - 0x84DDB   /   0x849C8 - 0x849C9
#HP  (unequipped value):   0x84DF2 - 0x84DF3
#MP  (max/current):        0x84DDE - 0x84DDF   /   0x84DE0 - 0x84DE1
#MP  (unequipped value):   0x84DF4 - 0x84DF5
#AGL (current/unequipped): 0x84DE6 - 0x84DE7   /   0x84DF8 - 0x84DF9
#ATK (current/unequipped): 0x84DE8 - 0x84DE9   /   0x84DFA - 0x84DFB
#UDF (current/unequipped): 0x84DEA - 0x84DEB   /   0x84DFC - 0x84DFD
#LDF (current/unequipped): 0x84DEC - 0x84DED   /   0x84DFE - 0x84DFF
#SPD (current/unequipped): 0x84DEE - 0x84DEF   /   0x84E00 - 0x84E01
#INT (current/unequipped): 0x84DF0 - 0x84DF1   /   0x84E02 - 0x84E03
#
#Magic
#<TODO same deal will write them later>
#Moves 
## of moves learned: 0x84E5B
#All moves: 01020304050607080900A0B0C0D0E0F
#
#Lizard Tail:    
#Acrobatic Blitz:
#Sonic Javelin:  
#Blizzard Bash:  
#Mirage Lancer:  
#Dolphin Attack: 
#Bird Step:      
#Swan Diver:    
#Tough Love:  
#Rushing Gale:  
#Tempest Break: 
#Frost Breath:  
#Vulture Blade: 
#Hurricane Kick:
#
#1.1.3 Gala
#name (starting offset): 0x85391
#Level: 0x849F2
#EXP: 0x
#AP: 0x
#HP  (max/current):        0x851EE - 0x851EF   /   0x851F0 - 0x851F1
#HP  (unequipped value):   0x85206 - 0x85207
#MP  (max/current):        0x851F2 - 0x851F3   /   0x851F4 - 0x851F5
#MP  (unequipped value):   0x85208 - 0x85209
#AGL (current/unequipped): 0x851FA - 0x851FB   /   0x8520C - 0x84DF9
#ATK (current/unequipped): 0x851FC - 0x851FD   /   0x8520E - 0x8520F
#UDF (current/unequipped): 0x851FE - 0x851FF   /   0x85210 - 0x85211
#LDF (current/unequipped): 0x85200 - 0x85201   /   0x85212 - 0x85213
#SPD (current/unequipped): 0x85202 - 0x85203   /   0x85214 - 0x85215
#INT (current/unequipped): 0x85204 - 0x85205   /   0x85216 - 0x85217
#
#Magic
#<TODO same deal will write them later>
#Moves 
## of moves learned: 0x
#All moves: 01020304050607080900A0B0C0D0E0F
#
#Flying Knee Attack:
#Battering Ram:     
#Ironhead:          
#Back Punch:        
#Guillotine:       
#Head-Splitter:
#Side Kick:  
#Black Rain: 
#Neo Raising: 
#Electro Thrash: 
#Bull Horns:  
#Thunder Punch: 
#Lightning Storm: 
#Explosive Fist: 
#
#1.2 Money
#
#        Money works like stats, which means values are in reverse order. For 
#example, you decide to become filthy rich and give yourself 500,000G (0x7A120).
#Put '07' in the third byte, 'A1' in the second and '20' in the first and you're
#good to go.
#
#Money offsets: 0x84756, 0x84757, 0x84758
#
#1.3 Items
#
#        Items are stored using two bytes, one identifies the item, the other 
#says the quantity you have, ex. '78 0E' means '14 Healing Flowers'. Refer to
#next section for valid values to enter here. Maybe it goes without saying but
#in this game everything belongs on the same inventory (weapons, items, etc) so
#it can get quite large, I haven't tested how big it can be. If anyone out there
#discover this mail me please so I can update this info!
#
#Inventory offset (start): 0x85B12
#
#1.4 Lists
#
#This section is still work in progress. I plan to play through the game, 
#acquiring everything, and updating the list as I go but you can help by sending
#me the remaining items and testing other values, etc. if you don't want to wait
#(won't take that long anyway, maybe a week or two, but who knows I'm a busy man
#and can drop gaming if work or something else requires it...)
#
#EDIT: I decided to test all possible values, in case I miss something in my
#gameplay. Note that the game auto-rearranges the inventory so some values
#may be off. As I said before, feel free to correct me if you find any errors :D
#
#1.4.1 Items
#
#0x65 Honey                 0x82 Life Water            0x8F Fire Book I
#0x6D Miracle Water         0x83 Power Water           0x90 Fire Book II
#0x77 Healing Leaf          0x84 Guardian Water        0x91 Fire Book III
#0x78 Healing Flower        0x85 Swift Water           0x92 Wind Book I
#0x79 Healing Berry         0x86 Wisdom Water          0x93 Wind Book II
#0x7A Healing Bloom         0x87 Magic Water           0x94 Wind Book III
#0x7B Healing Fruit         0x88 Door of Light         0x95 Thunder Book I
#0x7C Magic Leaf            0x89 Door of Wind          0x96 Thunder Book II
#0x7D Magic Fruit           0x8A Incense               0x97 Thunder Book III
#0x7E Antidote              0x8B Power Elixir          0x98 Lippian Flute
#0x7F Medicine              0x8C Shield Elixir         0x99 Spikefish Flute
#0x80 Phoenix               0x8D Speed Elixir          0xA3 Healing Shroom
#0x81 Fury Boost            0x8E Wonder Elixir
#
#1.4.2 Weapons
#
#1.4.2.1 Ra-Seru Weapons (?!) 
#
#What? Why the Ra-Seru are listed here?! If you remember, everytime you save
#a Genesis Tree your chars gets stronger, yes that's how it was implemented...
#(save a tree and the game automatically upgrades your Ra-Seru "weapons" to the
#next level). But you can have two Ra-Seru equipped now, thanks to me!! :D
#They don't get displayed on battle though... Just imagine having two Meta lv.9
#by the end of the game! Oh well...
#
#0x01 Ra-Seru Meta lv. 1    0x0A Ra-Seru Terra lv. 1   0x13 Ra-Seru Ozma lv. 1
#0x02 Ra-Seru Meta lv. 2    0x0B Ra-Seru Terra lv. 2   0x14 Ra-Seru Ozma lv. 2
#0x03 Ra-Seru Meta lv. 3    0x0C Ra-Seru Terra lv. 3   0x15 Ra-Seru Ozma lv. 3
#0x04 Ra-Seru Meta lv. 4    0x0D Ra-Seru Terra lv. 4   0x16 Ra-Seru Ozma lv. 4
#0x05 Ra-Seru Meta lv. 5    0x0E Ra-Seru Terra lv. 5   0x17 Ra-Seru Ozma lv. 5
#0x06 Ra-Seru Meta lv. 6    0x0F Ra-Seru Terra lv. 6   0x18 Ra-Seru Ozma lv. 6
#0x07 Ra-Seru Meta lv. 7    0x10 Ra-Seru Terra lv. 7   0x19 Ra-Seru Ozma lv. 7
#0x08 Ra-Seru Meta lv. 8    0x11 Ra-Seru Terra lv. 8
#0x09 Ra-Seru Meta lv. 9    0x12 <empty wp. for Noa>
#
#1.4.2.2 "Normal" Weapons
#
#0x1A Vahn Fist             0x23 Battle Knife          0x2C Holy Claw
#0x1B Ra-Seru Blade         0x24 Short Sword           0x2D Golden Claw
#0x1C Noa Feral             0x25 Force Blade           0x2E Survival Club
#0x1D Hard Beat             0x26 Beast Buster          0x2F Red Club
#0x1E Heavy Strike          0x27 Chaos Breaker         0x30 Power Club
#0x1F Ra-Seru Fangs         0x28 Nail Glove            0x31 Survival Axe
#0x20 Gala Mace             0x29 Crimson Nails         0x32 Battle Axe
#0x21 Ra-Seru Club          0x2A Fighter Claw          0x33 Great Axe
#0x22 Survival Knife        0x2B Bloody Claw           0x52 <empty wp. for Vahn>
#0xBA Astral Sword
#
#1.4.3 Armors
#
#0x43 Hunter's Clothes      0x4A Triumph Armor         0x51 Ra-Seru Robe
#0x44 Savior Clothes        0x4B Ra-Seru Armor         0x53 Power Plate
#0x45 Warrior Armor         0x4C Fighting Robe         0x54 Fighting Plate
#0x46 Ironman Armor         0x4D Green Robe            0x55 Valor Plate
#0x47 Master Armor          0x4E Scarlet Robe          0x56 War God Plate
#0x48 Expert Armor          0x4F Tempest Robe          0x57 Ra-Seru Plate
#0x49 Hero Armor            0x50 Battle Robe
#
#1.4.4 Helmets
#
#0x34 Warrior Seal          0x39 Guardian Clip         0x3E Ra-Seru Plume
#0x35 Ironman Seal          0x3A Green Clip            0x3F Power Earring
#0x36 Expert Seal           0x3B Jeweled Clip          0x40 Fighter's Band
#0x37 Hero Seal             0x3C Royal Crown           0x41 War God Band
#0x38 Ra-Seru Seal          0x3D Pronged Crown         0x42 Ra-Seru Helmet
#
#1.4.5 Boots
#
#0x58 Warrior Boots         0x5E Ra-Seru Boots         0x64 Ra-Seru Shoes
#0x59 Ironman Boots         0x5F Eletric Shoes         0x66 Power Shoes
#0x5A Master Boots          0x60 Tempest Shoes         0x67 Fighting Boots
#0x5B Expert Boots          0x61 Tempest Shoes         0x68 War God Boots
#0x5C Hero Boots            0x62 Olive Shoes           0x69 Ra-Seru Thongs
#0x5D Triumph Boots         0x63 Steel Boots
#
#1.4.6 Relics
#
#Note that some equippable relics are also story items, in this case they get
#listed on the next section instead of here, ok?
#
#0x6E Earth Egg             0xCF Warrior Icon          0xE8 Mettle Ring
#0x6F Water Egg             0xD0 Evil God Icon         0xE9 Mettle Armband
#0x70 Light Egg             0xD1 Speed Chain           0xEA Mettle Goblet
#0x71 Dark Stone            0xD2 Slowness Chain        0xEB Mettle Gem
#0x72 Earth Talisman        0xD3 Target Chain          0xEC War Soul
#0x73 Earth Talisman        0xD4 Defender Chain        0xED Evil Medallion
#0x74 Water Talisman        0xD5 Guardian Chain        0xEE Ivory Book
#0x75 Light Talisman        0xD6 Cure Amulet           0xEF Crimson Book
#0x76 Dark Talisman         0xD7 Pure Amulet           0xF0 Bronze Book
#0x77 Evil Talisman         0xD8 Forest Amulet         0xF1 Golden Compass
#0xC0 Life Ring             0xD9 Magic Amulet          0xF2 Silver Compass
#0xC1 Life Armband          0xDA Stone Amulet          0xF3 Chicken Heart
#0xC2 Magic Ring            0xDB Nature Amulet         0xF4 Chicken Safe
#0xC3 Magic Armband         0xDC Wonder Amulet         0xF5 Chicken Guard
#0xC4 Spirit Jewel          0xDD Earth Jewel           0xF6 Chicken King
#0xC5 Spirit Talisman       0xDE Deep Sea Jewel        0xF7 Life Source
#0xC6 Power Ring            0xDF Burning Jewel         0xF9 Magic Source
#0xC7 Scarlet Jewel         0xE0 Tempest Jewel         0xFA Mettle Source
#0xC8 Azure Jewel           0xE1 Madlight Jewel        0xFB Bad Luck Bell
#0xC9 Guardian Ring         0xE2 Luminous Jewel        0xFC Good Luck Bell
#0xCA Speed Ring            0xE3 Ebony Jewel           0xFD <unnamed item>
#0xCB Wisdom Ring           0xE4 Rainbow Jewel         0xFE Point Card
#0xCC Vitality Ring         0xE5 Life Grail            0xFF Platinum Card
#0xCD War God Icon          0xE6 Magic Grail 
#0xCE Unholy Icon           0xE7 Lost Grail
#
#1.4.7 Miscellaneous
#
#0x6A Zalan's Letter        0xA5 Lightning Key         0xB2 Soru Bread
#0x6B Something Good(!?)    0xA6 Star Key              0xB3 Letona Key
#0x6C Minea's Ring          0xA7 Mountain Key          0xB4 West Ratayu Key
#0x9A Mary's Diary          0xA8 Water Key             0xB5 Nemesis Gem
#0x9B Soren's Secrets       0xA9 Fertilizer            0xB6 Seru Flame
#0x9C Gold Card             0xAA Weed Hammer           0xB7 Genesis Seedling
#0x9D Light Lure            0xAB Ra-Seru Egg           0xB8 Soren Flute
#0x9E Normal Lure           0xAC Mei's Pendant         0xB9 <invalid item>
#0x9F Heavy Lure            0xAD Camera Stone          0xBB Music Score
#0xA0 Old Rod               0xAE Star Pearl            0xBC Fire Droplet
#0xA1 Deluxe Rod            0xAF Yuma's Ring           0xBD Ruins Key
#0xA2 Legendary Rod         0xB0 Spring Salts          0xBE TimeSpace Bomb
#0xA4 Sunrise Key           0xB1 Zalan's Crown         0xBF Evil Seru Key
#
#
#1.5 Thanks & contact info
#
#-Thanks to Contrail, for this wonderful game, I enjoy it to this day!
#-Thanks to the free & open source software people!
#-Thanks to the GameFAQs people!
#-Thanks to anyone who deserves a thanks but I forgot to mention!
#
#You can reach me on demonsword at gmail dot com. Please, if you want to mail
#me, write in proper English so I can understand you. Offensive mails won't 
#get replied. And please, I'm a busy man, so if I don't reply to you the same
#day/month/year/century please don't be mad at me ok? :)
#
#---EOF
