# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import pandas as pd
from send_sms import SMS


class SecretSanta:
    def __init__(self,names):
        # with open('names.txt') as file:
        #     self.names = file.read().strip().split()
        self.names = names
        self.assigned = []

    def __getChoice__(self,santa_name=None, inp_type = None):
        """
        :return: returns a randomly selected choice from the names
        """
        selected = np.random.choice(self.names)
        if type == 'items':
            return selected
        else:
            if selected in self.assigned:
                selected = self.__getChoice__(santa_name)
            else:
                if selected == santa_name:
                    selected = self.__getChoice__(santa_name)
            self.assigned.append(selected)
            return selected

class Wishlist:
    def __init__(self, name, phone_number, item, url, additional_details, address):
        self.name = name
        self.url = url
        self.phone_number = "+1" + str(phone_number)
        self.selected_item = item
        self.additional_details = additional_details
        self.address = address


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    df = pd.read_excel('Wishlist.xlsx')
    if len(df) % 2 != 0:
        raise ValueError
    SS = SecretSanta(df.names)
    for santa_name in df.names:
        assignee = SS.__getChoice__(santa_name=santa_name)
        record = df[df.names == assignee]
        ss = SecretSanta(['item1', 'item2'])
        result = ss.__getChoice__(inp_type='items')
        item_no = result if not pd.isna(record[result].values[-1]) and result == 'item2' else 'item1'
        url_id = 'url_for_' + str(item_no[:-1]) + '_' + str(item_no[-1])
        selected_item, url = record[item_no].values[-1], record[url_id].values[-1]
        if pd.isna(selected_item) and pd.isna(url):
            selected_item = 'anything'
            url = 'anywhere'
        elif pd.isna(selected_item):
            selected_item = 'particular item'
        elif pd.isna(url):
            url = 'anywhere'
        phone_number = df[df.names == santa_name].phone_number.values[-1]
        additional_details = record.additional_details.values[-1] if not pd.isna(record.additional_details.values[-1]) else "None"
        address = record.address.values[-1]
        wishlist = Wishlist(name=assignee, item=selected_item, phone_number=phone_number, url=url, additional_details=additional_details, address = address)
        SMS().send(wish_list=wishlist)


    # Find these values at https://twilio.com/user/account
    # To set up environmental variables, see http://twil.io/secure

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
