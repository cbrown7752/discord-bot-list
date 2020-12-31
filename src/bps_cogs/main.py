#
#          DiscordMachines main.py | 2020 (c) Mrmagicpie
#          All rights reserved. Licensed under Mrmagicpie https://license.mrmagicpie.xyz
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
from flask import render_template, Blueprint
main = Blueprint('main', __name__)
# from sql import db
# from login import logged_in
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
@main.route("/", methods=["GET"])
def main():
    return render_template('index.html'), 200

#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#