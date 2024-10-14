#Py-Fortify
#!/usr/bin/env python
# coding: utf-8
# By Ishan Oshada : https://github.com/Ishanoshada/Py-Fortify
#1:36 AM 23/6/26



import marshal,base64,gzip,zlib,bz2,lzma,binascii,codecs,os,random,argparse,string ,subprocess
try:
    import python_minifier
except:
       
    os.system("pip install python_minifier")
    print("\x1b[1m\x1b[92m" + "[+] dependencs installed")
    import python_minifier
try:
    import pyfiglet
except:
    os.system("pip install pyfiglet")
    print("\x1b[1m\x1b[92m" + "[+] dependencs installed")
    import pyfiglet
try:
    import requests
except:
    os.system("pip install requests")
    print("\x1b[1m\x1b[92m" + "[+] dependencs installed")
    import requests
try:
    import colorama
except:
    
    os.system("pip install colorama")
    print("\x1b[1m\x1b[92m" + "[+] dependencs installed")
    colorama
try:
    import tqdm
except:
    os.system("pip install tqdm")     
    print("\x1b[1m\x1b[92m" + "[+] dependencs installed")
    import tqdm
    
import time,sys

###################################

_name_ = "Py-Fortify"
class bc:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    YELLOW = '\033[1;33m'
    RED= '\033[1;31m'
    WHITE= '\033[0m' 
    UNDERLINE = '\033[4m'  
    
bcolors = ['\033[95m'
    '\033[94m',
     '\033[96m',
     '\033[92m',
     '\033[93m',
     '\033[91m',
    
     '\033[1;33m',
     '\033[1;31m',
     ]     
FONTS = (
    "basic",
    "o8",
    "cosmic",
    "graffiti",
    "chunky",
    "epic",
    "poison",
    "doom",
    "avatar",
    "3-d",
    "alligator2",
    "banner3-D",
    "block",
    "bubble",
    "digital",
    "doh",
    "doom",
    "epic",
    "fuzzy",
    "isometric1",
    "letters",
    "nancyj-fancy",
    "ogre",
    "poison",
    "roman",
    "shadow",
    "starwars",
    "stop",
    "univers",
    "usaflag",
)

##################################


def m1(code):
     try:
          code = code.encode()
     except:
          code = code
     en = gzip.compress(marshal.dumps(compile(code,_name_,"exec")))
     output = "import base64,marshal,binascii,gzip,zlib\n"

     output += f"#Encoded by {_name_}\n"
     output += "try:\n"
     output += f"\texec(marshal.loads(gzip.decompress({en})))\n"
     output += "except Exception as b:\n\tprint(f'Error by {b} ')"
     return  output


def m2(data):
     en = lzma.compress(base64.b64encode(marshal.dumps(compile(data,_name_,"exec"))))
     return f"import marshal,base64\nexec(marshal.loads(base64.b64decode(lzma.decompress({en}))))"
     
     
def m3(data):
     _name_ = "Py-Fortify"
    
     en = lzma.compress(base64.b85encode(marshal.dumps(compile(data,_name_,"exec"))))
     return    f"import marshal,base64\nexec(marshal.loads(base64.b85decode(lzma.decompress({en}))))"
     


def m4(data):
     _name_ = "Py-Fortify"
     en = lzma.compress(marshal.dumps(compile(data,_name_,"exec")))
     output = f"#Encoded by {_name_}\n"
   
     output += "import binascii,lzma,base64,marshal,gzip,zlib\n"
     output += f"\ntry:\n\t\texec(marshal.loads(lzma.decompress({en})))\n\n\nexcept Exception as b:\n\n\t\t"+"print(f'\\n\\n\tError to : {b}\\n\\n ')"
     return  output


def m5(data):
     
     en = base64.b64encode(lzma.compress(marshal.dumps(compile(data,_name_,"exec"))))
     return    f"import marshal,lzma\nexec(marshal.loads(lzma.decompress(base64.b64decode({en}))))"
     
def  m6(data):
     _name_ = "Py-Fortify"
     
     en = lzma.compress(zlib.compress(marshal.dumps(compile(data,_name_,"exec"))))
     return  f"import marshal,zlib,lzma\nexec(marshal.loads(zlib.decompress(lzma.decompress({en}))))"

def m7(data):
     _name_ = "Py-Fortify"
     
     en = lzma.compress(gzip.compress(marshal.dumps(compile(data,_name_,"exec"))))
     return    f"import marshal,gzip\nexec(marshal.loads(gzip.decompress(lzma.decompress({en}))))"

def m8(data):
     
     en = lzma.compress(marshal.dumps(compile(data,_name_,"exec")))
     return    f"import marshal\nexec(marshal.loads(lzma.decompress({en})))"

def m9(code):
        _name_ = "Py-Fortify"
        en  = base64.b64encode(gzip.compress(marshal.dumps(compile(code,_name_,"exec"))))
        output = f"#ENCODED BY {_name_} \n#you can try this decode\n"
        #output += "#https://github.com/Ishanoshada/Py-Fortify"
        output += "import marshal,base64,gzip,zlib,bz2,lzma\n"
        output += f"exec(marshal.loads(gzip.decompress(base64.b64decode({en}))))"
        return output
       
def m10(code):
     
# code = python_minifier.minify(code)
 code1 = compile(code,_name_,'exec')
 en = base64.b64encode(gzip.compress(marshal.dumps(code1)))
 return f"import marshal,base64,gzip,lzma;exec(marshal.loads(gzip.decompress(base64.b64decode({en}))))"

def m11(code):
     
     try:
      code = code.encode()
     except:
        code = code
     finally:
        en  = base64.b64encode(gzip.compress(marshal.dumps(compile(code,_name_,"exec"))))
        output = f"#ENCODED BY {_name_} \n#you can try this decode\n"
        output += "#https://github.com/Ishanoshada/Py-Fortify\n"
        output += "import marshal,base64,gzip,zlib,bz2,lzma\n"
        output += f"exec(marshal.loads(gzip.decompress(base64.b64decode({en}))))"
     return output



def m20(code):
        data= python_minifier.minify(code).encode()
        en  = base64.b64encode(gzip.compress(marshal.dumps(compile(code,_name_,"exec"))))
        
        output = "#https://github.com/Ishanoshada/Py-Fortify\n"
        output += f"#ENCODED BY {_name_} \n#you can try this decode\n"
        output += "import marshal,base64,gzip,zlib,bz2,lzma\n"
        output += f"exec(marshal.loads(gzip.decompress(base64.b64decode({en}))))"
        return output



def l1(data,line):
     output = "import marshal,base64,lzma,gzip,zlib,binascii\n"
     output += "#https://github.com/Ishanoshada/Py-Fortify\n"
     for i in range(line):
          if int(line/2) == i:
             en = gzip.compress(base64.b85encode(marshal.dumps(data)))
             output += f"exec(marshal.loads(base64.b85decode(gzip.decompress({en}))));"
          else:
               da = f"#{base64.b85encode(lzma.compress(data.encode())).decode()}"
               en = gzip.compress(base64.b85encode(marshal.dumps(da)))
               output += f"exec(marshal.loads(base64.b85decode(gzip.decompress({en}))));"

     return  output          


def l2(data,line):
     output = "import marshal,base64,lzma,gzip,zlib,binascii\n"
     output += "#https://github.com/Ishanoshada/Py-Fortify\n"
     for i in range(line):
          if int(line/2) == i:
             en = lzma.compress(gzip.compress(base64.b85encode(marshal.dumps(data))))
             output += f"exec(marshal.loads(base64.b85decode(gzip.decompress(lzma.decompress({en})))));"
          else:
               da = f"#{base64.b85encode(lzma.compress(data.encode())).decode()}"
               en = lzma.compress(gzip.compress(base64.b85encode(marshal.dumps(da))))
               output += f"exec(marshal.loads(base64.b85decode(gzip.decompress(lzma.decompress({en})))));"

     return  output        


def l3(code,n:int):
    try:
        code = code.encode()
    except:
        code =code
    output = f"#ENCODE BY{_name_} \n#you can try this decode\n"
    output += "#https://github.com/Ishanoshada/Py-Fortify\n"
    output += "import marshal,base64,gzip,zlib,bz2\n"
    for i in range(n):
        en  = base64.b64encode(gzip.compress(marshal.dumps(f"#{bz2.compress(base64.b64encode(code))}")))
        output += f"exec(marshal.loads(gzip.decompress(base64.b64decode({en}))));"
        if int(i/2) == i:
          en =   base64.b64encode(gzip.compress(marshal.dumps(code)))
          output += f"exec(marshal.loads(gzip.decompress(base64.b64decode({en}))));"
    return output

def l4(code,n:int):
    try:
        code = code.encode()
    except:
        code =code
    output = f"#ENCODED BY {_name_} \n#you can try this decode\n"
    output += "#https://github.com/Ishanoshada/Py-Fortify\n"
    output += "import marshal,base64,gzip,zlib,bz2,lzma\n"
    for i in range(n):
        en  = base64.b64encode(gzip.compress(marshal.dumps(compile(f"#{bz2.compress(base64.b64encode(marshal.dumps(code)))}",_name_,"exec"))))
        output += f"exec(marshal.loads(gzip.decompress(base64.b64decode({en}))));"
        if int(i/2) == i:
          en =   base64.b64encode(gzip.compress(marshal.dumps(compile(code,_name_,"exec"))))
          output += f"exec(marshal.loads(gzip.decompress(base64.b64decode({en}))));"
    return output

def l5(code, n: int):
    _name_ = "Py-Fortify"
    try:
        code = code.encode()
    except:
        code = code
    output = f"#ENCODED BY {_name_} \n#you can try this decode\n"
    output += "#https://github.com/Ishanoshada/Py-Fortify\n"
    output += "import marshal, base64,lzma\n"
    for i in range(n):
        en = base64.a85encode(marshal.dumps(compile(f"#{base64.a85encode(marshal.dumps(code)).decode()}", _name_, 'exec'))).decode()
        output += f'exec(marshal.loads(base64.a85decode("""{en}""")))\n'
        if int(i / 2) == i:
            en = base64.a85encode(marshal.dumps(compile(code, _name_, 'exec'))).decode()
            output += f'exec(marshal.loads(base64.a85decode("""{en}""")))\n'
    return output


def l6(code, n: int):
    _name_ = "Py-Fortify"
    try:
        code = code.encode()
    except:
        code = code
    output = f"#ENCODED BY {_name_} \n#you can try this decode\n"
    output += "#https://github.com/Ishanoshada/Py-Fortify\n"
    output += "import marshal, base64, codecs\n"
    for i in range(n):
        en = base64.b64encode(marshal.dumps(compile(f"#codecs.encode({code}, 'rot_13').decode()", _name_, 'exec'))).decode()
        output += f'exec(marshal.loads(base64.b64decode("""{en}""")))\n'
        if int(i / 2) == i:
            en = base64.b64encode(marshal.dumps(compile(code, _name_, 'exec'))).decode()
            output += f'exec(marshal.loads(base64.b64decode("""{en}""")))\n'
    return output


def xor_encrypt(data, key):
    key = key.encode()
    encrypted = bytearray()
    for i in range(len(data)):
        encrypted.append(data[i] ^ key[i % len(key)])
    return encrypted

def l7(code, n: int):
    try:
        code = code.encode()
    except:
        code = code
    output = f"#ENCODED BY {_name_} \n#you can try this decode\n"
    output += "#https://github.com/Ishanoshada/Py-Fortify\n"
    output += "import marshal, base64\n"
    for i in range(n):
        en = base64.b64encode(xor_encrypt(marshal.dumps(compile(f"#{base64.b64encode(xor_encrypt(marshal.dumps(code), 'ishh')).decode()}", _name_, 'exec')), 'ishh')).decode()
        output += f'exec(marshal.loads(xor_encrypt(base64.b64decode("""{en}"""), "ishh")))\n'
        if int(i / 2) == i:
            en = base64.b64encode(xor_encrypt(marshal.dumps(compile(code, _name_, 'exec')), 'ishh')).decode()
            output += f'exec(marshal.loads(xor_encrypt(base64.b64decode("""{en}"""), "ishh")))\n'
    return output


###################################



colorama.init(autoreset=True)


def printf(text):
    return text.title().center(os.get_terminal_size().columns)

# Initialize current version
CURRENT_VERSION = "2"  # Update this to your current version

# URL for the version file
VERSION_URL = "https://raw.githubusercontent.com/Ishanoshada/Py-Fortify/master/.version"
# URL for the main script file
SCRIPT_URL = "https://raw.githubusercontent.com/Ishanoshada/Py-Fortify/master/py_fortify.py"




def update():
    """Checks for updates and updates the script if a new version is available."""
    try:
        # Get the latest version from the version file
        latest_version = requests.get(VERSION_URL).text.strip()
        print(f"Current version: {CURRENT_VERSION}, Latest version: {latest_version}")

        # Compare versions
        if int(latest_version) > int(CURRENT_VERSION):
            print("A new version is available. Updating...")
            # Download the latest script
            r = requests.get(SCRIPT_URL)
            with open('py_fortify.py', 'wb') as f:
                f.write(r.content)
            print("Updated successfully to version " + latest_version)
            print("You can run this again")
            sys.exit(1)
        else:
            print("You are running the latest version.")
    except Exception as e:
        print(f"Error in update: {e}")

def logo():
    font = random.choice(FONTS)
    color1 = random.choice(bcolors)
    color2 = random.choice(bcolors)
    while color1 == color2:
        color2 = random.choice(bcolors)
    print(color1 + "•" * os.get_terminal_size().columns, end="\n" * 2)
    print(
        color2
        + pyfiglet.figlet_format(
            "Py\nFortify",
            width=os.get_terminal_size().columns,
            justify="center",
            font=font,
        ),
        end="",
    )
    print(color1 + "•" * os.get_terminal_size().columns, end="\n" * 2)


def parse_args():
    parser = argparse.ArgumentParser(description="obfuscate python programs".title())
    parser._optionals.title = "syntax".title()
    parser.add_argument(
        "-i", "--input", type=str, help="input file name".title(), required=True
    )
    parser.add_argument(
        "-o", "--output", type=str, help="output file name".title(), required=True
    )
    parser.add_argument(
        "-e", "--exec", type=str, help="block -i/ interactive (-e 1)".title(), required=False
    )
    
    parser.add_argument(
        "-m", "--method", type=str, help=" 1: high  encode method is used/ 2: Both methods are used at once [2 recommended] ".title(), required=True
    )
    
    parser.add_argument(
        "-c",
        "--complexity",
        type=int,
        help="complexity of obfuscation. 50 recommended".title(),
        required=True,
    )
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    return parser.parse_args()


def m_encoded(data):
    m_func = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11]
    
    method = random.choice(m_func)
    
    return method(data)
    

def l_encoded(data,x):
    l_func = [l1,l2,l3,l4,l6,l7]
    method = random.choice(l_func)
    
    return method(data,x)

###################################

def main():
    logo()
    args = parse_args()
    print(bc.OKCYAN)
    if check_update():
        print(bc.WARNING+ prinf("[!] update available"))
        print(bc.OKBLUE + printf("[•] updating..."))
        update()
        print(bc.OKBLUE + printf("[•] successfully updated..."))
        sys.exit(bc.OKCYAN + printf("run the program again"))
    print(random.choice(bcolors) + "\t[•] encoding ".title() + args.input)
    
    with tqdm.tqdm(total=args.complexity, bar_format=colorama.Style.BRIGHT + '{l_bar}' +
          colorama.Fore.CYAN + colorama.Back.WHITE + '{bar}' + colorama.Style.RESET_ALL +
          colorama.Fore.CYAN + '| {n_fmt}/{total_fmt}' + colorama.Style.RESET_ALL) as pbar:
   
        with open(args.input) as file:
                for i in range(args.complexity):
                  if i == 0:
                   
                   output = m20(file.read())
                   if str(args.exec) == "1":
                       output = l6(output)
                   output = l_encoded(output,50)
                  if i == int(int(args.complexity)/2):
                     if str(args.method) == "2":
                      output = l_encoded(output,50)
                  else:
                     output = m_encoded(output)
                  time.sleep(0.1)
                  pbar.update(1)
    fol = str(args.output).replace('.py',' ').replace(" ","")
    a = subprocess.getoutput(f"mkdir {fol} ")
    if "exists" in a:
         pass

    
    with open(fol+"/"+args.output, "w") as out:
        
        output = m20(output)
        out.write(output)
    print("\n\n")
    print((bc.OKCYAN+ f"\t[•] encoding successful!\n\n\tSaved as :- {fol}/".title() + args.output))





if __name__ == "__main__":
    update()
    main()
    


###################################

                                                                                                                                                                                                                                                

                                                                              
