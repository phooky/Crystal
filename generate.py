import pattern
import ply
import projection

res = (800,600)
# screen upper-left phy coords, in.
s1 = (-0.2,-0.15)
# screen lower-righ phy coords, in.
s2 = (0.2, 0.15)
# screen distance
p=pattern.make_depths(res[0],res[1],1.0,3.0)
ply.write_ply('out.ply',p)
p=projection.map_to_screen(p,(0,0),res,s1,s2)
ply.write_ply('outm.ply',p)
#p=
#ply.write_ply('outp.ply',p)
