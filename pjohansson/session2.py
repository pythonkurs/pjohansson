import requests
import untangle

def download_data():
    """Downloads data from NYC Grand Central information website, returns
    full request.get data."""

    print "Downloading current data from ",
    print "http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml ..." ,

    # Download data
    raw_data = requests.get(
            "http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml"
            )

    # Verify download status
    if raw_data.status_code == 200:
        print "Done."
    else:
        print "Could not download data."

    return raw_data

def get_outage_data(raw_data):
    """Reads raw data and returns untangled outage data."""

    # Untangle content from downloaded data
    untangled_data = untangle.parse(raw_data.content)

    # Get outage data from tree
    return untangled_data.NYCOutages.outage

def count_repair(outage_data):
    """Counts and returns the number of status 'Repair' in outage data."""

    # Go through all outages, check reason data and count number of 'Repair'
    count_repair = 0
    for outage in outage_data:
        if outage.reason.cdata.upper() == 'REPAIR':
            count_repair += 1

    return count_repair
