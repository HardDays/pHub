import urllib2, urllib

class NotifController(object):
    def __init__(self):
        #self.db_collector = db_collector
        #self.url = 'https://api.twilio.com/2010-04-01/Accounts/ACd8d6b302b4c2443c0d5c4900c83be654/Messages.json'
        #self.auth = ('ACd8d6b302b4c2443c0d5c4900c83be654', '127b3a7934c97c80cef18e3a4002ce1d')

        self.url = 'https://api.twilio.com/2010-04-01/Accounts/AC30d84becc930c90cb2c2bf01ea6a99ab/Messages.json'
        self.auth = ('AC30d84becc930c90cb2c2bf01ea6a99ab', 'ac118f8179fcd39274ddd982892853d0')
        #self.client = Client('SKaeabc58042634cd32b65c545ff4cb42b', 'Q6Y2g5mEiZMAYAl3kBSPPA6BvhaSfn2F', 'ACd8d6b302b4c2443c0d5c4900c83be654')

    def send_to_user(self, user, notification):
        #+12029993558
        if user.phone:
            r = requests.post(self.url, 
                        data={'From': '+16123602818', 'To': user.phone, 'Body': notification.message}, auth=self.auth)

    def send_to_phone(self, phone, message):
        #r = requests.post(self.url, 
                       # data={'From': '+12029993558', 'To': phone, 'Body': message}, auth=self.auth)

        data = urllib.urlencode({'From': '+16123602818', 'To': phone, 'Body': message})
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, self.url, self.auth[0], self.auth[1])
        auth_handler = urllib2.HTTPBasicAuthHandler(passman)
        opener = urllib2.build_opener(auth_handler)
        urllib2.install_opener(opener)
        content = urllib2.urlopen(self.url, data)
        print(content)
        #print(r.status_code, r.reason)
        '''
        message = self.client.api.account.messages.create(
                                            to=phone,
                                            from_='+12029993558',
                                            body=message)'''

    def send_to_group(self, group, notification):
        for user in group.users:
            self.send_to_user(user, notification)

    def send_to_contacts(self, user, notification):
        for contact in user.contacts:
            self.send_to_user(contact, notification)