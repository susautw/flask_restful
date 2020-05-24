import argparse

from waitress import serve
from app import create_app


def main():
    app = create_app()
    args = get_arg_parser().parse_args()
    serve(app, host=args.host, port=args.port)
    serve(app, host=args.host, port=args.port)


def get_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, default='0.0.0.0')
    parser.add_argument('--port', type=int, default=80)
    return parser


if __name__ == '__main__':
    main()