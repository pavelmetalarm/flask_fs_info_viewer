from flask import Flask, render_template
import fs_info



app = Flask(__name__)

#hardware_info = fs_info.all_my_disks[0]
hardware_info = fs_info.all_my_disks

@app.route('/info')
def info():
    return render_template('info.html', total=fs_info.total, free=fs_info.free, used=fs_info.used,\
           all_my_disks = hardware_info)





if __name__ == "__main__":
    app.run()
