from datetime import datetime


class dh:
    @staticmethod
    def Out(func, text):
        now = datetime.now()
        print("{} {%10s} {} ".format(now),func,text)