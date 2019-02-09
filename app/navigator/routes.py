#!/usr/bin/python3.6.7
###################################################################################################
# Name: routes.py
# Summary: This file contains routes for github navigator application
# Author(s): Irtiza Ali
# LastUpdated: 18/01/2019
###################################################################################################


# sys modules
import os
import sys
import json
from flask import Blueprint, render_template
from flask import request, jsonify, abort
from flask_api import status
mod = Blueprint('github_navigator', __name__)

# Developer defined modules
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'helpers'))
import navigator_helpers as nav_helpers


@mod.route('/navigator', methods=['GET'])
def health_check():
    '''
    It will be used to verify the status of api
    '''
    response = {}
    # extracting query params
    search_term = request.args.get('search_term')
    if request.args.get('number_of_repositories'):
        number_of_repositories = int(request.args.get('number_of_repositories'))
    else:
        number_of_repositories = None

    # if search_term is provided
    if search_term:
        response['search_term'] = search_term
        repositories_obj_list = nav_helpers.get_repositories(search_term, number_of_repositories)
        response['repo_information'] = repositories_obj_list
        return render_template('repo_info_template.html', result=response), status.HTTP_200_OK
    else:
        response['search_term'] = "No search term provided"
        return render_template('repo_info_template.html', result=response), status.HTTP_400_BAD_REQUEST
