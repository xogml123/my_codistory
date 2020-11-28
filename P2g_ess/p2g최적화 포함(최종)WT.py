from openpyxl import load_workbook
import numpy as np

workbook = load_workbook("C:/project/DATA 입력 기본 형식(다른 섬)-모든섬수정.xlsx", data_only=True)
sheet = workbook['사동_종합']
cost_sheet = workbook['설치비용']


#설치비용 입력
pv_cost_per_unit = cost_sheet['E2'].value
wt_cost_per_unit = cost_sheet['E3'].value
ess_cost_per_W =  cost_sheet['E4'].value
p2g_cost_per_W = cost_sheet['E5'].value#cost value 받는부분
fuel_cell_cost_per_W=cost_sheet['E6'].value


num_pv_init=sheet['J3'].value
num_wt_init=sheet['I3'].value



time_hour = np.arange(0, 8760)
elec_consumption = []
gas_consumption = []
pv_generation_unit = []
wt_generation_unit = []
for row in sheet.rows:
    elec_consumption.append(row[1].value)
    gas_consumption.append(row[2].value)# consumption 받는부분
    pv_generation_unit.append(row[4].value)
    wt_generation_unit.append(row[3].value)
del elec_consumption[0:2]
del gas_consumption[0:2]
del pv_generation_unit[0:2]
del wt_generation_unit[0:2]#불필요한 부분 삭제
'''#array로 만들기
elec_consumption = np.array(elec_consumption)
gas_consumption = np.array(gas_consumption)
pv_generation_unit = np.array(pv_generation_unit)
wt_generation_unit  = np.array(wt_generation_unit)'''







# coefficient 입력
generation2ess = 0.85
generation2p2g = 0.65
p2g2fuelcell = 0.9



def  calc_vol_p2g(*x):
    current_ess = np.zeros(8761)#매번 함수가 호출될때마다 초기화
    current_ess[0]=x[0]/2 #ess 초기 절반채워진 상태에서 시작
    current_p2g = np.zeros(8761)
    vol_ess=x[0]
    final_gas_change_8760=0#time8760 일때 가스량-time0일때 가스량
    elec_generation=[]
    for i in range(0,8761):
        elec_generation.append(x[1]*pv_generation_unit[i]+x[2]*wt_generation_unit[i])
    largest_fuel_cell_power=0
    for time in time_hour:
        gas_demand_from_elec_demand = 0
        gas_supply_from_elec_excess = 0
        gas_supply_from_elec_generation = 0  # 매번초기화 해야하기때문에 for 문 내부로 넣음
        flow_p2g=0
       
       
        if elec_generation[time] * generation2ess + current_ess[time] - elec_consumption[time] < 0:  # ess에 있는 전력 다 쓰고 현재 발전량 다 써도 요구 전력 충당 불가능 = p2g-fuel cell (#1)
            elec_shortage = -(elec_generation[time] * generation2ess + current_ess[time] - elec_consumption[time])  # ess 내의 전력기준 계산
            current_ess[time + 1] = 0
            gas_demand_from_elec_demand = elec_shortage / p2g2fuelcell  # p2g에서 fuelcell  통해서 전력 요구량 채워야 할 때 필요한 가스량,p2g내의 가스량 기준 계산
            if largest_fuel_cell_power<=elec_shortage:
                largest_fuel_cell_power=elec_shortage#elec_shortage 최댓값 largest_fuel_cell_power으로함
            #scen=1
        else:  # 전력 사용을 연료전지 없이 충당할 수 있 경우(elec_generation[time]*generation2ess+current_ess[time]-elec_consumption[time]>0)
            if current_ess[time] > elec_consumption[time] :  # 이미 가지고있는 ess 전력을 모두 사용하지 못해서 강제로 p2g로 넘겨줘야하는 경우(ess만 1시간 전력 유지 되므로)
                gas_supply_from_elec_generation = (current_ess[time] - elec_consumption[time]) * generation2p2g
                if elec_generation[time] * generation2ess < vol_ess:  # elec_generation으로 인해 발생하는 전력을 ess에 저장할때 vol_ess를 넘지 않는 경우
                    current_ess[time + 1] = elec_generation[time] * generation2ess
                    #scen=2
                else:  # elec_generation으로 인해 발생하는 전력을 ess에 저장할때 vol_ess를 넘는 경우
                    current_ess[time + 1] = vol_ess
                    gas_supply_from_elec_excess = (elec_generation[time] - vol_ess/generation2ess) * generation2p2g
                    #scen=3


            else:  # 이미 가지고있는 ess 잔여량을 모두 사용하는 경우
                if elec_generation[time] * generation2ess + current_ess[time] - elec_consumption[time] < vol_ess:  # vol_ess 가 가득차지 않는 경우
                    current_ess[time + 1] = elec_generation[time] * generation2ess + current_ess[time] - elec_consumption[time]
                    #scen=4
                else:  # vol_ess가 가득차는 경우
                    current_ess[time + 1] = vol_ess
                    gas_supply_from_elec_excess = (elec_generation[time] * generation2ess + current_ess[time] -
                                                   elec_consumption[time] - vol_ess) * generation2p2g / generation2ess
                    #scen=5

        flow_p2g = -gas_demand_from_elec_demand + gas_supply_from_elec_excess + gas_supply_from_elec_generation - gas_consumption[time]
        if (current_p2g[time] + flow_p2g)<x[3]:
            current_p2g[time + 1] = current_p2g[time] + flow_p2g
        else:
            current_p2g[time + 1]=x[3]
        #print(current_ess[time+1],current_p2g[time+1],scen)
        if time==8759:
            final_gas_change_8760=current_p2g[time+1]
    max_minus=(abs(np.amin(current_p2g)))
    max_minus=max_minus.astype('int64')
    p2g_capacity=x[3]+max_minus
        
        
    #p2g_capacity = abs(np.amin(current_p2g)) + np.amax(current_p2g)
    return [p2g_capacity,final_gas_change_8760,largest_fuel_cell_power]
#ess,pv,wt 대수 range 로 조정가능
start1=num_pv_init-100*10
finish1=num_pv_init+100*10
start2=num_wt_init-10*1
finish2=num_wt_init+10*1
capacity_ess=[i for i in range(100000,500000,100000)]#향후조정#15
num_pv=[j for j in range(0,num_pv_init+400*5,400)]#10
num_wt=[k for k in range(num_wt_init-2*5,num_wt_init+2*10,2)]#10
num_p2g=[l for l in range(1690*10000*30-150*1000000*2,1690*10000*30+150*1000000*2,150*1000000)]#4

x=[]#[[ess1,pv1,wt1],...[essn,pvn,wtn]]
for a in capacity_ess:
    for b in num_pv:
        for c in num_wt:
            for d in num_p2g:
                x.append([a,b,c,d])
result=[]#result=[[ess용량,pv갯수,wt갯수,pv용량,8760시에서 가스량],[],...[]]
standard_percent=5#추후 지정
for i in x:
    temp=calc_vol_p2g(*i)
    if temp[1]<1690*1000000*standard_percent/100 and temp[1]>0:#1년 총 가스 샤용량의 5%이상보다 final_gas_change_8760 크면 그부분 제외함
        y=[]
        y.append(i[0])
        y.append(i[1])
        y.append(i[2])
        
        y.extend(calc_vol_p2g(*i))
        result.append(y)




smallest_case=1000000000000000000
smallest_case_variate=[]
for i in result:
    
    cost=i[0]*ess_cost_per_W+i[1]*pv_cost_per_unit+i[2]*wt_cost_per_unit+i[3]*p2g_cost_per_W+i[5]*fuel_cell_cost_per_W
    if cost <smallest_case:
        smallest_case=cost
        smallest_case_variate=i.copy()#넓은 범위에서
capacity_ess2=[i for i in range(smallest_case_variate[0]-2500*20,smallest_case_variate[0]+2500*20,2500)]#40
if smallest_case_variate[1]-40*5<=0:
    num_pv2=[j for j in range(0,smallest_case_variate[1]+40*5,40)]
else:
    num_pv2=[j for j in range(smallest_case_variate[1]-40*5,smallest_case_variate[1]+40*5,40)]#10   

num_wt2=[smallest_case_variate[2]-1,smallest_case_variate[2],smallest_case_variate[2]+1]#3
num_p2g2=[l for l in range(smallest_case_variate[3]-37*1000000*2,smallest_case_variate[3]+37*1000000*2,37*1000000)]
x2=[]#[[ess1,pv1,wt1],...[essn,pvn,wtn]]
for a in capacity_ess2:
    for b in num_pv2:
        for c in num_wt2:
            for d in num_p2g2:
                x2.append([a,b,c,d])
result2=[]#result=[[ess용량,pv갯수,wt갯수,pv용량,8760시에서 가스량],[],...[]]
for i in x2:
    temp=calc_vol_p2g(*i)
    if temp[1]<1680*1000000*standard_percent/100 and temp[1]>0:#1년 총 가스 샤용량의 5%이상보다 final_gas_change_8760 크면 그부분 제외함
        y=[]
        y.append(i[0])
        y.append(i[1])
        y.append(i[2])
 
        y.extend(calc_vol_p2g(*i))
        result2.append(y)



smallest_case=1000000000000000000
smallest_case_variate=[]
for i in result2:
    
    cost=i[0]*ess_cost_per_W+i[1]*pv_cost_per_unit+i[2]*wt_cost_per_unit+i[3]*p2g_cost_per_W+i[5]*fuel_cell_cost_per_W
    if cost <smallest_case:
        smallest_case=cost
        smallest_case_variate=i.copy()
    
print('ess=',smallest_case_variate[0])
print('pv=',smallest_case_variate[1])
print('wt=',smallest_case_variate[2])
print('p2g=',smallest_case_variate[3])
print('잉여생산량=',smallest_case_variate[4])
print('fuelcell=',smallest_case_variate[5])
print('cost=',int(smallest_case))
        
        

#이 이후로 result 의 각 원소(리스트)경우에 대한 경제 계산 최소를 구해야함
        
    
