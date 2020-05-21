from telegram import Update
from botInit import initialize
from botSession import lx_tg, dp, logger
from flask import Flask, request as flask_req


app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    update = Update.de_json(flask_req.json, lx_tg)
    dp.process_update(update)
    return '', 200


@app.route('/', methods=['GET'])
def status():
    return '@LuXunRobot is online.', 200


if __name__ == '__main__':
    initialize()
    app.run(host='localhost', port=10569, debug=False)
    logger.info('Started.')  # Should not be displayed
