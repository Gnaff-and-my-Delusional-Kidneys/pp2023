import subprocess
def main():
    while True:
        cmd = input('shell> ')
        if cmd == 'exit':
            break
        try:
            output = subprocess.check_output(cmd, shell=True)
            print(output.decode('utf-8'))
        except Exception as x:
            print(x)
if __name__ == '__main__':
    main()