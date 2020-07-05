import neat
import pygame

import json
import os
import random


from base import Base
from bird import Bird
from pipe import Pipe
from score import Score


class Ai:
    def __init__(self, genomes, config):
        # Window setup
        self.width = 310
        self.height = 510
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Neat training')
        self.clock = pygame.time.Clock()

        #  Images setup
        self.groundy = self.height - 100
        self.x_speed = -4
        self.background = pygame.transform.scale(pygame.image.load(os.path.join(
            '..', 'assets', 'sprites', 'background-day.png')), (self.width, self.height))

        #  Entities setup
        self.birds = []
        self.pipes = [Pipe(self.width + 50, random.randint(60, self.groundy - 150), self.x_speed),
                      Pipe(self.width + 250, random.randint(60, self.groundy - 150), self.x_speed)]
        self.score = Score()
        self.base = Base(self.groundy, self.x_speed)

        #  Sound setup
        pygame.mixer.init()

        #  Neat setup
        self.genomes = genomes
        self.config = config
        self.nets = []
        self.ge = []
        self.scores = []
        self.fitnesses = []
        for _, genome in self.genomes:
            net = neat.nn.FeedForwardNetwork.create(genome, config)
            self.nets.append(net)
            self.birds.append(Bird(230, 350))
            genome.fitness = 0
            self.ge.append(genome)
        self.fitness()

    def fitness(self):
        """
        Tests the birds and get the best genomes
        """
        while True:
            self.clock.tick(60)

            #  See if window was closed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            #  Get next pipe index
            pipe_ind = 0
            if len(self.birds) > 0:
                if len(self.pipes) > 1 and self.birds[0].x > self.pipes[0].x + self.pipes[0].width:
                    pipe_ind = 1
            else:
                break

            for x, bird in enumerate(self.birds):
                self.ge[x].fitness += 1

                #  For each bird, check if it must jump
                inputs = bird.y_speed, self.x_speed, abs(
                    bird.y - self.pipes[pipe_ind].y), abs(bird.y - self.pipes[pipe_ind].bottom), abs(bird.x - self.pipes[pipe_ind].x)
                output = self.nets[x].activate(inputs)

                if output[0] > 0.5:
                    bird.jump()

                #  Check i the bird is dead
                if bird.collide(self.win, self.pipes):

                    self.ge[x].fitness -= 10

                    #  Kill bird and add its fitness and score to lists
                    bird.die()
                    self.scores.append(self.score.value)
                    self.fitnesses.append(self.ge[x].fitness)

                    #  Change genomes
                    self.birds.pop(x)
                    self.nets.pop(x)
                    self.ge.pop(x)

                    #  If it was the last bird, write fitnesses and scores in a file
                    if len(self.birds) == 0:
                        self.write_records()

            for pipe in self.pipes:
                #  Update score if needed
                for bird in self.birds:
                    if bird.x >= pipe.x and not pipe.passed:
                        for g in self.ge:
                            g.fitness += 10
                        self.score.increase()
                        pipe.passed = True
                #  Replace pipe if needed
                if pipe.x <= - pipe.width:
                    pipe.x = 350
                    possible_y = [random.randint(60, self.height - 250) for _ in range(100)]
                    y_index = random.randint(0, 99)
                    new_y = possible_y[y_index]
                    pipe.y = new_y
                    pipe.passed = False

            self.x_speed = -4 - self.score.value * 0.01
            self.draw()

    def draw(self):
        """
        Draw everything on the screen
        Returns:
            None
        """
        self.win.blit(self.background, (0, 0))
        for pipe in self.pipes:
            pipe.draw(self.win)
        self.base.draw(self.win)
        self.score.draw(self.win, self.width // 2, 40)
        for bird in self.birds:
            bird.draw(self.win)
        pygame.display.update()

    def write_records(self):
        """
        Writes the data from the generation into the json file.
        It is called every generation for the case in wich a bird
        gets invincible, this way the data won't be lost
        Returns:
            None
        """
        #  Get scores min, mean and max
        scores_dict = {'min': min(self.scores), 'mean': sum(self.scores) /
                       len(self.scores), 'max': max(self.scores)}

        #  Get fitness min, mean and max
        fitness_dict = {'min': min(self.fitnesses), 'mean': sum(self.fitnesses) /
                        len(self.fitnesses), 'max': max(self.fitnesses)}

        #  Create dictionary and dump it into file
        scores[f'gen_{len(scores)}'] = {'scores': scores_dict, 'fitness': fitness_dict}
        with open('scores.json', mode='w') as records:
            json.dump(scores, records, indent=2)


def main():

    #  Get config path and generate configurations for the neural network
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')

    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    #  Create population and reporter
    population = neat.Population(config)
    population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    population.add_reporter(stats)

    #  Train and evolve population
    population.run(Ai, 100)


if __name__ == '__main__':
    #  Scores dictionary
    scores = {}
    main()
