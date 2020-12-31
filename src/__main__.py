#
#          DiscordMachines __main__.py | 2020 (c) Mrmagicpie
#          All rights reserved. Licensed under Mrmagicpie https://license.mrmagicpie.xyz
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
import os

from flask import Flask, redirect, render_template, request, session, url_for
import flask
import re
app = Flask(__name__)

for cog_dir in os.listdir(os.getcwd()):
    if os.name == "nt":
        dir_lmao = f"{os.getcwd()}\{cog_dir}"
    else:
        dir_lmao = f"{os.getcwd()}/{cog_dir}"
    if os.path.isdir(dir_lmao) and cog_dir.startswith("bps_"):
        for cogs in os.listdir(cog_dir):
            if cogs.endswith('.py'):
                file = open(f'{cog_dir}/{cogs}', 'r')
                e = []
                for i in file.readlines():
                    x = re.findall("^#", i)
                    if not x:
                        e.append(i)
                raw_cog_oop = e[1].split(" ", 1)[0]
                cog = getattr(__import__(f"{cog_dir}.{cogs[:-3]}", fromlist=[raw_cog_oop]), raw_cog_oop)
                app.register_blueprint(cog)

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'), code=302)

@app.errorhandler(404)
def not_found(e):
    return render_template("errors/404.html"), 404

if __name__ == '__main__':

    app.secret_key = 'dkjghasdlfsadlfkjdjfnkjk383wi8977w3mbi2ko2jwiohmw4tbiwueglJGB'
    app.run(port="2002", debug=True, use_reloader=True)
