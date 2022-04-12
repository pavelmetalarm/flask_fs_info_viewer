from flask import Flask, render_template
import fs_info

app = Flask(__name__)


@app.route('/info')
def info():
    return render_template('info.html', total=fs_info.total, free=fs_info.free, used=fs_info.used)


if __name__ == "__main__":
    app.run()
