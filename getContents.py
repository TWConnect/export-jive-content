from utils.fetchUtil import handleListRequest
from models.content import Content
from models.message import Message
from models.comment import Comment

from requests.auth import HTTPBasicAuth

bauth = HTTPBasicAuth('user', 'pass')
url = "https://organization-name.jiveon.com/api/core/v3/places/72743/contents?count=100"

handleListRequest(url, Content.parse_response, auth=bauth)

apiUrl = "https://organization-name.jiveon.com/api/core/v3"

query = Content.select().where(Content.id >= 0).order_by(Content.id)

print(len(query))

for content in query:
    print(content.id, content.subject)
    if content.type == "discussion":
        handleListRequest(apiUrl + '/messages/contents/' + str(content.content_id), Message.parse_response, auth=bauth)
    elif content.type == "poll" \
        or content.type == "idea" \
        or content.type == "document" \
        or content.type == "update" \
        or content.type == "file" \
        or content.type == "post":
        handleListRequest(content.self_ref + '/comments', Comment.parse_response, auth=bauth)

