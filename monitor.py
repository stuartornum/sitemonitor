#!/usr/bin/env python

import urllib2
import sys
from optparse import OptionParser


def check_site(options):
    req = urllib2.Request(options.website)
    response = urllib2.urlopen(req)

    if int(response.code) != int(options.code):
        print '\n[ERROR] Response code match failed'
        print 'Received:', response.code
        print 'Expected:', options.code
        sys.exit(1)
    else:
        print "\n[SUCCESS] Correct response code:", options.code

    if options.text is not None:
        data = response.read()
        if str(options.text) not in data:
            print '\n[ERROR] Response did not contain the required text'
            print 'Required text:', options.text
            sys.exit(1)
        else:
            print "\n[SUCCESS] Text found:", options.text


def main():
    parser = OptionParser()
    parser.add_option('-w', '--website', dest='website', default=None,
                      help='Website to check')
    parser.add_option('-c', '--code', dest='code', default=200,
                      help='Response code, default is 200')
    parser.add_option('-t', '--text', dest='text', default=None,
                      help='Check if text is present in the body')

    (options, args) = parser.parse_args()

    if options.website is None:
        print '\n[ERROR] Please enter a website to monitor, e.g. ( -w www.google.com)'
        sys.exit(1)

    check_site(options)


if __name__ == "__main__":
    main()
