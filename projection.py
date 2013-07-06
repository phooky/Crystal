
def project(point,ds):
    "Project a point in screen space to its location in voxel space."
    # eye is at 0
    xs,ys,dp = point
    xp = dp * xs / ds
    yp = dp * ys / ds
    return (xp,yp,dp)

def map_to_screen(points,o1,o2,s1,s2):
    mapped = []
    od = (float(o2[0]-o1[0]),float(o2[1]-o1[1]))
    sd = (s2[0]-s1[0],s2[1]-s1[1])
    for p in points:
        x,y,d=p
        x = (((x-o1[0])/od[0])*sd[0])+s1[0]
        y = (((y-o1[1])/od[1])*sd[1])+s1[1]
        mapped.append((x,y,d))
    return mapped

        
def project_points(points,ds):
    projected = []
    for point in points:
        projected.append(project(point,ds))
    return projected


    
