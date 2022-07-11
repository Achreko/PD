from tile_generator import Tile_generator
import camera

if __name__ == "__main__":
    tile_generator = Tile_generator()
    tile_generator.generate()
    fname = tile_generator.save_res()
    camera.run_camera(fname)