from Crypto.Util.number import bytes_to_long, long_to_bytes

# Given values
p = 12356573163529598509213416174151861564596383830485018644278746893087090144408283958799336630528980126522872980535414844640172383511144755076498012598740491
g = 3
x = 4269683307793620725070072977211386971525204150007887251853021892065742120162824806232150523319700182794711503615223400958382182740095937720121533292824860

# Ciphertext components
c1 = 11576793294956581447942827732474525036726321123141607291649578919191328375748354750403570532336816570254127112205724739592493832284630645500328575885898482
c2 = 5869151441899192030633298239328772075475210301249926616779656042841923219443140774357107951495645924345530369302336702148205619608533666433864816609554681

# Calculate s = c1^x mod p
s = pow(c1, x, p)

# Calculate s_inv = s^(-1) mod p using pow with a negative exponent
s_inv = pow(s, -1, p)

# Decrypt message
m = (c2 * s_inv) % p

# Convert message to bytes
flag = long_to_bytes(m)
print(flag.decode())

