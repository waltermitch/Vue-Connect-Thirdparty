from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABdTV7Ggrx4ArIw5bFu74J2Ysv3z4Gs46f6eYj-XLC_EiBFDIbx7mSOAbD6dxOJt_L7JPm_qpTjhOUEGB0NGVQ_XTwPlTU4tXuWEmb4VSOvDXTHgv2QY3QMpGC9MtZcnEJWv_8ms_GLvLXqFcBECfHWccBz_B6lhE2dMd22ClUHHIKsIOg='

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
