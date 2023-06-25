from turtle import * 

speed(12)
color("red", "yellow")
begin_fill()

for _ in range(18):
    right(20)

    for _ in range(2):
        forward(200)
        right(90)
        forward(100)
        right(90)

end_fill()
done()