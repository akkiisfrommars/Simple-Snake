import turtle
import time
import random
import snake
import food
import gold
import poison


# noinspection PyPep8Naming
def play_game():
    # Initialize the snake and screen
    snake_instance = snake.Snake()
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(width=530, height=600)
    screen.title("Snake Game")
    screen.tracer(0)
    COORD = 250

    # Initialize the food
    food_instance = food.Food()

    # Initialize the gold and poison but don't display it yet
    gold_instance = gold.Gold()
    gold_instance.hideturtle()

    poison_instance = poison.Poison()
    poison_instance.hideturtle()

    # Drawing a border
    t = turtle.Turtle()
    t.color("red")
    t.pensize(5)
    t.penup()
    t.goto(-COORD, COORD)
    t.pendown()
    t.goto(COORD, COORD)
    t.goto(COORD, -COORD)
    t.goto(-COORD, -COORD)
    t.goto(-COORD, COORD)
    t.penup()
    t.hideturtle()
    screen.update()

    # Random info
    # Made by Akhil
    draw_name = turtle.Turtle()
    draw_name.color("white")
    draw_name.penup()
    draw_name.hideturtle()
    draw_name.goto(-250, -285)
    draw_name.write("Made by: akkiisfrommars", font=("Cosmic Sans MS", 20, "normal"))

    # Version
    draw_ver = turtle.Turtle()
    draw_ver.color("white")
    draw_ver.penup()
    draw_ver.hideturtle()
    draw_ver.goto(195, -285)
    draw_ver.write("Version 1.0", font=("Cosmic Sans MS", 10, "normal"))

    # end of random info

    # Setting up key listeners
    screen.listen()
    screen.onkey(snake_instance.up, "Up")
    screen.onkey(snake_instance.down, "Down")
    screen.onkey(snake_instance.left, "Left")
    screen.onkey(snake_instance.right, "Right")
    screen.onkey(snake_instance.pause, "p")

    # Score
    score = 0
    font_size = 30
    draw_score = turtle.Turtle()
    draw_score.color("white")
    draw_score.penup()
    draw_score.hideturtle()
    draw_score.goto(125, 260)
    draw_score.write(f"Score: {score}", font=("Fixedsys", font_size, "normal"))

    draw_pauses = turtle.Turtle()
    draw_pauses.color("white")
    draw_pauses.penup()
    draw_pauses.hideturtle()
    draw_pauses.goto(0, -285)
    draw_pauses.write(f"Pauses left: {snake_instance.number_of_pauses}", font=("Cosmic Sans MS", 20, "normal"))

    game_is_on = True
    while game_is_on:
        # draw pauses
        draw_pauses.clear()
        draw_pauses.write(f"Pauses left: {snake_instance.number_of_pauses}", font=("Cosmic Sans MS", 20, "normal"))
        if score < 10:
            if random.randint(1, 100) == 50:
                poison_instance.refresh()
                poison_instance.showturtle()
        elif score <= 10:
            if random.randint(1, 20) == 5:
                poison_instance.refresh()
                poison_instance.showturtle()
        elif score >= 50:
            if random.randint(1, 10) == 2:
                poison_instance.refresh()
                poison_instance.showturtle()

        screen.update()
        time.sleep(0.2)
        snake_instance.move()

        # Detect collision with food
        if snake_instance.head.distance(food_instance) < 22:
            # Spawn gold
            if not gold_instance.isvisible() and random.randint(1, 10) == 7:
                gold_instance.refresh()
                gold_instance.showturtle()
            if score > 99:
                font_size = 25
            score += 1
            draw_score.clear()
            draw_score.write(f"Score: {score}", font=("Fixedsys", font_size, "normal"))
            snake_instance.create_segment()
            food_instance.refresh()

        # Detect collision with gold
        if gold_instance.isvisible() and snake_instance.head.distance(gold_instance) < 22:
            if score > 99:
                font_size = 25
            score += 10
            draw_score.clear()
            draw_score.write(f"Score: {score}", font=("Fixedsys", font_size, "normal"))
            for _ in range(10):
                snake_instance.create_segment()
            gold_instance.hideturtle()

        # Detect collision with poison
        if poison_instance.isvisible() and snake_instance.head.distance(poison_instance) < 22:
            if score > 99:
                font_size = 25
            score -= 10
            if score < 0:
                game_is_on = False
            draw_score.clear()
            draw_score.write(f"Score: {score}", font=("Fixedsys", font_size, "normal"))
            for _ in range(10):
                snake_instance.delete_segment()
            poison_instance.hideturtle()

        # Detect collision with wall
        if snake_instance.head.xcor() > COORD or snake_instance.head.xcor() < -COORD or snake_instance.head.ycor() > COORD or snake_instance.head.ycor() < -COORD:
            game_is_on = False

        # Detect collision with self
        for segment in snake_instance.segments[1:]:
            if snake_instance.head.distance(segment) < 10:
                game_is_on = False

    # Display "GAME OVER" message
    draw2 = turtle.Turtle()
    draw2.penup()
    draw2.hideturtle()
    draw2.goto(-250, 260)
    draw2.color("white")
    draw2.write("GAME OVER", font=("Courier", 30, "normal"))

    # Ask to play again
    play_again = screen.textinput("Game Over", "Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes" or play_again.lower() == "y" or play_again.lower() == "yeah":
        screen.clear()
        play_game()
    else:
        screen.bye()

# Start the game


play_game()
