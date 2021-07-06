import simple_draw as sd
point = sd.get_point(10, 100)
length = 100
def coube (point, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=90, length=length, width=3)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=180, length=length, width=3)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=-90, length=length, width=3)
    v4.draw()
coube(point=point, angle=0)

point_1 = sd.get_point(300, 100)
def pentagon (point, angle=0, lenght = 200):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=72, length=length, width=3)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=144, length=length, width=3)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=216, length=length, width=3)
    v4.draw()
    v5 = sd.get_vector(start_point=v4.end_point, angle=289, length=length, width=3)
    v5.draw()
pentagon(point=point_1, angle=0)

point_2 = sd.get_point(60, 250)
def hexagon (point, angle=0, lenght = 100):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=60, length=length, width=3)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=120, length=length, width=3)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=180, length=length, width=3)
    v4.draw()
    v5 = sd.get_vector(start_point=v4.end_point, angle=240, length=length, width=3)
    v5.draw()
    v6 = sd.get_vector(start_point=v5.end_point, angle=300, length=length, width=3)
    v6.draw()
hexagon(point=point_2, angle=0)
sd.pause()