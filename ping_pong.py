import turtle


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 5
PADDLE_HEIGHT = 1
PADDLE_MOVE = 30
BALL_MOVE = 10
BALL_SPEEDUP = 1.05


def setup_paddle(position_x: int) -> turtle.Turtle:
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=PADDLE_HEIGHT, stretch_len=PADDLE_WIDTH)
    paddle.penup()
    paddle.goto(position_x, 0)
    return paddle


def setup_ball() -> turtle.Turtle:
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = BALL_MOVE  # type: ignore[attr-defined]
    ball.dy = BALL_MOVE  # type: ignore[attr-defined]
    return ball


def main() -> None:
    window = turtle.Screen()
    window.title("Ping Pong")
    window.bgcolor("black")
    window.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    window.tracer(0)

    paddle_left = setup_paddle(-350)
    paddle_right = setup_paddle(350)
    ball = setup_ball()

    score_left = 0
    score_right = 0

    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write(
        "Links: 0  Rechts: 0",
        align="center",
        font=("Courier", 24, "normal"),
    )

    def paddle_left_up() -> None:
        y = paddle_left.ycor()
        if y < 250:
            paddle_left.sety(y + PADDLE_MOVE)

    def paddle_left_down() -> None:
        y = paddle_left.ycor()
        if y > -240:
            paddle_left.sety(y - PADDLE_MOVE)

    def paddle_right_up() -> None:
        y = paddle_right.ycor()
        if y < 250:
            paddle_right.sety(y + PADDLE_MOVE)

    def paddle_right_down() -> None:
        y = paddle_right.ycor()
        if y > -240:
            paddle_right.sety(y - PADDLE_MOVE)

    window.listen()
    window.onkeypress(paddle_left_up, "w")
    window.onkeypress(paddle_left_down, "s")
    window.onkeypress(paddle_right_up, "Up")
    window.onkeypress(paddle_right_down, "Down")

    while True:
        window.update()

        ball.setx(ball.xcor() + ball.dx)  # type: ignore[attr-defined]
        ball.sety(ball.ycor() + ball.dy)  # type: ignore[attr-defined]

        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1  # type: ignore[attr-defined]

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1  # type: ignore[attr-defined]

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx = -BALL_MOVE  # type: ignore[attr-defined]
            score_left += 1
            pen.clear()
            pen.write(
                f"Links: {score_left}  Rechts: {score_right}",
                align="center",
                font=("Courier", 24, "normal"),
            )

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx = BALL_MOVE  # type: ignore[attr-defined]
            score_right += 1
            pen.clear()
            pen.write(
                f"Links: {score_left}  Rechts: {score_right}",
                align="center",
                font=("Courier", 24, "normal"),
            )

        if (
            340 < ball.xcor() < 350
            and paddle_right.ycor() - 50 < ball.ycor() < paddle_right.ycor() + 50
        ):
            ball.setx(340)
            ball.dx *= -BALL_SPEEDUP  # type: ignore[attr-defined]

        if (
            -350 < ball.xcor() < -340
            and paddle_left.ycor() - 50 < ball.ycor() < paddle_left.ycor() + 50
        ):
            ball.setx(-340)
            ball.dx *= -BALL_SPEEDUP  # type: ignore[attr-defined]


if __name__ == "__main__":
    main()
