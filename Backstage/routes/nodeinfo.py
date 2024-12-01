from flask import jsonify

from Backstage import app

@app.route('/.well-known/nodeinfo', methods=['GET'])
def nodeinfo():
    info = {
        "links":[
            {"rel":"http://nodeinfo.diaspora.software/ns/schema/2.0",
             "href":f"{app.config.get('servename')}/nodeinfo/2.0"}
             ]
    }
    return jsonify(info)


@app.route('/nodeinfo/2.0', methods=['GET'])
def nodeinfo_2_0():
    info = {
        "version":"2.0",
        "software":{
            "name":"Backstage",
            "version":app.config.get('version')
        },
        "protocols":[
            "http://nodeinfo.diaspora.software/ns/schema/2.0"
        ],
        "services":{
            "inbound":[],
            "outbound":[]
        },
        "openRegistrations":app.config.get('openRegistrations'),
        "usage":{
            "users":{
                "total":0,
                "activeHalfyear":0,
                "activeMonth":0
            },
            "localPosts":0,
            "localComments":0
        },
        "metadata":{
            "nodeName":app.config.get('servename'),
            "softwareRepository": ""

        }
    }
    return jsonify(info)
