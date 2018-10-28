# utils.py

def read_content(storyfiles):
    s = {}
    for k in storyfiles:
        try:
            with open(storyfiles[k], 'r') as f:
                s[k] = f.read()
        except Exception as e:
            print(e)
    return s
