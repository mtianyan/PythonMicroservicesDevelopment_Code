import argparse
import sys
import signal
import os

import jinja2
from chaussette.server import make_server
from werkzeug.serving import run_with_reloader

from .app import create_app


_HERE = os.path.dirname(__file__)
_SETTINGS = os.path.join(_HERE, '..', '..', 'settings.ini')
_TMPL_DIR = os.path.join(_HERE, 'templates')
_STATIC_FOLDER = os.path.join(_HERE, 'static')


def _quit(signal, frame):
    print("Bye!")
    # add any cleanup code here
    sys.exit(0)


def main(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description='Runnerly Tokendealer')

    parser.add_argument('--fd', type=int, default=None)
    parser.add_argument('--config-file', help='Config file',
                        type=str, default=_SETTINGS)
    args = parser.parse_args(args=args)

    app = create_app(args.config_file)
    app.static_folder = _STATIC_FOLDER

    fs_loader = jinja2.FileSystemLoader([_TMPL_DIR])
    app.jinja_loader = jinja2.ChoiceLoader([app.jinja_loader, fs_loader])
    host = app.config.get('host', '0.0.0.0')
    port = app.config.get('port', 5000)
    debug = app.config.get('DEBUG', False)

    signal.signal(signal.SIGINT, _quit)
    signal.signal(signal.SIGTERM, _quit)

    def runner():
        if args.fd is not None:
            # use chaussette
            httpd = make_server(app, host='fd://%d' % args.fd)
            httpd.serve_forever()
        else:
            app.run(debug=debug, host=host, port=port)

    if not debug:
        runner()
    else:
        run_with_reloader(runner)


if __name__ == "__main__":
    main()
