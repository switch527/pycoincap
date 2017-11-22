from pycoincap import CryptoMarket as market


def test():
	m = market()
	z = m.stats()
	print z

if __name__ == '__main__':
    test()

