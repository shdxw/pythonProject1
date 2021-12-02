import base64
import io
import json
from PIL import Image
from bottle import run, request
import bottle

from Model import Model

bottle.BaseRequest.MEMFILE_MAX = 1000000 * 25 #максимальный размер боди в байтах
application = bottle.app()


@application.route("/api", method=['POST'])
def api():
    text = request.json['data']
    urls = []
    for item in text:
        urls.append(item['item'])
    print("received items")
    bottle.response.content_type = 'application/json'
    bottle.response.status = 200
    bottle.response.body = json.dumps(detect(urls))
    return bottle.response


def detect(imgs):
    decode_imgs = []
    for img in imgs:
        imgdata = base64.b64decode(img)
        decode_imgs.append(Image.open(io.BytesIO(imgdata)))
    # Model
    model = Model()
    model.multi_label = False
    results = model(decode_imgs)
    results.save()
    print(results.pandas())
    res = []
    for x in results.pandas().xyxy:
        cars = list(filter(lambda c: c in ['bus', 'car', 'motorcycle', 'truck'], list(x['name'])))
        res.append({'count': len(cars)})
    res = {'data': res}
    print(res)
    return res


if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True)



