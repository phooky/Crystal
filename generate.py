import pattern
import ply
import projection

p=pattern.make_depths(800,600,10,1000)
ply.write_ply('out.ply',p)
p=projection.project_points(p,0.4,0.0001,0.0001,800,600)
ply.write_ply('outp.ply',p)
