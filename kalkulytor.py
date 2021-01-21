print('fghjtresdfghjk')
znak= int(input('выбирите что делать с числами: \n"плюс клв 1","минус клв 2 ","умнажения клв 3","деления клв 4" =>'))

if znak==1:
    od = int(input('Введите 1- число!!!'))
    dv = int(input('Введите 2- число!!!'))
    tr = int(input('Введите 3- число!!!'))
    sum= od+dv+tr
    print('ответ: '+str(od)+" + "+str(dv)+" + "+str(tr)+"  = "+str(sum))

elif znak==2:
    od = int(input('Введите 1- число!!!'))
    dv = int(input('Введите 2- число!!!'))
    tr = int(input('Введите 3- число!!!'))
    min=od-dv-tr
    print('ответь: '+str(od)+" - "+str(dv)+" - " +str(tr)+"  = "+str(min))
    print('ответь: '+str(min))


elif znak==3:
    od = int(input('Введите 1- число!!!'))
    dv = int(input('Введите 2- число!!!'))
    tr = int(input('Введите 3- число!!!'))
    min=od*dv*tr
    print('ответь: '+str(od)+" * "+str(dv)+" * " +str(tr)+"  = "+str(min))
    print('ответь: '+str(min))

elif znak == 4:
    od = int(input('Введите 1- число!!!'))
    dv = int(input('Введите 2- число!!!'))
    tr = int(input('Введите 3- число!!!'))
    min = od / dv / tr
    print('ответь: ' + str(od) + " / " + str(dv) + " / " + str(tr) + "  = " + str(min))
    print('ответь: ' + str(min))



else :
    print('вы не правильна нажали кнопку!!!!')
