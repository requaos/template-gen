# Import the email modules we'll need
import pprint
from email.parser import BytesParser, Parser
from email.policy import default

messagefile = '../data/test.eml'
# If the e-mail headers are in a file, uncomment these two lines:
with open(messagefile, 'rb') as fp:
    eml = BytesParser(policy=default).parse(fp)

#  Or for parsing headers in a string (this is an uncommon operation), use:
# headers = Parser(policy=default).parsestr(
#         'From: Foo Bar <user@example.com>\n'
#         'To: <someone_else@example.com>\n'
#         'Subject: Test message\n'
#         '\n'
#         'Body would go here\n')


# dict_variable = {key:value for (key,value) in dictonary.items()}
keys = ['content_html', 'content_text', 'from', 'subject', 'attachment_type', 'attachment_filename', 'sophistication', 'reply_to', 'from_display_name', 'name', 'reply_to_diplay_name', 'template_translation_uuid']
template = {key:'' for key in keys}

#  Now the header items can be accessed as a dictionary:
# print('To: {}'.format(eml['to']))
# print('From: {}'.format(eml['from']))
template['from'] = eml['from']
# print('Subject: {}'.format(eml['subject']))
template['subject'] = eml['subject']

# You can also access the parts of the addresses:
# print('Recipient username: {}'.format(eml['to'].addresses[0].username))
# print('Sender name: {}'.format(eml['from'].addresses[0].display_name))
template['from_display_name'] = eml['from'].addresses[0].display_name

ctype = eml.get_content_maintype()
if ctype == 'multipart':
    for part in eml.get_payload():
        subctype = part.get_content_maintype()
        if subctype == 'text':
            if part.get_content_subtype() == 'plain':
                template['content_text'] = part.get_payload()
            elif part.get_content_subtype() == 'html':
                template['content_html'] = part.get_payload()
elif ctype == 'text':
    if eml.get_content_subtype() == 'plain':
        template['content_text'] = eml.get_payload()
    elif eml.get_content_subtype == 'html':
        template['content_html'] = eml.get_payload()
else:
    print('nope...')

templates = []
templates.append(template)

# pprint.pprint(template)

output = 'output.et'
with open(output, 'w') as out:
    out.write(str(templates))
#print(str(eml.keys()))
