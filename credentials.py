def confirm(value=""):
    while True:
        print("Is this the correct input? (y/n): "+value)
        confirm = input()
        if confirm == "y" or confirm =="Y":
            print("Saved.")
            print("-------")
            return True
        elif confirm == "n" or confirm =="N":
            print("Discarded.")
            print("-------")
            return False
        else:
            print("Enter y or n.")

while True: #asks for the discord username
    print("Enter Discord username:")
    discordUsername = input()
    if (confirm(discordUsername)==True):
        break

while True: #asks for the discord password
    print("Enter Discord password:")
    discordPassword = input()
    if (confirm(discordPassword)==True):
        break

while True: #asks for the instagram username
    print("Enter Instagram username:")
    InstagramUsername = input()
    if (confirm(InstagramUsername)==True):
        break

while True: #asks for the instagram password
    print("Enter Instagram password:")
    InstagramPassword = input()
    if (confirm(InstagramPassword)==True):
        break

while True: #final confirmation
    print("Discord username: "+discordUsername)
    print("Discord password: "+discordPassword)
    print("Instagram username: "+InstagramUsername)
    print("Instagram password: "+InstagramPassword)
    if (confirm()==True):
        break

#saves the credentials to a file
file = open("info.txt","w")
file.write(discordUsername+"\n")
file.write(discordPassword+"\n")
file.write(InstagramUsername+"\n")
file.write(InstagramPassword)
file.close()

