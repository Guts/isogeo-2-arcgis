import urllib2
import socket

def is_bad_proxy(pip):
    try:
        proxy_handler = urllib2.ProxyHandler({'http': pip})
        opener = urllib2.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib2.install_opener(opener)
        req=urllib2.Request('http://www.example.com')  # change the URL to test here
        sock=urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print 'Error code: ', e.code
        return e.code
    except Exception, detail:
        print "ERROR:", detail
        return True
    return False

def main():
    socket.setdefaulttimeout(120)

    protocole = u"http"
    prox = u"10.0.4.2"
    port = u"3128"

    # two sample proxy IPs
    proxyList = ['10.0.4.2:3128', '{0}:{1}'.format(prox, port)]

    for currentProxy in proxyList:
        if is_bad_proxy(currentProxy):
            print "Bad Proxy %s" % (currentProxy)
        else:
            print "%s is working" % (currentProxy)

if __name__ == '__main__':
    main()
