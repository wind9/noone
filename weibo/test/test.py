from config import headers


def ceshi():
   return headers

__all__ = ['ceshi']

if __name__ == '__main__':
    t = ceshi()
    print("start ----")
    print(t)

