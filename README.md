# The Gunpowder Plot Kata

## The Story

You have travelled back in time to November 1605, there's been a failed assassination attempt against King James I and one John Johnson, Servant to Mr. Thomas Percy, was there apprehended; who had placed Thirty-six Barrels of Gunpowder in the Vault under the House, with a Purpose to blow King, and the whole Company, when they should there assemble.

Although the government had an inklings of a plot, the first clear intelligence came with the anonymous warning given to a Catholic nobleman, Lord Monteagle, that he should not attend the opening of Parliament on 5 November. It read as follows:

My loRd, OUT of the LovE i bEar tO SomE OF YoUr friEnds, i haVe a CAre Of yOur PreserVATion. THeRefORE I WoulD aDVIse YOU, As YOU tEndEr yoUr life, TO DEvIsE soME exCUSe To shIft YoUR aTteNDANcE aT ThIS PaRliAMENt; FoR gOD anD man HatH ConCURREd To puNiSh THE wIcKedNess OF ThIs tIME. aNd tHInk NOT slIghTly oF THiS adVErtisemenT, but rETiRE YoUrselF inTO YouR CoUNtrY whERE YoU may ExpeCt the eVenT In SAFeTy. foR ThoUgH ThErE be NO apPEArANCe oF Any stir, yEt i SaY ThEy sHALL reCeiVe a tErriBlE Blow THiS paRliAmENT; and YET tHEy SHAlL nOt SEe Who hUrTs them. THis cOUNSel IS NOt To Be cONdeMNEd BECauSE it may do You GoOD aNd CaN Do yOu no hARm; FOr tHE dANGeR iS paSsed AS SoOn as you hAVe BurnT THE lEtteR. AnD i HopE God wILl Give YoU the grAcE To mAkE gooD usE of It, to whose holy protection i commend you.

But as you may notice, something seems strange about the font. As a keen computer scientist, you are aware of the Baconian cipher, a method of steganographic message encoding devised by Francis Bacon in 1605, could this message have been encoded with this technique? If we can decode this message we may find out more information about this John Johnson and his co-conspirators.

For your convenience, the message has also been saved in `message.txt`.

## Bacon's Cipher

To encode a message, each letter of the plaintext is replaced by a group of five of the letters 'A' or 'B'. This replacement is a 5-bit binary encoding and is done according to the alphabet of the Baconian cipher (from the Latin Alphabet).

In the first version I and J, U and V are each grouped together, but a second version of Bacon's cipher uses a unique code for each letter. In other words, I, J, U and V each have their own pattern in this variant.

The Baconian alphabet may optionally be extended to add a few punctuation characters such as the space, which has been added as the next character `bbaba` aka `11010`, no other punctuation is used in the secret message.

Letter 	Code 	Binary
A 	aaaaa 	00000
B 	aaaab 	00001
C 	aaaba 	00010
D 	aaabb 	00011
E 	aabaa 	00100
F 	aabab 	00101
G 	aabba 	00110
H 	aabbb 	00111
I 	abaaa 	01000
J 	abaab 	01001
K 	ababa 	01010
L 	ababb 	01011
M 	abbaa 	01100
N 	abbab 	01101
O 	abbba 	01110
P 	abbbb 	01111
Q 	baaaa 	10000
R 	baaab 	10001
S 	baaba 	10010
T 	baabb 	10011
U 	babaa 	10100
V 	babab 	10101
W 	babba 	10110
X 	babbb 	10111
Y 	bbaaa 	11000
Z 	bbaab 	11001
` `	bbaba 	11010

An obfuscated function which can encode has been made available as `encode.g(message, carrier)`.

For example:
```py
>>> encode.g('HELLO WORLD', 'The quick brown fox jumps over the lazy dogs, gamboling in the fields where the shepherds keep watch')
'thE QUicK broWn FOx JuMPs OVEr THe LaZy DOgs, GAMbOlinG iN tHE fieLDS WHERE THE SHEPHERDS KEEP WATCH'

>>> encode.g('steganography', "To encode a message each letter of the plaintext is replaced by a group of five of the letters 'A' or 'B'.")
"To eNcOde A MesSage eACh letter OF tHe PLAintEXt Is rePlaced bY A GRouP OF FIve oF THE LETTERS 'A' OR 'B'."

>>> encode.g('imperceptibility', 'The quick brown fox jumps over the lazy dogs, gamboling in the fields where the shepherds keep watch')
'tHe quiCK broWN FOx jUmpS oveR the Lazy Dogs, GAMBOliNG iN the fielDs Where ThE ShEpheRds KEEP watCH'

>>> encode.g('telecommunication', 'The quick brown fox jumps over the lazy dogs, gamboling in the fields where the shepherds keep watch')
ValueError: message is too long for the carrier
```

Note: when the message is shorter than the carrier, the latter groups are all uppercase, so outside of the alphabet and are assumed not to form part of the message.

## References
- https://en.wikipedia.org/wiki/Gunpowder_Plot
- https://www.parliament.uk/about/living-heritage/evolutionofparliament/parliamentaryauthority/the-gunpowder-plot-of-1605/overview/
- https://en.wikipedia.org/wiki/Bacon%27s_cipher
