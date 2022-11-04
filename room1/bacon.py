mapping = {
"00000": "A",
"00001": "B",
"00010": "C",
"00011": "D",
"00100": "E",
"00101": "F",
"00110": "G",
"00111": "H",
"01000": "I",
"01001": "J",
"01010": "K",
"01011": "L",
"01100": "M",
"01101": "N",
"01110": "O",
"01111": "P",
"10000": "Q",
"10001": "R",
"10010": "S",
"10011": "T",
"10100": "U",
"10101": "V",
"10110": "W",
"10111": "X",
"11000": "Y",
"11001": "Z",
"11010": " "
}


def decode(message: str) -> str:
    formatted_message = message.replace(" ", "").replace(",", "").replace(".", "").replace("'", "").replace(";", "") # todo improve this replacem

    decoded_message = "".join(["1" if l.isupper() else "0" for l in formatted_message])
    result = ""
    for i in range(0, len(decoded_message), 5):
        if l := mapping.get(decoded_message[i: i+5]):
            result += l

    return result

print(decode("My loRd, OUT of the LovE i bEar tO SomE OF YoUr friEnds, i haVe a CAre Of yOur PreserVATion. THeRefORE I WoulD aDVIse YOU, As YOU tEndEr yoUr life, TO DEvIsE soME exCUSe To shIft YoUR aTteNDANcE aT ThIS PaRliAMENt; FoR gOD anD man HatH ConCURREd To puNiSh THE wIcKedNess OF ThIs tIME. aNd tHInk NOT slIghTly oF THiS adVErtisemenT, but rETiRE YoUrselF inTO YouR CoUNtrY whERE YoU may ExpeCt the eVenT In SAFeTy. foR ThoUgH ThErE be NO apPEArANCe oF Any stir, yEt i SaY ThEy sHALL reCeiVe a tErriBlE Blow THiS paRliAmENT; and YET tHEy SHAlL nOt SEe Who hUrTs them. THis cOUNSel IS NOt To Be cONdeMNEd BECauSE it may do You GoOD aNd CaN Do yOu no hARm; FOr tHE dANGeR iS paSsed AS SoOn as you hAVe BurnT THE lEtteR. AnD i HopE God wILl Give YoU the grAcE To mAkE gooD usE of It, TO WHOSE HOLY PROTECTION I COMMEND YOU."))