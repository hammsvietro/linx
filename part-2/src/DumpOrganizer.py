import DumpManager
import json

def jsonWriter(dump):

    with open("update.json", "a") as f:
        json.dump(dump,f, indent=3, separators=(',', ': '))
        print("update.json created")
        f.close()


def NewDump(dump):

    output=[]

    for check in dump:
        if check[1] == "You got a 200":
            productId = check[0]['productId']
            image = check[0]['image']

            if len(output) == 0:
                output.append({
                "productId": productId,
                "images": [image]
                })

            repeated = False

            for line in output:

                if line["productId"] == productId:
                    repeated = True
                    if len(line['images']) < 3:
                        line['images'].append(image)

            if repeated is False:
                output.append({
                "productId": productId,
                "images": [image]
                })




    return output
