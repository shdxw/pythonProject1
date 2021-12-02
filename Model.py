import torch


class Model(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating model')
            cls._instance = torch.hub.load('ultralytics/yolov5', 'yolov5x')
            # Put any initialization here.
        return cls._instance


if __name__ == '__main__':
    #print('cuda:0' if torch.cuda.is_available() else 'cpu')
    cuda = torch.device('cuda')  # Default CUDA device
    cuda0 = torch.device('cuda:0')
    cuda2 = torch.device('cuda:2')  # GPU 2 (these are 0-indexed)

    x = torch.tensor([1., 2.], device=cuda0)
    # x.device is device(type='cuda', index=0)
    y = torch.tensor([1., 2.]).cuda()
