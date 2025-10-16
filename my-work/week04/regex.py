import re

with open ('access.log.smaller.txt', 'r') as fp:
    log_data = fp.read()

# dates = re.findall("\[(.*)\].", log_data)
# print(dates)

anonymized_log_data = re.sub(r'(\d{1,3}\.\d{1,3}\.)\d{1,3}\.\d{1,3} -', '\\1XXX.XXX', log_data)
print(anonymized_log_data)

with open('anonymized_access.log.txt', 'w') as fp:
    fp.write(anonymized_log_data)