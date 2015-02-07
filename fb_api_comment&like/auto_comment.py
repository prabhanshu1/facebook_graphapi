import json
import fb                     #To install this package run: sudo pip install fb
from facepy import GraphAPI   #To install this package run: sudo pip install facepy
from facepy import get_extended_access_token
from facepy.exceptions import OAuthError
def comment():
    token="YOUR ACCESS TOKEN"
    facebook=fb.graph.api(token)
    graph1 = GraphAPI(token,verify_ssl_certificate=False)

    query="me"+"/feed?fields=id,from&since=DATE_TIME &limit="no.of posts"          #IT QUERY FO ALL YOUR FEEDS SINCE  DATE_TIME (YYYY-MM-DDThh:mm:ss) WITH NO.OF POST QUERID LIMITED TO no.of post

    try:
        r=graph1.get(query)
    except OAuthError as error:
        print error.message

    idlist=[x['id'] for x in r['data']]
    print("There are "+ str(len(idlist)) +" posts.")

    length=len(idlist)
    count=0
    for id in (idlist[:len(idlist)]):
        name=r['data'][count]["from"]["name"]
        name=name.split(" ")
        count+=1
        facebook.publish(cat="comments",id=id,message="Thanks "+str(name[0])+ " !!") #Comments on each post with message Thanks (first_name) !!
        facebook.publish(cat="likes",id=id)                 #Likes each post
        print("Notification number:"+str(count)+" on www.facebook.com/"+str(id).split('_')[0]+"/posts/"+str(id).split('_')[1])

comment()
