import os, sys

port = 8080
if len(sys.argv) > 1:
    try:
        port = int(sys.argv[1])
    except ValueError:
        print(f'USAGE: {os.path.basename(sys.argv[0])} [<port>]\n<port> will default to 8080')
        sys.exit(1)

if not os.path.exists('site'):
    print("Build the site first! (run build.bat)")
    sys.exit(1)

os.chdir('site')
os.system(f'start cmd.exe /c {sys.executable} -m http.server {port}')
os.system(f'start http://127.0.0.1:{port}')
