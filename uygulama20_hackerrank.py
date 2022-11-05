#find the percentage (yanlış anladığım şekliyle)--> Bir isim için 3 not isteme mantığım
# ve bu notları bir listeye atıp isimle birlikte dict haline getirmek.
# scores listesinin bulunduğu konum çok önemli. Eğer içerdeki for un içinde olsa her bir
# girilen not için ayrı liste oluşturulur ilk for dan önce oluştursak tüm öğrencilerin 
# notları tek bir listeye konulacak vs  
sum = 0   
student_marks = {}  
n = int(input())
for x in range(n):
    name = input()
    scores = list()
    for mark in range(3) :
        mark = float(input())
        scores.append(mark)
    student_marks[name] = scores
print(student_marks)    
query_name = input()
for mark in student_marks[query_name] :
    sum += mark
print(sum/3)

#İstenen haliyle: Tek bi satırda string ifade giriyoruz ve bu ifadeleri dict şekline sokuyoruz.
sum = 0
n = int(input())
student_marks = {}
scores = []
for _ in range(n):
    info = input().split()
    name = info[0]
    scores = info[1:4]
    student_marks[name] = scores
query_name = input()
for mark in student_marks[query_name] :  
    sum += float(mark)
print(sum/3)   
    