import turtle as t
import sys
import time as tt


time=['8:20','13:00','18:00']
arrive=['동서울','강릉고속','광주','동대구','포항']
money=[16400,25500,17600,14600,22600] #가격 최신화

def schedule():
    t.shape('turtle')
    t.speed(0)
    t.up()
    t.fd(200)
    t.down()
    t.left(90)
    t.fd(200)
    t.left(90)
    t.fd(400)
    t.left(90)
    t.fd(400)
    t.left(90)
    t.fd(400)
    t.left(90)
    t.fd(200)
    t.up()
    t.goto(-0,200)
    t.down()
    t.right(180)
    t.fd(400)
    t.up()
    t.left(90)
    t.goto(-200,120)#가로줄1
    t.down()
    t.fd(400)
    t.up()
    t.goto(-200,40)#가로줄2
    t.down()
    t.fd(400)
    t.up()
    t.goto(-200,-40)#가로줄3
    t.down()
    t.fd(400)
    t.up()
    t.goto(-200,-120)#가로줄4
    t.down()
    t.fd(400)
    t.up()
    t.goto(-70,250) #고속버스노선조회 위치 
    t.write('고속버스 노선조회',font=("Arial", 20))
    t.goto(-130,225)
    t.down()
    t.color('blue')
    t.write('지역별 터미널',font=("Arial", 10))
    t.up()
    t.goto(70,225)
    t.down()
    t.color('blue')
    t.write('일반요금',font=("Arial", 10))

    t.color('black')
    print_area=['동서울','강릉고속','광주','동대구','포항']
    print_price=['16,400','25,500','17,600','14,600','22,600']
    y=80
    t.up()
    t.goto(-170,150)
    for i in print_area:
        t.write(i,font=("Arial", 15))
        t.goto(-170,y)
        y-=90
    t.goto(30,150)
    y=80
    for i in print_price:
        t.write(i,font=("Arial", 15))
        t.up()
        t.goto(30,y)
        t.down()
        y-=90
    y=-230
    for z in time:
        t.up()
        t.goto(-200,y)
        t.down()
        t.write(z,align="center",font=("Arial", 15))
        y-=30

def bus():    #버스좌석 출력
    t.reset()
    t.shape('turtle')
    t.up()
    t.home()
    t.speed(0)
    t.width(5)
    t.shape('turtle')
    t.down()
    t.left(90)
    t.fd(300)
    t.left(90)
    t.fd(380)
    t.left(90)
    t.fd(600)
    t.left(90)
    t.fd(380)
    t.left(90)
    t.fd(300)
    t.width(3)

    t.hideturtle()
    y=215
    for i in range(9):
        t.up()
        t.goto(-348,y)
        t.down()
        for i in range(0,4) :
            t.color("skyblue")
            t.forward(60)
            t.right(90)    
        y-=64
    y=215
    for i in range(9):
        t.up()
        t.goto(-268,y)
        t.down()
        for i in range(0,4) :
            t.forward(60)
            t.right(90)
            t.end_fill()
        y-=64
    y+=64
    t.up()
    t.goto(-188,y)
    t.down()
    for i in range(0,4) :
        t.forward(60)
        t.right(90)
    t.end_fill()
    y=215

    for i in range(9):
        t.up()
        t.goto(-100,y)
        t.down()
        for i in range(0,4) :
            t.forward(60)
            t.right(90)
            t.end_fill()
        y-=64
    t.showturtle()
    t.color("black")
    y=225
    t.up()
    for i in range(1,26,3):
        t.goto(-325,y)
        t.write(i,font=("Arial", 20))
        y-=64
    y=225
    for i in range(2,27,3):
        t.goto(-245,y)
        t.write(i,font=("Arial", 20))
        y-=64
    y+=64
    t.goto(-170,y)
    t.write(27,font=("Arial", 20))
    y=225
    for i in range(3,29,3):
        t.goto(-80,y)
        t.write(i,font=("Arial", 20))
        y-=64
    

def red_circle(x,y):
    t.up()
    t.goto(x,y)
    t.down()
    t.fillcolor("red")
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.up()
    t.goto(x,y)
    t.down()
    t.write('예매완료',font=("Arial", 8))


def turn(x,y):
    red_circle(x,y)
    if-188<=x<=-128 and -297<=y<=-237:
        a=27
    else:
        y_min=215
        y_max=275
        for i in range(1,26,3):   #1,4,7,10,13,16,19,22,25
            if -348<=x<=-288 and y_min<=y<=y_max:
                a=i
                break
            else:
                a='none'
            y_min-=64
            y_max-=64
            
        if a=='none':
            y_min=215
            y_max=275
            for i in range(2,27,3):
                if -268<=x<=-208 and y_min<=y<=y_max:
                    a=i
                    break
                else:
                    a='none'
                y_min-=64
                y_max-=64
                
            if a=='none':
                y_min=215
                y_max=275
                for i in range(3,29,3):
                    if -100<=x<=-40 and y_min<=y<=y_max:
                        a=i
                        break
                    else:
                        a='none'
                    y_min-=64
                    y_max-=64
    t.color('blue')
    t.up()
    t.goto(25,275)
    t.write(a,font=("Arial", 17))
    t.goto(25,240)
    t.write('번 좌석을 예매하셨습니다',font=("Arial", 17))
    t.color('black')
    t.goto(25,215)
    t.write('----------------------------',font=("Arial", 17))
    t.goto(25,190)
    t.write('도착지 :',font=("Arial", 17))
    t.goto(125,190)
    t.write(arrive[arrive.index(ar)],font=("Arial", 17))
    t.goto(25,165)
    t.write('----------------------------',font=("Arial", 17))
    t.goto(25,140)
    t.write('시간 :',font=("Arial", 17))
    t.goto(125,140)
    t.write(time[time.index(ti)],font=("Arial", 17))
    t.goto(25,115)
    t.write('----------------------------',font=("Arial", 17))
    t.goto(25,90)
    t.write('요금 :',font=("Arial", 17))
    t.goto(125,90)
    t.write(money[arrive.index(ar)],font=("Arial", 17))
    t.onscreenclick(None)
    tt.sleep(3)
    t.reset()
    main()


arrive_list=[]
def bus_arrive():
    global ar
    ar=1
    while(ar):
        ar = input('도착지를 입력해주세요')
        if ar in arrive:
            arrive_list.append(ar)
            break
        else:
            print("다시 입력해주세요")
            ar=1

time_list=[]
def bus_time():
    global ti
    ti=1
    while(ti):
        print('8:20(1),  13:00(2),  18:00(3)')
        ti = input('시간을 입력해주세요')
        if ti in time:
            time_list.append(ti)
            break
        else:
            print("다시 입력해 주세요")
            ti=1



def main():
    choice=int(input('1.버스 예매하기   2.지난 기록 조회  3.프로그램 종료'))
    if choice==1:
        schedule()
        bus_arrive()
        bus_time()
        bus()
        t.onscreenclick(turn)
        print("완료")
        t.mainloop()
        cnt+=1

        
    elif choice==2:
        print('지난 기록을 조회합니다')
        test=len(arrive_list)
        if test==0:
            print('기록이 없습니다.')
            main()
        else:
            for i in range(len(arrive_list)):
                print('목적지 : ',arrive_list[i],'시간 : ',time_list[i])
            main()
            

               
    elif choice==3:
        print('프로그램을 종료합니다.')
        t.bye() 
        sys.exit(1)
    else:
        print('번호를 잘못 입력하셨습니다. 다시입력해 주세요')
        main()
        
main()


