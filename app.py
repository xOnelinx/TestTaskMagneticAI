from flask import Flask
from parser_app.parser import Parser, FormattedPrint

app = Flask(__name__)


@app.route('/games')
def all_games():
    parser = Parser("https://play.google.com/store/apps/category/GAME")
    parsed_games = parser.get_parsed_objects()
    return FormattedPrint.formatter(parsed_games)


@app.route('/games/<substr>')
def filter_games(substr):
    parser = Parser("https://play.google.com/store/apps/category/GAME")
    parsed_games = parser.get_parsed_objects()
    parsed_games = Parser.filter_by_substring(substr, parsed_games)
    return FormattedPrint.formatter(parsed_games)


if __name__ == '__main__':
    app.run()
