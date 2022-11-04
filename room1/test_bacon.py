import bacon
import pytest

@pytest.mark.parametrize(('message, expected'), [("", ""), 
("Hello", "Q"), 
("thE QUicK broWn FOx JuMPs OVEr THe LaZy DOgs, GAMbOlinG iN tHE fieLDS WHERE THE SHEPHERDS KEEP WATCH", 'HELLO WORLD'),
("To eNcOde A MesSage eACh letter OF tHe PLAintEXt Is rePlaced bY A GRouP OF FIve oF THE LETTERS 'A' OR 'B'.", 'STEGANOGRAPHY'),
('tHe quiCK broWN FOx jUmpS oveR the Lazy Dogs, GAMBOliNG iN the fielDs Where ThE ShEpheRds KEEP watCH', 'IMPERCEPTIBILITY'),
('My loRd, OUT of the LovE i bEar tO SomE OF YoUr friEnds, i haVe a CAre Of yOur PreserVATion. THeRefORE I WoulD aDVIse YOU, As YOU tEndEr yoUr life, TO DEvIsE soME exCUSe To shIft YoUR aTteNDANcE aT ThIS PaRliAMENt; FoR gOD anD man HatH ConCURREd To puNiSh THE wIcKedNess OF ThIs tIME. aNd tHInk NOT slIghTly oF THiS adVErtisemenT, but rETiRE YoUrselF inTO YouR CoUNtrY whERE YoU may ExpeCt the eVenT In SAFeTy. foR ThoUgH ThErE be NO apPEArANCe oF Any stir, yEt i SaY ThEy sHALL reCeiVe a tErriBlE Blow THiS paRliAmENT; and YET tHEy SHAlL nOt SEe Who hUrTs them. THis cOUNSel IS NOt To Be cONdeMNEd BECauSE it may do You GoOD aNd CaN Do yOu no hARm; FOr tHE dANGeR iS paSsed AS SoOn as you hAVe BurnT THE lEtteR. AnD i HopE God wILl Give YoU the grAcE To mAkE gooD usE of It, TO WHOSE HOLY PROTECTION I COMMEND YOU.', 'ROBERT CATESBY PROPOSED THIS PLOT WITH FOUR OTHER MAIN CONSPIRATORS THOMAS PERCY JOHN WRIGHT THOMAS WINTOUR AND GUY FAWKES')])
def test_decode(message, expected):
    assert bacon.decode(message) == expected
    