"""Downloads escalator service data of the NYC subway system and calculates the
fraction of those having the status of 'Repair'."""

from pjohansson.session2 import download_data, get_outage_data, count_repair

raw_data = download_data()
outage_data = get_outage_data(raw_data)
num_repair = count_repair(outage_data)

print
print "%d out of %d, or %.1f%% of all, escalators in the system currently has the status 'Repair'." % (num_repair, len(outage_data),
                num_repair / float(len(outage_data)) * 100)
