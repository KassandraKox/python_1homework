'''Напишите программу, удаляющую из текста все слова, в которых 
присутствуют все буквы "абв".'''

text = 'Напишите пвпавбп программу, швабра удалявбющую из этого текбвста все слова, содержащие "абв"'
print(text)

def del_abv(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)
def del_avb(text):
    text = list(filter(lambda x: 'авб' not in x, text.split()))
    return " ".join(text)
def del_vab(text):
    text = list(filter(lambda x: 'ваб' not in x, text.split()))
    return " ".join(text)
def del_vba(text):
    text = list(filter(lambda x: 'вба' not in x, text.split()))
    return " ".join(text)
def del_bav(text):
    text = list(filter(lambda x: 'бав' not in x, text.split()))
    return " ".join(text)
def del_bva(text):
    text = list(filter(lambda x: 'бва' not in x, text.split()))
    return " ".join(text)
    
text = del_bav(text)   
text = del_bva(text)    
text = del_vba(text)
text = del_abv(text)
text = del_avb(text)
text = del_vab(text)
print(text)