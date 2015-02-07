import facebook
import requests
import json
import datetime
import iso8601

def time_diff(x):
    a=iso8601.parse_date(x)   #for parsing the facebook date standard to datetime
    b=datetime.datetime.now()
    a=a.replace(tzinfo=None)
    b=b.replace(tzinfo=None)
    c=b-a
    d = divmod(c.total_seconds(),86400)  # days
    h = divmod(c.total_seconds(),3600)  # hours
    m = divmod(c.total_seconds(),60)  # minutes

    if(m[0]>30):                      #facebook stores the time of any event in GMT 
        min=m[0]-30
        hour=h[0]-5
    else:
        min=m[0]+30
        hour=h[0]-6
        
    return (m[1],min%60,hour%24,d[0])

def post_trafficpolice(city_id):
    posts=graph.get_connections(id=city_id,connection_name='statuses')
    i=0
    print("Posts by traffic police")
    while(i<message_post_no):
        time=posts['data'][i]['updated_time']
        t_diff=time_diff(time)
        if(t_diff[2]>0):
            break
        print (str(int(t_diff[2]))+" hour "+str(int(t_diff[1]))+" min ")
        post=posts['data'][i]['message'].encode('utf8')
        print (post)
        print("\n\n")
        i=i+1

def post_public(city_id):
    print('Problems faced by General Public\n')
    tagged=graph.get_connections(id=city_id,connection_name='tagged')
    i=0
    while(i<tagged_post_no):
        time=tagged['data'][i]['updated_time']
        t_diff=time_diff(time)
        if(t_diff[3]>1):
            break
        if(tagged['data'][i]['type']=="status"):
            print (str(int(t_diff[3]))+" days "+str(int(t_diff[2]))+" hour "+str(int(t_diff[1]))+" min ")
            post=tagged['data'][i]['message'].encode('utf8')
            print(post)
            print("\n\n")
        i=i+1



token="YOUR TOKEN HERE"

global message_post_no
global tagged_post_no
message_post_no=10
tagged_post_no=10

delhi_id='117817371573308'
kolkata_id='129115403803409'
chennai_id='141144945912047'
bangalore_id='147207215344994'

graph = facebook.GraphAPI(access_token=token)

################################################################
#DELHI
################################################################

detail= graph.get_object(id=delhi_id)
print (detail['name'])
print (detail['about'])
print (detail['link'])
print (json.dumps(detail['location'],indent=4,sort_keys="true"))
print (detail['phone'])
print (detail['website'])
print ("\n")

posts=graph.get_connections(id=delhi_id,connection_name='statuses')

i=0
print("Posts by traffic police")
while(i<message_post_no):
    time=posts['data'][i]['updated_time']
    t_diff=time_diff(time)
    if(t_diff[2]>0):
        break
    post=posts['data'][i]['message'].encode('utf8')
    p=post[0]
    j=1
    while(post[j]!="\n"):
        p+=post[j]
        j=j+1
        if(j>70):
            break
    p=str.lower(p)
    print (str(int(t_diff[2]))+" hour "+str(int(t_diff[1]))+" min ")
    if(p=="traffic advisory" or p=="traffic alert"):
        print ("Traffic Alerts")
        print (post[j+1:])
    else:
        print(p)
        print (post[j+1:])
    
    print("\n\n")
    i=i+1

print("\n\n\n")

post_public(delhi_id)


 #officeorder
# press release
# notice issued
# Guidelines for children while walking to school
# Guidelines for teachers for ensuring safety of school children
# LOSS REPORT
################################################################
#KOLKATA TRAFFIC
################################################################

detail= graph.get_object(id=kolkata_id)
print (detail['name'])
print (detail['link'])
print (detail['website'])
print (detail['general_info'])
print ("\n")
post_trafficpolice(kolkata_id)

print("\n\n\n")
post_public(kolkata_id)

################################################################
#BANGALORE
################################################################


detail= graph.get_object(id=bangalore_id)
print (detail['name'])
print (detail['link'])
print (json.dumps(detail['location'],indent=4,sort_keys="true"))
print (detail['phone'])
print (detail['website'])
print ("\n")

post_trafficpolice(bangalore_id)

print("\n\n\n")
post_public(bangalore_id)

################################################################
#CHENNAI
################################################################

detail= graph.get_object(id=chennai_id)
print (detail['name'])
print (detail['link'])
print (json.dumps(detail['location'],indent=4,sort_keys="true"))
print (detail['phone'])
print (detail['website'])
print ("\n")

post_trafficpolice(chennai_id)
print("\n\n\n")
post_public(chennai_id)

