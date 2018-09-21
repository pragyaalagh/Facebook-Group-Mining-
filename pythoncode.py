
a_token='Graph API explorer generated token'


#this segment is to find the data of the user who access token is being used 

url="https://graph.facebook.com/v2.11/me?fields=id%2Cname&access_token={}".format(a_token)
payload=dict(id='id',name='name')
r=requests.get(url,data=payload)
user_data=json.loads(r.text)
print(user_data)

#this segment is to find all the groups that the user is an admin of
#alternate approach could be to use json.dumps(r.content)

urlgroup="https://graph.facebook.com/v2.11/me/groups?access_token={}".format(a_token)
payload=dict(id='id',name='name')
r1=requests.get(urlgroup,data=payload)
if r1.status_code==200:
        print("Success")
else:
        print("cannot access the group")
datagroup=json.loads(r1.text)
print(datagroup)
group_name=list()
group_id=list()
req_group_id='0'

for x in datagroup["data"]:
        group_name.append(x['name'])
        group_id.append(x['id'])
groups= dict(zip(group_name,group_id)) 
#this forms a dictionary of the groups and the corresponding id's of the groups the user is an admin of
print(groups)

#this segment returns the id of the required group from amongst the groups that the user is an admin of 
for y in groups:
        if y['name']=="UberNeoUltraModern Family":
                req_group_id=y['id']
                print("required group id found")
        else:
                print("required group id cannot be found")
                

#this segment is to access the feed of the group required through the group id

feedurl="https://graph.facebook.com/v2.11/{}/feed?access_token={}".format(req_group_id).format(a_token)
r2=requests.get(feedurl)
if r2.status_code==200:
        print("sucess")
else:
        print("not able to access the feed")
postdata=json.decodes(r2.text)
p_data=json.loads(postdata)
pprint(p_data)
