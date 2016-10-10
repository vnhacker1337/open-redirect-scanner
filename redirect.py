import requests
import sys
import time
import os


os.system('clear')
print "#################################################"
print "# Open redirect Scanner for dummies like me :)  #"
print "#  by ak1t4 (know.0nix@gmail.com)               #"
print "  twitter.com/knowledge_2014  		       #"
print "  www.security-root.com			       #"
print "#################################################"
print ""
print "Use ./redirect.py [subdomains.file] [redirect-payload]"
print "Example ./redirect.py uber.list '//yahoo.com/%2F..'"


# Payloads example

#payload = '//www.google.com/%2F..'
#payload2 = '//www.yahoo.com//'
#payload3 = '//www.yahoo.com//%2F%2E%2E'

# first argument - file with subdomains

file = sys.argv[1]

# second argument - payload string

payload = sys.argv[2]



#open file with subdomains and iterates
 
with open(file) as f:

		print ""
		print "Searching the ex-girlfriend target &  Holy Grial at [303 see others].."
		print ""
		time.sleep(4)


		# loop for find the trace of all requests (303 is an open redirect) see the final destination

                for line in f:
		    

                    try:

                        line2 = line.strip()

                        line3 = 'http://' + line2 + payload

                        print line3

                        response = requests.get(line3, verify=True)    

                        print response

                        try:

                            if response.history:
                             
                                print "Request was redirected"
                             
                                for resp in response.history:

                                    print "|"
                                    print resp.status_code, resp.url
                                    

                                print "Final destination:"

                                print "+"
                                print response.status_code, response.url

                                
                            else:

                                print "Request was not redirected"

                            
                        except:
                            print "connection error :("

                    except:

                        print "quiting.."


