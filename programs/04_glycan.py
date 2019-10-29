# SH-1

def non_repeating(iupac):

    glycan = iupac.split('-')

    if len(glycan) > 3:

        mono_1 = glycan[0]
        mono_1 = mono_1[:-2] + '(' + mono_1[-2:]

        mono_mid = glycan[1:-2]

        for i, x in enumerate(mono_mid):

            x = x[:1] + ')' + x[1:-2] + '(' + x[-2:]

            mono_mid[i] = x

        mono_n = glycan[-2]
        mono_n = mono_n[:1] + ')' + mono_n[1:-1] + '(' + mono_n[-1:] + '1'

        linkage = glycan[-1]

        return mono_1 + '-' + '-'.join(mono_mid) + '-' + mono_n + '-'

    else:

        mono_1 = glycan[0]
        mono_1 = mono_1[:-2] + '(' + mono_1[-2:]

        mono_n = glycan[-2]
        mono_n = mono_n[:1] + ')' + mono_n[1:-1] + '(' + mono_n[-1:] + '1'

        linkage = glycan[-1]

        return mono_1 + '-' + mono_n + '-'

def repeating(iupac):

    glycan = iupac.split('(')

    rep = glycan[1]
    rep = rep.split(')')

    n = int(rep[1][0])

    rep = rep[0]
    rep = rep.split('-')

    if len(rep) > 3:

        mono_1 = rep[0]
        mono_1 = mono_1[:-2] + '(' + mono_1[-2:]

        mono_mid = rep[1:-2]

        for i, x in enumerate(mono_mid):

            x = x[:1] + ')' + x[1:-2] + '(' + x[-2:]

            mono_mid[i] = x

        mono_n = rep[-2]
        mono_n = mono_n[:1] + ')' + mono_n[1:-1] + '(' + mono_n[-1:] + '-' + rep[-1]

        rep =  mono_1 + '-' + '-'.join(mono_mid) + '-' + mono_n + ')'

    else:

        mono_1 = rep[0]
        mono_1 = mono_1[:-2] + '(' + mono_1[-2:]

        mono_n = rep[-2]
        mono_n = mono_n[:1] + ')' + mono_n[1:-2] + '(' + mono_n[-2:] + '-' + rep[-1]

        rep =  mono_1 + '-' + mono_n + ')'

    chain = rep * n
    chain = chain[:-2]

    return chain

input = '(Galb1-4GlcNAcb1-3)2b-Sp'
output = 'Gal(b1-4)GlcNAc(b1-3)Gal(b1-4)GlcNAc(b1-'

print(repeating(input))
print(output)
