import pattern
import ply

ply.write_ply('out.ply',pattern.make_depths(800,600,0,1000))
