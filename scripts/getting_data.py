"""Downloads escalator service data of the NYC subway system and calculates the 
fraction of those having the status of 'Repair'."""

import requests
import untangle

print "Downloading current data from http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml ..." ,

# Download data
raw_data = requests.get("http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml")

# Verify download status
if raw_data.status_code == 200:
    print "Done."
else:
    print "Could not download data."

# Untangle content from downloaded data
untangled_data = untangle.parse(raw_data.content)

# Get outage data from tree
outages = untangled_data.NYCOutages.outage

# Go through all outages, check reason data and count number of 'Repair'
count_repair = 0
for outage in outages:
    if outage.reason.cdata.upper() == 'REPAIR':
        count_repair += 1

# Print final data
print 
print "%d out of %d, or %.1f%% of all, escalators in the system currently has the status 'Repair'." % (count_repair, len(outages), 
                count_repair / float(len(outages)) * 100)
