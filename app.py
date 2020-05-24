import pyglet
from game import player, monster, goblin, resources, life
from random import random, randint

from config import WIDTH, HEIGHT

import pickle

# load the previous score if it exists
try:
    with open('score.dat', 'rb') as file:
        score = pickle.load(file)
except:
    score = 0

pyglet.font.load("Garamond")

# Set up a window
game_window = pyglet.window.Window(WIDTH, HEIGHT)

# Create the container for our graphics
main_batch = pyglet.graphics.Batch()

# Load the main music
theme_song = pyglet.media.load('./resources/music.wav')
music = pyglet.media.Player()
music.queue(theme_song)

# Set the music for when player wins
victory_song = pyglet.media.load('./resources/win.wav')
victory_music = pyglet.media.Player()
victory_music.queue(victory_song)

# Set the music for when player loses
losing_song = pyglet.media.load('./resources/lose.wav')
losing_music = pyglet.media.Player()
losing_music.queue(losing_song)

# Initialize the player sprite
hero = player.Player(x=400, y=300, batch=main_batch)
monster_inst = monster.Monster(x=randint(0, WIDTH), y=randint(0,HEIGHT), batch=main_batch)
goblin_inst = goblin.Goblin(x=randint(0, WIDTH), y=randint(0,HEIGHT), batch=main_batch)

# Set up the two top labels, score label and lives label
score_label = pyglet.text.Label(text="Caught 0", font_name="Garamond", font_size=26, x=30, y=455, batch=main_batch)
lives_label = pyglet.text.Label(text=f"Lives {hero.lives}", font_name="Garamond", font_size=26, x=385, y=455, batch=main_batch)

# Store all objects that update each frame in a list
game_objects = [goblin_inst, hero, monster_inst]

# Tell the main window that the player object responds to events
game_window.push_handlers(hero.key_handler)

@game_window.event
def on_draw():
    game_window.clear()
    resources.background.blit(0, 0)
    main_batch.draw()

is_drawing = True  # Controls whether to show movement

def game_won():
    global is_drawing

    is_drawing = False
    music.pause()
    # Play victory music!
    victory_music.play()
    # Set up victory label
    victory_label = pyglet.text.Label(text="YOU WON!!!", font_name="Garamond", font_size=40, x=110, y=230, batch=main_batch)
    hi_score_label = pyglet.text.Label(text=f"High Score {score}", font_name="Garamond", font_size=26, x=150, y=350, batch=main_batch)

def game_lost():
    global is_drawing

    is_drawing = False
    music.pause()
    # Play losing music!
    losing_music.play()
    # Set up losing label
    losing_label = pyglet.text.Label(text="YOU LOST :(", font_name="Garamond", font_size=40, x=110, y=230, batch=main_batch)
    hi_score_label = pyglet.text.Label(text=f"High Score {score}", font_name="Garamond", font_size=26, x=150, y=350, batch=main_batch)

def update(dt):

    global score

    if is_drawing:

        for obj in game_objects:
            obj.update(dt)

        # To avoid handling collisions twice, we employ nested loops of ranges.
        # This method also avoids the problem of colliding an object with itself.
        for i in range(len(game_objects)):
            for j in range(i + 1, len(game_objects)):

                obj_1 = game_objects[0]
                obj_2 = game_objects[1]
                # add a 3rd object
                obj_3 = game_objects[2]
                # add a 4th object
                if len(game_objects) == 4:
                    obj_4 = game_objects[3] 
                if len(game_objects) == 5:
                    obj_4 = game_objects[3] 
                    obj_5 = game_objects[4] 
                # if len(game_objects) < 5:
                if len(game_objects) == 6:
                    obj_4 = game_objects[3] 
                    obj_5 = game_objects[4] 
                    obj_6 = game_objects[5]
                elif obj.name == "life" in game_objects:
                    obj_6 = obj.name == "life"             

                # Make sure the objects haven't already been killed
                if not obj_2.dead and not obj_3.dead:
                    if obj_1.collides_with(obj_2):
                        print(f"{obj_1.name} collides with {obj_2.name}")
                        obj_1.handle_collision_with(obj_2)
                        obj_2.handle_collision_with(obj_1)
                    if obj_2.collides_with(obj_3):
                        print(f"{obj_2.name} collides with {obj_3.name}")
                        obj_2.handle_collision_with(obj_3)
                        obj_3.handle_collision_with(obj_2)
                    if obj_1.collides_with(obj_3):
                        print(f"{obj_1.name} collides with {obj_3.name}")
                        obj_1.handle_collision_with(obj_3)
                        obj_3.handle_collision_with(obj_1)
                    try:
                        if obj_1.collides_with(obj_4):
                            print(f"{obj_1.name} collides with {obj_4.name}")
                            obj_1.handle_collision_with(obj_4)
                            obj_4.handle_collision_with(obj_1)
                        if obj_2.collides_with(obj_4):
                            print(f"{obj_2.name} collides with {obj_4.name}")
                            obj_2.handle_collision_with(obj_4)
                            obj_4.handle_collision_with(obj_2)
                        if obj_3.collides_with(obj_4):
                            print(f"{obj_3.name} collides with {obj_4.name}")
                            obj_3.handle_collision_with(obj_4)
                            obj_4.handle_collision_with(obj_3)
                    except UnboundLocalError:
                        pass
                    try:
                        if obj_1.collides_with(obj_5):
                            print(f"{obj_1.name} collides with {obj_5.name}")
                            obj_1.handle_collision_with(obj_5)
                            obj_5.handle_collision_with(obj_1)
                        if obj_2.collides_with(obj_5):
                            print(f"{obj_2.name} collides with {obj_5.name}")
                            obj_2.handle_collision_with(obj_5)
                            obj_5.handle_collision_with(obj_2)
                        if obj_3.collides_with(obj_5):
                            print(f"{obj_3.name} collides with {obj_5.name}")
                            obj_3.handle_collision_with(obj_5)
                            obj_5.handle_collision_with(obj_3)
                        if obj_4.collides_with(obj_5):
                            print(f"{obj_4.name} collides with {obj_5.name}")
                            obj_4.handle_collision_with(obj_5)
                            obj_5.handle_collision_with(obj_4)
                    except UnboundLocalError:
                        pass
                    try:
                        if obj_6 in game_objects:
                            if obj_1.collides_with(obj_6):
                                print(f"{obj_1.name} collides with {obj_6.name}")
                                obj_1.handle_collision_with(obj_6)
                                obj_6.handle_collision_with(obj_1)
                            if obj_2.collides_with(obj_6):
                                print(f"{obj_2.name} collides with {obj_6.name}")
                                obj_2.handle_collision_with(obj_6)
                                obj_6.handle_collision_with(obj_2)
                            if obj_3.collides_with(obj_6):
                                print(f"{obj_3.name} collides with {obj_6.name}")
                                obj_3.handle_collision_with(obj_6)
                                obj_6.handle_collision_with(obj_3)
                            if obj_4.collides_with(obj_6):
                                print(f"{obj_4.name} collides with {obj_6.name}")
                                obj_4.handle_collision_with(obj_6)
                                obj_6.handle_collision_with(obj_4)
                            if obj_5.collides_with(obj_6):
                                print(f"{obj_5.name} collides with {obj_6.name}")
                                obj_5.handle_collision_with(obj_6)
                                obj_6.handle_collision_with(obj_5)
                    except UnboundLocalError:
                        pass

        # Get rid of dead objects
        for to_remove in [obj for obj in game_objects if obj.dead]:
            # Remove the object from any batches it is a member of
            to_remove.delete()

            # Remove the object from our list
            game_objects.remove(to_remove)

            if to_remove.name == "Joe":
                new_player = player.Player(x=randint(0, WIDTH), y=randint(0, HEIGHT), batch=main_batch)
                game_objects.insert(1, new_player) #insert(1, new_player)
                game_window.push_handlers(new_player.key_handler)
                # Update lives
                hero.lives -= 1
                print("Dead")
                life_sound_effect = pyglet.media.load('./resources/loselife.wav', streaming=False)
                life_sound_effect.play()
            elif to_remove.name == "Monster":
                # Add a new monster
                new_monster = monster.Monster(x=randint(0, WIDTH), y=randint(0, HEIGHT), batch=main_batch)
                game_objects.insert(2, new_monster) #insert(2, new_monster)
                # Update score
                hero.score += 10
                gotcha_sound_effect = pyglet.media.load('./resources/points.wav', streaming=False)
                gotcha_sound_effect.play()
            elif to_remove.name == "life":
                # Update lives
                hero.lives += 1
                print("Life")
                life_sound_effect = pyglet.media.load('./resources/life.wav', streaming=False)
                life_sound_effect.play()

            score_label.text = f"Caught {hero.score}"
            lives_label.text = f"Lives {hero.lives}"

            # generate second goblin
            if hero.score == 50 and len(game_objects) == 3:
                goblin_inst = goblin.Goblin(x=randint(0, WIDTH), y=randint(0, HEIGHT), batch=main_batch)
                game_objects.insert(3, goblin_inst)

            # generate third goblin
            if hero.score == 100 and len(game_objects) == 4:
                goblin_inst = goblin.Goblin(x=randint(0, WIDTH), y=randint(0, HEIGHT), batch=main_batch)
                game_objects.insert(4, goblin_inst)

            # randomly generate 1up
            rand_num = random() <= 0.1
            if rand_num:
                life_inst = life.Life(x=randint(0, WIDTH), y=randint(0, HEIGHT), batch=main_batch)
                life_list = []
                life_list.append(life_inst)
                if len(game_objects) == 6:
                    if obj_6 not in game_objects:
                        game_objects.insert(5, life_inst)
                else:
                    if life_inst in game_objects:
                        life_list = []
                    else:
                        game_objects.extend(life_list) 
                         
            if hero.score == 500:
                if hero.score > score:
                    score = hero.score
                game_won()
                # save the score
                with open('score.dat', 'wb') as file:
                    pickle.dump(score, file)

            if hero.lives <= 0:
                if hero.score > score:
                    score = hero.score
                game_lost() 
                # save the score
                with open('score.dat', 'wb') as file:
                    pickle.dump(score, file)

if __name__ == "__main__":
    # Update the game 120 times per second
    pyglet.clock.schedule_interval(update, 1 / 120.0)

    music.play()
    # Tell pyglet to do its thing
    pyglet.app.run()
