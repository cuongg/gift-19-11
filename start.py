from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from functools import partial
import webbrowser

PORT = 8765
ROOT = Path(__file__).resolve().parent / 'dist'
URL = f'http://127.0.0.1:{PORT}/?61f15939408dab54'
if __name__ == '__main__':
    try:
        server = ThreadingHTTPServer(('127.0.0.1', PORT), partial(SimpleHTTPRequestHandler, directory=str(ROOT)))
    except OSError:
        print(f'Port {PORT} is occupied. Open {URL} if the gift server is already running.')
        raise SystemExit(1)
    print(f'Open {URL}\nPress Ctrl+C to stop.', flush=True)
    webbrowser.open(URL)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
