import os

def create_file(link):
    os.mkdir(link)



def delete_if_exists(link):
    try:
        os.rmdir(link)
    except Exception as e:
        print("file not empty")

def create_file_in_folder(link,f):
    file = os.path.join(link, f)
    os.makedirs(link, exist_ok=True)
    with open(file, 'w') as f:
        f.write("")


def write_to_file(link, str):
    with open(link, 'a') as f:
        f.write(str)


def delete_file(link):
    try:
        os.remove(link)
    except FileNotFoundError:
        print(f"שגיאה: הקובץ '' לא נמצא.")
    except Exception as e:
        print(f"אירעה שגיאה: {e}")

def list_in_folder(link):
   li = os.listdir(link)
   for i in li:
        print(i)


def dir():
    print(os.getcwd())

