import sys
from player import *
from Enemy import *
import random
from StaticWall import *
from DestroyableWall import *
import array
from definitions import *
import random

class ViewWindow():
    worldx = 760
    worldy = 520
    iconSize = 40
    fps = 40  # frame rate
    clock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption('Dyna Blaster')

    ok = True;
    world = pygame.display.set_mode([worldx, worldy])
    backdrop = pygame.image.load(os.path.join('Slike', 'background.jpg')).convert()
    backdropbox = world.get_rect()

    player = Player('playerup.png')  # spawn player
    # prepravila sam da se plejer pojavi na (50,50) da se ne bi preklapao sa ispisom za Score
    player.rect.x = iconSize
    player.rect.y = iconSize
    player_list = pygame.sprite.Group()
    player_list.add(player)
    steps = 10  # how fast to move

    # ovaj randint krece od 50 da se ne bi preklapali sa ispisom za SCORE
    enemy1 = Enemy(680, random.randint(iconSize, worldy-2*iconSize), 'enemy1.png')  # spawn enemy
    enemy2 = Enemy(random.randint(iconSize, worldx-iconSize*2), random.randint(iconSize, worldy-2*iconSize), 'enemy2.png')  # spawn enemy
    enemy_list = pygame.sprite.Group()  # create enemy group
    enemy_list.add(enemy1)  # add enemy to group
    enemy_list.add(enemy2)  # add enemy to group

    stWalls_list = pygame.sprite.Group()  # create static walls group
    deWalls_list = pygame.sprite.Group()  # create destroyableWalls group

    wallsPositions= make_matrix()

    # iscrtavanje okolnih zidova kroz naredne 2 for petlje
    for x in range(0, worldx, iconSize):
        stWall1 = StaticWall(x, 0)
        stWall2 = StaticWall(x, worldy - iconSize)
        stWalls_list.add(stWall1)
        stWalls_list.add(stWall2)
        wallsPositions[stWall1.rect.x][0] = 1
        wallsPositions[stWall2.rect.x][0] = 1
    for y in range(iconSize, worldy, iconSize):
        stWall3 = StaticWall(0, y)
        stWall4 = StaticWall(worldx - iconSize, y)
        stWalls_list.add(stWall3)
        stWalls_list.add(stWall4)
        wallsPositions[0][stWall3.rect.y] = 1
        wallsPositions[0][stWall4.rect.y] = 1

    # iscrtavanje unutrasnjih zidova
    for x in range(iconSize*2, worldx - iconSize*2, iconSize*2):
        for y in range(iconSize*2, worldy - iconSize*2, iconSize*2):
            stWall = StaticWall(x, y)
            wallsPositions[stWall.rect.x][stWall.rect.y] = 1
            stWalls_list.add(stWall)

    #unistivi zidovi
    for x in range(iconSize, worldx - iconSize, iconSize):
        for y in range(iconSize, worldy - iconSize, iconSize):
            if (bool(random.getrandbits(1))):
                if (wallsPositions[x][y] == 0):#ako je prazno polje
                    deWall = DestroyableWall(x, y)
                    wallsPositions[x][y] = 2#za unistive zidove
                    deWalls_list.add(deWall)


    print(wallsPositions)

    bomb_list=pygame.sprite.Group()


    while ok:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                sys.exit()
                ok = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    player.control(-steps, 0, "l")
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    player.control(steps, 0, "r")
                if event.key == pygame.K_UP or event.key == ord('w'):
                    player.control(0, -steps, "up")
                if event.key == pygame.K_DOWN or event.key == ord('x'):
                    player.control(0, steps, "down")
                if event.key == pygame.K_KP_ENTER or event.key == ord('g'):
                    player.control(0, steps, "e")


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    player.control(steps, 0, "l")
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    player.control(-steps, 0, "r")
                if event.key == pygame.K_UP or event.key == ord('w'):
                    player.control(0, steps, "up")
                if event.key == pygame.K_DOWN or event.key == ord('x'):
                    player.control(0, -steps, "down")
                if event.key == pygame.K_KP_ENTER or event.key == ord('g'):
                    player.control(player.rect.x,player.rect.y, "e")

                if event.key == ord('q'):
                    pygame.quit()
                    sys.exit()
                    ok = False

        #    world.fill(BLACK)
        world.blit(backdrop, backdropbox)

        stWalls_list.draw(world)
        deWalls_list.draw(world)

        player.update(enemy_list, world)
        player_list.draw(world)  # refresh player position

        player.show_score(world)
        player.show_lives(world)

        enemy_list.draw(world)  # refresh enemies
        for e in enemy_list:
            e.move()

        pygame.display.flip()
        clock.tick(fps)

        # def __init__(self):
        #     super().__init__()
        #     self.initUI()
        #     self.show()
        #
        # def initUI(self):
        #     self.resize(600, 600)
        #     self.setWindowTitle('Dyna Blaster')
        #     self.setWindowIcon(QIcon('projakat_slika1.jpg'))
        #
        #     palette = QPalette()
        #     palette.setBrush(10, Qt.darkGray)
        #     self.setPalette(palette)
        #
        #     self.show()
        #
        # def closeEvent(self, event):
        #     reply = QMessageBox.question(self, 'Dyna Blaster', 'Are you sure you want to exit?',
        #                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        #
        #     if reply == QMessageBox.Yes:
        #         event.accept()
        #     else:
        #         event.ignore()
        #
        # def paintEvent(self, e):
        #     qp = QPainter()
        #     qp.begin(self)
        #     self.drawBrushes(qp)
        #     qp.end()
        #
        # def drawBrushes(self, qp):
        #     nullbrush = QBrush()
        #     emptybrush = QBrush(Qt.darkGreen)
        #     wallImage = QImage("IndestructableWall.jpg")
        #     wallbrush = QBrush()
        #     wallbrush.setTextureImage(wallImage)
        #
        #     wallImage2 = QImage("Wall.jpg")
        #     wallbrush2 = QBrush()
        #     wallbrush2.setTextureImage(wallImage2)
        #
        #     bombImage = QImage("Bomb.jpg")
        #     bombBrush = QBrush()
        #     bombBrush.setTextureImage(bombImage)
        #
        #     # iscrtevanje na tabli
        #     w = 0
        #     h = 0
        #     offset = 40
        #     for i in range(0, height):
        #         for j in range(0, width):
        #             if (Kind(Matrix[i][j]) == Kind.Empty):
        #                 qp.setBrush(emptybrush)
        #             elif (Kind(Matrix[i][j]) == Kind.IndestructibleWall):
        #                 qp.setBrush(wallbrush)
        #             elif (Kind(Matrix[i][j]) == Kind.Wall):
        #                 qp.setBrush(wallbrush2)
        #             qp.drawRect(w, h, 40, 40)
        #             w = w + offset
        #         w = 0
        #         h = h + offset

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = ViewWindow()
        sys.exit(app.exec_())
