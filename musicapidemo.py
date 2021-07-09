#!/usr/bin/python3

'''
musicapidemo.py

Description:
        Demo script written to retrieve the Music Festival list 
        in JSON objects and format it for internal display as per requirement

Modification history:
1.0.0   04 July 2021            Vijayakumar Krishnaswamy
    Initial version
'''

from flask import Flask, jsonify, abort, request, make_response, url_for, render_template
import urllib.request, json, logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app.config['JSON_SORT_KEYS'] = False

app = Flask(__name__)

@app.errorhandler(429)
def too_many_requests(e):
    return render_template('429.html'), 429

@app.route('/displaymusicapi', methods = ['GET'])
def funcGET():
    try:
        sURL = "https://eacp.energyaustralia.com.au/codingtest/api/v1/festivals/"
        #Taking response and request  from url
        sResponse = urllib.request.urlopen(sURL)
        #reading and decoding the data
        dictResponse = json.loads(sResponse.read().decode(sResponse.info().get_param('charset') or 'utf-8'))

        tmpList=[]
        tmpDict={'label':'','bands':[{'name':'','festivals':[{'name':''}]}]}

        for json_object in dictResponse:
            for each_object in (json_object['bands']):
                if 'name' in each_object:
                    for dict_object in tmpDict['bands']:
                        dict_object['name']=each_object['name']
                        if 'recordLabel' in each_object:
                            if each_object['recordLabel'] == '':
                                break
                            tmpDict['label']=each_object['recordLabel']
                            if 'name' in json_object:
                                for dict_object in tmpDict['bands']:
                                    for fest_object in dict_object['festivals']:
                                        fest_object['name']=json_object['name']
                        tmpDictCopy=tmpDict.copy()
                        tmpList.append(tmpDictCopy)
                        tmpDict={'label':'','bands':[{'name':'','festivals':[{'name':''}]}]}
                        #sKey = "label"
                        #if 'Pacific Records' in [tmpD[sKey] for tmpD in tmpList]:
                        #        for modList in tmpList:
                        #                modList.append(my_list[idx])
        return jsonify(sorted(tmpList, key=lambda k: k['label'])), 200

    except urllib.error.HTTPError as ex:
        logger.exception(ex.args)
        raise ex
    except Exception as e:
        logger.exception(ex.args)
        raise ex

if __name__ == '__main__':
        app.run(host='0.0.0.0',port='9443',threaded=True)
