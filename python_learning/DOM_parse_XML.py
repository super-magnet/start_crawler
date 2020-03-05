import xml.dom.minidom
document_tree = xml.dom.minidom.parse('storehouse.xml')
collection = document_tree.documentElement
print(collection.toxml())
goods = collection.getElementsByTagName('goods')
goods_record = []
for good_object in goods:
    if good_object.hasAttribute('category'):
        goods_record.append(good_object.getAttribute('category'))
    name = good_object.getElementsByTagName('name')[0]
    goods_record.append(name.childNodes[0].data)
    amount = good_object.getElementsByTagName('amount')[0]
    goods_record.append(amount.childNodes[0].data)
    price = good_object.getElementsByTagName('price')[0]
    goods_record.append(price.childNodes[0].data)

print(goods_record)
