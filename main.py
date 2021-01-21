          #дом
#   1№

x=10
y=120
print(x,y)
x,y=y,x
print(x,y)


#   2№
print('Наш калькулятор принимает 4 значения! =D ')
a=float(input('Введите 1-значения !'))
b=float(input('Введите 2-значения !'))
c=float(input('Введите 3-значения !'))
d=float(input('Введите 4-значения !'))

f=a+b+c+d
print('мы добавили ваши значении  '+str(f))


git init
git add .
git commit -m "first commit"
git remote add origin https://github.com/unun9/python_lesson_2.git
git push -u origin master