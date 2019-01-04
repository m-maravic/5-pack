import sys
from player import *
from Enemy import *
import random

class ViewWindow ():
    worldx = 720
    worldy = 500

    fps = 40        # frame rate
    clock = pygame.time.Clock()
    pygame.init()

    ok = True;
    world = pygame.display.set_mode([worldx, worldy])
    backdrop = pygame.image.load(os.path.join('Slike','pozadina.jpg')).convert()
    backdropbox = world.get_rect()
    player = Player('playerup.png')   # spawn player
    player.rect.x = 0
    player.rect.y = 0
    player_list = pygame.sprite.Group()
    player_list.add(player)
    steps = 10      # how fast to move

    enemy1 = Enemy(random.randint(0,720), random.randint(0,500), 'enemy1.png')  # spawn enemy
    enemy2 = Enemy(random.randint(0,720), random.randint(0,500), 'enemy2.png')  # spawn enemy
    enemy_list = pygame.sprite.Group()  # create enemy group
    enemy_list.add(enemy1)  # add enemy to group
    enemy_list.add(enemy2)  # add enemy to group

    while ok:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
                ok = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    player.control(-steps,0,"l")
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    player.control(steps,0,"r")
                if event.key == pygame.K_UP or event.key == ord('w'):
                    player.control(0, -steps,"up")
                if event.key == pygame.K_DOWN or event.key == ord('x'):
                    player.control(0, steps, "down")

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    player.control(steps,0, "l")
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    player.control(-steps,0, "r")
                if event.key == pygame.K_UP or event.key == ord('w'):
                    player.control(0, steps, "up")
                if event.key == pygame.K_DOWN or event.key == ord('x'):
                    player.control(0, -steps, "down")
                if event.key == ord('q'):
                    pygame.quit()
                    sys.exit()
                    ok = False

    #    world.fill(BLACK)
        world.blit(backdrop, backdropbox)
        player.update(enemy_list)
        player_list.draw(world) #refresh player position

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