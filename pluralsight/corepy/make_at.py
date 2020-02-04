import os

def make_at(path, dir_name):
    original_path = os.getcwd()
    os.chdir(path)
    try:
        os.mkdir(dir_name)
    except OSError as e:
        print(e, file=sys.stderr)
        raise
    finally:
        os.chdir(original_path)

def main():
    make_at("C:\\Users\\abamboi\\Documents\\DevOPS\\Study\\Python\\pluralsight\\corepy", 'kkt')

if __name__ == "__main__":
    main()
