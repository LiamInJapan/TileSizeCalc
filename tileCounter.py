# Tile gen counter
import argparse

class TileCounter:

	# width / height
	ios_screen_sizes = {
		"iPhone5"  : [1136, 640],
		"iPhone6"  : [1334, 750],
		"iPhone6+" : [2208, 1242],
		"iPadMini" : [2048, 1536],
		"iPadAir"  : [2048, 1536],
		"iPadPro"  : [2732, 2048],
	}

	def __init__(self, desiredScreensWidth, desiredScreensHeight, tileSize):
		
		self.tileSize = tileSize

		for key, value in self.ios_screen_sizes.iteritems():
			
			widthCounter = 0
			heightCounter = 0
			desiredWidth = desiredScreensWidth*value[0]
			desiredHeight = desiredScreensHeight*value[1]
			requiredWidth = 0
			requiredHeight = 0

			while (widthCounter < desiredWidth):
				widthCounter += tileSize

			while (heightCounter < desiredHeight):
				heightCounter += tileSize

			print key + ":", value
			print "%s: required image width: %d required image height: %d" % (key, widthCounter, heightCounter)

parser = argparse.ArgumentParser()

parser.add_argument("desiredWidth", help="the desired number of screens width", type=int)
parser.add_argument("desiredHeight", help="the desired number of screens height", type=int)
parser.add_argument("tileSize", help="the desired size of the tile", type=int)

args = parser.parse_args()
tc = TileCounter(args.desiredWidth, args.desiredHeight, args.tileSize)
