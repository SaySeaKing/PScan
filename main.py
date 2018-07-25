# -*- coding:utf-8 -*-

import _divide_IP
import time
import _scan_port
import _result_record
import threading
import Queue
PORT_ = Queue.Queue()
import nmap
import sys
import _ip_record
screenLock = threading.Semaphore(value=1)

result_ = {}
ports_ = []

def get_Port(ip, port):
    global ports_
    if threading.activeCount() <= thread_num:
            if _scan_port.Scan_Main(ip, port).run():
                ports_.append(port)


def task_Thread(ip, thread_num):
    while not PORT_.empty():
        if threading.activeCount() < thread_num:
            port = PORT_.get()
            task_get = threading.Thread(target=get_Port, args=(ip, port,))
            task_get.start()
    else:
        return

def do_only_Python(IP_):
    global ports_
    IP = _divide_IP.Divide_IP().run(IP_)
    # try:
    #     IP = _ip_record.ip_Decrease(IP_, IP)
    # except:
    #     pass
    while True:
        for ip in IP:
            try:
                ports = []
                for x in range(1, 500):
                    ports.append(x)
                ports_ = []
                for x in ports:
                    PORT_.put(x)
                task_ = threading.Thread(target=task_Thread, args=(ip, thread_num,))
                task_.setDaemon(True)
                task_.start()
                task_.join()
                # 等待
                time.sleep(5)
                _ip_record.result_Record(IP_, ip)
                if ports_ == []:
                    ports_ = ['NULL']
                _result_record.result_Record(IP_, [ip, ports_])
                print "%s SCAN END" % ip
            except Exception, e:
                print e
        break

def do_only_Nmap():
    IP = ''
    nm = nmap.PortScanner()
    ret = nm.scan(hosts='219.143.234.0/24', arguments='-sP')
    for key in ret['scan'].keys():
        IP += key + ' '
    ret = nm.scan(hosts=IP[:-1], arguments='-sS -p 1-65535')

def do_PythonScan_NmapAlive():
    global ports_
    IP = []
    nm = nmap.PortScanner()
    ret = nm.scan(hosts='219.143.234.0/24', arguments='-sP')
    for key in ret['scan'].keys():
        IP.append(key)
    while True:
        for ip in IP:
            try:
                ports = []
                for x in range(1, 65536):
                    ports.append(x)
                ports_ = []
                for x in ports:
                    PORT_.put(x)
                task_ = threading.Thread(target=task_Thread, args=(ip, thread_num,))
                task_.setDaemon(True)
                task_.start()
                task_.join()
                print ports_
                if ports_ != []:
                    print 'a'
                    _result_record.result_Record(IP_, [ip, ports_])
                print "%s SCAN END" % ip  
            except Exception, e:
                print e
        break

if __name__ == "__main__":
    starttime = time.time()
    thread_num = 1000
    # thread_num = raw_input(u"请输入线程数(默认3000): ".encode('gbk'))
    ip_list = ""
    file = open('input/ip_list.txt')
    for line in file.readlines():
        line = line.replace('{', '')
        line = line.replace('}', '')
        line = line.replace('ip', '')
        line = line.replace('\"', '')
        line = line.replace(':', '')
        line = line.replace('\n', '')
        line = line.replace("\r", "")
        line = line.replace('\"', '')
        IP_ = line
        ip_list += "%s," % IP_
    ip_list = ip_list[:-1]
    print ip_list
    do_only_Python(ip_list)
    end_time = time.time()
    betwn_time = end_time-starttime
    print betwn_time

