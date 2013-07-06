
def project(point,ds,xscale,yscale):
    "Project a point in screen space to its location in voxel space."
    # eye is at 0
    xs,ys,dp = point
    xp = dp * (xs*xscale) / ds
    yp = dp * (ys*yscale) / ds
    print xs, xp, ys, yp, dp
    return (xp,yp,dp)

def project_points(points,ds,xscale,yscale,X,Y):
    projected = []
    for point in points:
        x,y,d = point
        x -= X/2
        y -= Y/2
        projected.append(project((x,y,d),ds,xscale,yscale))
    return projected


    
