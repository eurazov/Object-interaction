import Objects


def collision(a, b):
    return a.radius+b.radius>=Objects.dist(a.position, b.position)


def update_field(a, dt, canvas, field_width, field_height, F):
    canvas.create_rectangle(0, 0, field_width, field_height, color="white")
    for i in range(len(a)):
        a[i].move(dt)
        a[i].accelerate(dt)
        a[i].draw(canvas, "black")
        a[i].force=F
    i=0
    while i<len(a):
        j=i+1
        while j<len(a):
            if collision(a[i], a[j]):
                a[i].velocity=(a[i].mass*a[i].velocity+a[j].mass*a[j].velocity)/(a[i].mass+a[j].mass)
                a[i].mass+=a[j].mass
                a[i].radius=(a[i].radius**3+a[j].radius**3)**(1./3)
                a[i].position+=a[j].position
                a[i].position/=2
                del a[j]
                break
            a[i].interact(a[j])
            j+=1
        i+=1