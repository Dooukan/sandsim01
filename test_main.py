import os
import unittest
import pygame as pg

os.environ["SDL_VIDEODRIVER"] = "dummy"

from main import Game

class TestGameUX(unittest.TestCase):
    def setUp(self):
        pg.init()
        self.game = Game()

    def tearDown(self):
        pg.quit()

    def test_window_caption(self):
        self.game.update()
        caption = pg.display.get_caption()[0]
        self.assertEqual(caption, "Snow Simulation | Left Click: Add Snow | R / F5: Reset | Esc: Quit")

    def test_check_events_quit_on_escape(self):
        pg.event.post(pg.event.Event(pg.KEYDOWN, key=pg.K_ESCAPE))
        with self.assertRaises(SystemExit):
            self.game.check_events()

if __name__ == "__main__":
    unittest.main()
