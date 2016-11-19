#!/usr/bin/python


class FileOwners:

    @staticmethod
    def group_by_owners(files):
	res = {}
        for key in files:
		if files[key] not in res.items():
			print files[key],"is first with",key
			res[files[key]] = key
		else:
			print files[key], "has been seen"
			res[files[key]].append(key) 
		print key,"==",files[key]
	return res

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))

