from scipy.io.wavfile import read

(fs, x) = read('stegano400.wav')
print(fs)
print(len(x.shape))
print(x[:,0])
print(x[:,1])

c1 = x[:,0]
c2 = x[:,1]
d = []
for a, b in zip(c1, c2):
    d.append(b - a)
print(d[0:100])

out = open('result', 'wb')
for t in d: out.write(chr(t))
out.close()
