pi = 3.1415
### LWE parameters ###
n = 192
l = 192
m = 1500
q = 8191
r = 5
t = 4
alpha = 0.0009959


S = matrix(ZZ, n, l, [randint(1,q-1) for _ in range(n*l)])

A = matrix(ZZ, m, n, [randint(1,q-1) for _ in range(m*n)])

from sage.stats.distributions.discrete_gaussian_integer import DiscreteGaussianDistributionIntegerSampler
sigma = alpha*q/sqrt(2*pi)
D = DiscreteGaussianDistributionIntegerSampler(sigma=sigma)
E = matrix(ZZ, m, l, [D() for _ in range(m*l)])

P = A*S + E


### INPUT VECTOR ###
v = vector([randint(0,t-1) for _ in range(l)])
print(v)
a = vector([randint(-r,r) for _ in range(m)])

### Cipher text ###
u = A.transpose() * a
c = P.transpose() * a + (v * (q/t))


### Decryption ###
v_out = vector(round(_) for _ in ((c - (S.transpose() * u))/float(q/t)))
print(v_out)

if (v == v_out):
    print("MATCH")
else:
    print("ERROR indexes are:")
    for _ in range(l):
        if (v[_] != v_out[_]):
            print(_, v[_], v_out[_])

