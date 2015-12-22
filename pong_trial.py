
""" use mouse to control the paddle"""
import math
import pygame
import random

__author__ = 'anudeep'


class Particle(object):
    color = (255, 255, 255)  # color of the ball

    def __init__(self, (x, y), size):
        self.size = size
        (self.x, self.y) = (x, y)
        self.y_initial = self.y  # just for reference, store the initial value of y

        self.gravity = 0  # gravity is always downwards so no need of angle,it is always pi/2
        self.angle = random.uniform(0, math.pi/4)
        self.velocity = 10  # random.randint(0,20)
        # ....split velocity into component vectors ....
        self.velocity_x = 0  # round1(math.cos(self.angle) * self.velocity, 2)  # velocity at t=0
        self.velocity_y = 0  # round1(math.sin(self.angle) * self.velocity,2)  # velocity at t=0
        self.elasticity = 1
        self.refer = 0
        self.adjustment = 0
        self.friction=0.99

    def move(self):

        self.velocity_x = round(math.cos(self.angle)*self.velocity, 2)
        self.velocity_y = round(math.sin(self.angle) * self.velocity, 2)
        self.velocity_y+=self.gravity
        self.x += round(self.velocity_x,2)
        self.y += round(self.velocity_y,2)

        if self.x > width - self.size:
            self.x=width-self.size
            self.angle = math.pi - self.angle  # angle after collision
            return 1
        elif self.x < self.size:
            self.x = self.size
            self.angle = math.pi - self.angle  # angle after collision
            return 2
        if self.y > height - self.size:
            self.y = height - self.size
            self.angle = 2 * math.pi - self.angle  # angle after collision
        elif self.y < self.size:
            self.y = self.size
            self.angle = 2 * math.pi - self.angle  # angle after collision

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)


class Bat:
    def __init__(self,length,breadth,x,y):
        self.length=length
        self.breadth=breadth
        self.x=x
        self.y=y
        self.amount=0

    def draw(self):
        pygame.draw.rect(screen,(255,255,255),(self.x,self.y,self.length,self.breadth))

    def move(self,dest):
        if dest<=height/2:
            dy=dest-self.y
            self.amount=dy/15
            self.y+=int(self.amount)
            # print self.amount,dest
            if int(2*self.y+self.breadth)>=int(dest):
                self.amount=0
            # boundary restrictions
            if self.y<0:
                self.y=0
            elif self.y+self.breadth>height:
                self.y=height-self.breadth
        else:
            dy=dest-self.y
            self.amount=dy/15
            self.y+=int(self.amount)
            # print self.amount,dest
            if 0<int(self.y+self.breadth-dest)<10:
                self.amount=0
            # boundary restrictions
            if self.y<0:
                self.y=0

            elif self.y+self.breadth>height:
                self.y=height-self.breadth


if __name__ == '__main__':
    elasticity=1

    def collide(p1,bat):
        half_of_bat=bat.y+bat.breadth/2

        def code_reuse(bat_no):
            if math.sin(p1.angle)>0:  # if the ball is in 1st or 2nd quadrant
                if p1.y>half_of_bat:
                    if p1.y>half_of_bat+bat.breadth/4:
                        print 'greater'
                        p1.velocity=12
                        if bat_no==1:
                            p1.angle=math.radians(random.uniform(70,45))
                        else:
                            p1.angle=math.radians(random.uniform(110,135))
                    else:
                        print 'lesser'
                        p1.velocity=8
                        if bat_no==1:
                            p1.angle=math.radians(random.uniform(45,0))
                        else:
                            p1.angle=math.radians(random.uniform(135,180))
                if p1.y<half_of_bat:
                    if p1.y<half_of_bat-bat.breadth/4:
                        p1.velocity=12
                        if bat_no==1:
                            p1.angle=math.radians(random.uniform(290,315))
                        else:
                            p1.angle=math.radians(random.uniform(200,225))
                    else:
                        p1.velocity=8
                        if bat_no==1:
                            p1.angle=math.radians(random.uniform(315,360))
                        else:
                            p1.angle=math.radians(random.uniform(180,200))
            elif math.sin(p1.angle)<0:  # if the ball is in 3rd or 4th quadrant
                if p1.y>half_of_bat:
                    if p1.y>half_of_bat+bat.breadth/4:
                        p1.velocity=12
                        if bat_no==1:
                            p1.angle=math.radians(random.uniform(315,360))
                        else:
                            p1.angle=math.radians(random.uniform(110,135))
                    else:
                        p1.velocity=8
                        if bat_no==1:
                            p1.angle=math.radians(random.uniform(290,315))
                        else:
                            p1.angle=math.radians(random.uniform(135,180))

                if p1.y<half_of_bat:
                    if p1.y<half_of_bat-bat.breadth/4:
                        p1.velocity=12
                        if bat_no==1:
                            p1.angle=math.radians(random.uniform(290,315))
                        else:
                            p1.angle=math.radians(random.uniform(200,225))
                    else:
                        p1.velocity=8
                        if bat_no==1:
                            p1.angle=math.radians(random.uniform(315,360))
                        else:
                            p1.angle=math.radians(random.uniform(180,200))
            else:
                p1.angle=-p1.angle
                p1.velocity*=0.5

        if bat.x==0:
            dx=abs(bat.x+bat.length-p1.x)
            if bat.y<=p1.y+p1.size<=bat.y+bat.breadth and dx<=p1.size:
                p1.x=bat.x+bat.length+p1.size+1
                code_reuse(1)
        else:
            dx=abs(bat.x-p1.x)
            if dx<=p1.size and bat.y<=p1.y+p1.size<=bat.y+bat.breadth+p1.size:
                p1.x=bat.x-p1.size-1
                code_reuse(2)
                return p1.x,p1.y,p1.angle

    def findparticle(x, y):
        for p in (bat1,bat2):
            if x in range(p.x,p.x+p.length):
                return p

    selected_particle = None
    mouse_x_prev = 0
    mouse_y_prev = 0
    speed_x = 0
    speed_y = 0
    running = True
    background_color = (0, 0, 0)  # black
    no_of_particles = 1
    my_particles = []
    score1="0"
    score2='0'
    (width, height) = (640, 480)
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('gravity ball')
    bat1=Bat(20,100,0,0)
    bat2=Bat(20,100,width-20,0)
    amount=4
    y_fut=0
    ref_list=[]
    for n in range(no_of_particles):
        x = random.randint(0, width)
        y = 100  # random.randint(0,height)
        size = 15  # random.randint(0,30)
        my_particles.append(Particle((x, y), size))
    particle=my_particles[0]

    while running:
        pygame.draw.rect(screen,(255,255,255),[250,0,100,30])
        bat1.draw()
        bat2.draw()
        particle.draw()
        myfont=pygame.font.SysFont("monospace",15)
        label=myfont.render(score1,1,(0,0,0))
        label2=myfont.render(score2,1,(0,0,0))
        screen.blit(label, (260,5))
        screen.blit(label2,(320,5))
        score_update=particle.move()
        if score_update==1:
            score1=str(int(score1)+1)
        elif score_update==2:
            score2=str(int(score2)+1)
        if score_update in [1,2]:
            pause=True
            pygame.display.update()
            particle.__init__((10,y),size)
            while pause:
                e=pygame.event.wait()
                if e.type==pygame.KEYUP:
                    pause=False
                elif e.type==pygame.QUIT:
                    running=False
                    break
        ref_list=collide(particle,bat2)
        collide(particle,bat1)
        if ref_list is None:
            bat1.move(y_fut)
        else:
            temp_fut=ref_list[0]*math.tan(ref_list[2])
            y_fut=ref_list[1]-temp_fut
            if y_fut>height:
                dy=y_fut-height
                y_fut=height-dy
            elif y_fut<0:
                y_fut=abs(y_fut)
        pygame.display.update()
        screen.fill(background_color)  # fill the window with background color

        # pygame.time.delay(90)
        clock.tick(60)  # force pygame for 60fps

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # when pressed close button,quit
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # print 'mouse', mouse_x, mouse_y
                selected_particle = findparticle(mouse_x, mouse_y)
            elif event.type == pygame.MOUSEBUTTONUP:
                selected_particle = None
                # print "Button up", speed_x, speed_y
            if selected_particle:
                new_mouse_x, new_mouse_y = pygame.mouse.get_pos()
                change=new_mouse_y-mouse_y
                selected_particle.y+= change
                mouse_y=new_mouse_y
                if selected_particle.y<=0:
                    selected_particle.y=0
                if selected_particle.y+selected_particle.breadth>=height:
                    selected_particle.y=height-selected_particle.breadth
                # set boundaries for the selected particle
                collide(particle,selected_particle)