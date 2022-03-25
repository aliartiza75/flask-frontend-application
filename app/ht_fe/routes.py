#!/usr/bin/python3.6.7
###################################################################################################
# Name: routes.py
# Summary: This file contains routes for ht frontend
# Author(s): Irtiza Ali
# LastUpdated: 18/01/2019
###################################################################################################

# sys modules
import os
# import json
from flask import Blueprint, render_template
# from flask import request, jsonify, abort
from flask_api import status
import requests
mod = Blueprint('github_navigator', __name__)

# Extracting environment variable
BE_IP_ADDR = os.environ['BE_IP_ADDR']


@mod.route('/datetime', methods=['GET'])
def health_check():
    '''
    It will be used to verify the status of api
    '''
    response = {}
    response = requests.get("http://" + BE_IP_ADDR + "/datetime")
    data = response.json()
    # if search_term is provided
    return render_template('repo_info_template.html', result=data), status.HTTP_200_OK


@mod.route('/', methods=['GET'])
def index():
    '''
    It will be used to verify the status of api
    '''
    # if search_term is provided
    return render_template('repo_info_template.html', result=None), status.HTTP_200_OK
