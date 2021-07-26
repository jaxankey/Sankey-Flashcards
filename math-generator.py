import pyperclip

# Generates math cards to paste into the google sheet
s = ''
for n in range(0,10):
    for m in range(0,10):
        s = s+'\n'+str(n)+' + '+str(m)+'\t'+str(n+m)
pyperclip.copy(s.strip())

        