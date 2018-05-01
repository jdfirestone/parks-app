from flask_frozen import Freezer
# instead of routes, use the name of the file that runs YOUR Flask app
from parks import app

app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

@freezer.register_generator
def detail():
        yield '/park/Glacier-Bay'
        yield '/park/Katmai'
        yield '/park/Kenai-Fjords'
        yield '/park/Lake-Clark'
        yield '/park/Denali'
        yield '/park/Kobuk-Valley'
        yield '/park/Gates-of-the-Arctic'
        yield '/park/American-Samoa'
        yield '/park/Saguaro'
        yield '/park/Petrified-Forest'
        yield '/park/Grand-Canyon'
        yield '/park/Hot-Springs'
        yield '/park/Joshua-Tree'
        yield '/park/Channel-Islands'
        yield '/park/Sequoia'
        yield '/park/Pinnacles'
        yield '/park/King-Canyon'
        yield '/park/Yosemite'
        yield '/park/Lassen-Volcanic'
        yield '/park/Redwood'
        yield '/park/Death-Valley'
        yield '/park/Black-Canyon-of-the-Gunnison'
        yield '/park/Mesa-Verde'
        yield '/park/Great-Sand-Dunes'
        yield '/park/Rocky-Mountain'
        yield '/park/Biscayne'
        yield '/park/Dry-Tortugas'
        yield '/park/Everglades'
        yield '/park/Hawaii-Volcanoes'
        yield '/park/Haleakala'
        yield '/park/Mammoth-Cave'
        yield '/park/Acadia'
        yield '/park/Isle-Royale'
        yield '/park/Voyageurs'
        yield '/park/Gateway-Arch'
        yield '/park/Glacier'
        yield '/park/Great-Basin'
        yield '/park/Carlsbad-Caverns'
        yield '/park/Theodore-Roosevelt'
        yield '/park/Cuyahoga-Valley'
        yield '/park/Crater-Lake'
        yield '/park/Congaree'
        yield '/park/Badlands'
        yield '/park/Wind-Cave'
        yield '/park/Great-Smoky-Mountains'
        yield '/park/Big-Bend'
        yield '/park/Guadalupe-Mountains'
        yield '/park/Virgin-Islands'
        yield '/park/Bryce-Canyon'
        yield '/park/Canyonlands'
        yield '/park/Zion'
        yield '/park/Capitol-Reef'
        yield '/park/Shenandoah'
        yield '/park/Mount-Rainier'
        yield '/park/Shenandoah'
        yield '/park/Olympic'
        yield '/park/North-Cascades'
        yield '/park/Grand-Teton'
        yield '/park/Yellowstone'
        yield '/park/Wrangell-St-Elias'
        yield '/park/Arches'



if __name__ == '__main__':
    freezer.freeze()
