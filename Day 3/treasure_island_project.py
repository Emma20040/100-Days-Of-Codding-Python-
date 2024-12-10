# ASCII arts
print('''

                         _____
         .-~---..._--~~~~     ~~~~---..__
        /       .  ~~-._                 ~-.
       /            .   |                   Y
       |        .       |                    \
       |  O        .   .|                     K
       |         .   . /                      |\
       /       Y       |                      | \_
      (   ( /  |.  .  /                       | ()\   .-~~-.-~-.___
      (   |/-^.\     |             :          j  \ \ /    /    Y   ~~-.
      /  /     \\___/    :          :        ."   | || o       !       \
     (  )       `\       j           :       |    \ \j         |        k
     (  )        |      /_        ___.Y      :     \__.   |   /         j\
     j  j        /    ."  ~~---~~~ /   \     \         ~~\\__/   :      !
  __/  /        /    / \    ".    /    .`\    ".         /".   Y__Y   ."\
  >__.~        |    |   `\    \  |    /   `\    \       /  /\  |  (  /\  \
               [nn  ]     [nn  ] [nn  ]     [nn  ]     [n ] [n ]  [n ] [n ]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      ''')

print("Welcome to treasure island\n your mission is to find the treasure ")
direction= input("left or right? ").lower()
if direction=="left":
    swin_wait=input("swim or wait? ").lower()
    if swin_wait=="wait":
        door=input("which door? ").lower()
        if door=="blue" or door=="red":
            print("game over")
        elif door=="yellow":
            print("you win!!!")
        else:
            print("you loss")
        
    else:
        print("game over")

else:
    print("Game over")